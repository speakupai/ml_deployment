import os

import librosa
import numpy as np
import soundfile as sf
import torch
from tqdm import tqdm

from utils import data, spectrogram, spectrogram_clean
from models.hifi_gan import Generator
from models.wavenet import WaveNet

from utils.hparams import hparams as hp

def inference(audio_clip):
    original_file = audio_clip
    save_dir = './uploads'
    checkpoint_path = './saved_model/latest_checkpoint.pt'
    #default_inf_device = 'cpu',

    # Load checkpoint
    checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))

    # Initializing model, optimizer, criterion and scaler
    model = Generator(wavenet=WaveNet())
    model.to('cpu')
    model.load_state_dict(checkpoint['generator_state_dict'])
    model.eval()

    inference_files = [original_file]

    with torch.no_grad():
        for file in inference_files:
            filename = os.path.splitext(os.path.split(file)[1])[0]
            x, _ = librosa.load(file, sr=16000, mono=True)
            target_length = len(x)
            x = torch.tensor(x).to('cpu')
            x = data.preprocess_inference_data(x,
                                            hp.inference.batched,
                                            hp.inference.batch_size,
                                            hp.inference.sequence_length,
                                            16000)

            # run inference and create spectrograms
            y = []
            for x_batch in tqdm(x):
                spect_orig = np.array(x_batch[0])
                spectrogram.create_spectrogram(spect_orig)
                clean_temp = model.inference(x_batch)
                y.append(clean_temp)
                spectrogram_clean.create_spectrogram(np.array(clean_temp))
            y = data.postprocess_inference_data(y, hp.inference.batched,
                                                16000)
            y = y[:target_length].detach().cpu().numpy()
            sf.write(os.path.join(save_dir, f'{filename}_denoised.wav'),
                    y.astype(np.float32), samplerate=hp.dsp.sample_rate)
