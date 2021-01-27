#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 2. Create app and model objects
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="style")
templates = Jinja2Templates(directory="templates")

#3. Welcome page

#@app.get("/index", response_class=HTMLResponse)
@app.get("/index")
async def read_item(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})