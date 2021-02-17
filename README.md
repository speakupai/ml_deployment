# Deploying AI Models on Cloud

The repo contains code for deploying a solution on AWS. We will be using Fast API for building the app.

## Environment
* fastapi==0.63.0
* librosa==0.8.0
* matplotlib==3.1.2
* numpy==1.19.5
* Pillow==8.1.0
* pypesq==1.2.4
* pystoi==0.3.3
* starlette==0.13.6
* torch==1.7.1
* torchaudio==0.7.2
* tqdm==4.47.0
* uvicorn==0.13.3
* Werkzeug==1.0.1

## Project Description

The files and folders in this project and their usage is as follows.

* models:
Contains pytorch model architecture used in this project. These models are loaded and updated using the saved checkpoints to run inference.

* sound_samples:
Containes samples to run inference.

* static:
Contains static files, css files, images to display and js files.

* templates:
Contains templates for web app.

* uploads:
Folder to store uploaded files.

* utils:
Utility files for various supporting functions. Contains files for creating spectrograms, parameters for inference, data file to pre and post process audio files.

* app.py
app file

* main.py
File containing all of the functionality in the app. It imports certain other files to run properly.

* Inference.py
Script to run inference o the audio clips.

## Local Run
To run the app locally run the following

```
git clone git@github.com:speakupai/ml_deployment.git
cd ml_deployment

$ python app.py
```

The app should look like this
<img src="" height="300" width="300">
