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
import shutil

# 2. Create app and model objects
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="styles")
templates = Jinja2Templates(directory="templates/")

#3. Welcome page

@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse("welcome.html", {"request": request, "message":"message"})

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}