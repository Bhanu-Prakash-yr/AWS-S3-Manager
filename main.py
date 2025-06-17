from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import boto3
import os

app = FastAPI()

# Enable CORS (allow all origins for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder for HTML frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html
@app.get("/", response_class=HTMLResponse)
def serve_html():
    with open("static/index.html", "r") as f:
        return f.read()

# S3 client using default AWS credentials
s3 = boto3.client("s3")

@app.post("/upload")
async def upload_file(bucket: str = Query(...), file: UploadFile = File(...)):
    try:
        with open(file.filename, "wb") as f:
            f.write(await file.read())
        s3.upload_file(file.filename, bucket, file.filename)
        os.remove(file.filename)
        return {"message": f" Uploaded {file.filename} to {bucket}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/list")
def list_files(bucket: str = Query(...)):
    try:
        response = s3.list_objects_v2(Bucket=bucket)
        files = [obj["Key"] for obj in response.get("Contents", [])]
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download")
def download_file(bucket: str = Query(...), filename: str = Query(...)):
    try:
        temp_file = f"temp_{filename}"
        s3.download_file(bucket, filename, temp_file)
        return FileResponse(temp_file, filename=filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete")
def delete_file(bucket: str = Query(...), filename: str = Query(...)):
    try:
        s3.delete_object(Bucket=bucket, Key=filename)
        return {"message": f"🗑️ Deleted {filename} from {bucket}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
