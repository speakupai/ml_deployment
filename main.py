#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil, os
from pathlib import Path
from typing import List
import uuid

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
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

'''
def save_uploaded_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    tmp_uploads_path = './uploads/'

    if not os.path.exists(tmp_uploads_path):
        os.makedirs(tmp_uploads_path)

    p = Path(tmp_uploads_path + file)
    print(p)

    save_uploaded_file(file, p)
    return {"filename": file.filename}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    filenames = {"filenames": []}

    tmp_uploads_path = "./uploads/{0}/".format(uuid.uuid1())
    if not os.path.exists(tmp_uploads_path):
        os.makedirs(tmp_uploads_path)
    
    for file in files:
        filenames["filenames"].append(file.filename)
        p = Path(tmp_uploads_path + file.filename)
        print(p)

        save_uploaded_file(file, p)

    return filenames
'''