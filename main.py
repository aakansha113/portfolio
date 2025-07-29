from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# In-memory counter
download_count = 0

@app.get("/", response_class=FileResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/download-resume")
async def download_resume():
    global download_count
    download_count += 1
    file_path = "static/resume/Aakansha_Resume.pdf"
    return FileResponse(path=file_path, filename="Aakansha_Resume.pdf", media_type="application/pdf")

@app.get("/download-count")
async def get_count():
    return {"downloads": download_count}
