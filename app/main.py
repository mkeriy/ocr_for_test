from typing import List
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse,ORJSONResponse
from fastapi.templating import Jinja2Templates
from app.ocr import det_and_rec

app = FastAPI()

templates = Jinja2Templates("./app/templates")

@app.post("/output", response_class=ORJSONResponse)
def img_processing(
    files: List[bytes] = File(description="Multiple files as bytes")
):
    result = det_and_rec(files[0])
    # draw_detected(files[0], res)
    return  ORJSONResponse(result)

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request" : request})



