#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil, os
from pathlib import Path
#from typing import List
#import uuid
#from Model import predict_type
from inference import inference
from utils.spectrogram import create_spectrogram

UPLOAD_FOLDER = 'uploads'

# 2. Create app and model objects
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="styles")

templates = Jinja2Templates(directory="templates/")

#3. Welcome page
@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse("welcome.html", {"request": request, "message":"message"})

@app.post("/uploads")
async def create_upload_file(request:Request,
                            #background_tasks:BackgroundTasks,
                            file: UploadFile = File(...), 
                            ):
    
    tmp_uploads_path = './uploads/'

    if not os.path.exists(tmp_uploads_path):
        os.makedirs(tmp_uploads_path)

    p = Path(tmp_uploads_path + file.filename)
    save_uploaded_file(file, p)

    #background_tasks.add_task(create_spectrogram(p), message='your file is being processed')
    
    #inference(p)
    
    return templates.TemplateResponse("upload_page.html", 
                                    {"request": request, 
                                    "filename": file.filename,
                                    "type":file.content_type})


def save_uploaded_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()

@app.get("/spect")
async def spect(file_path: str, response: FileResponse):
    spectogram = create_spectrogram(file_path)
    return FileResponse('spectrogram', media_type='image/png')

'''@app.get("/inf")
async def run_inference(path):
    inference(path)'''
