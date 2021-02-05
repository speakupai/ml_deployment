# python3

''' create librosa spectorgram '''

import librosa
from librosa.feature import melspectrogram
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
import time

save_folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Projects/Audio_super_res/ml_deployment/static/spectrograms'

def spect_stream(audio_path):
   # find duration
   clip_len = librosa.get_duration(filename = audio_path, sr=16000)
   
   # load audio
   for sub_clip in range(0, int(clip_len), 10):
      # load subsample of the file
      snd, sr = librosa.load(audio_path, sr=16000, offset=sub_clip, duration=10)

      # create spectrogram
      spect = melspectrogram(y=snd, sr=sr)
      fig, ax = plt.subplots()
      S_dB = librosa.power_to_db(spect, ref=np.max)
      img = librosa.display.specshow(S_dB, x_axis='time',
                                     y_axis='mel', sr=sr,
                                     fmax=8000, ax=ax)
      fig.colorbar(img, ax=ax, format='%+2.0f dB')
      ax.set(title='Mel-frequency spectrogram')

      fig.savefig(os.path.join(save_folder, str(sub_clip)+'.png'), format='png')
