# AWS-S3-Manager
 S3 File Manager with FastAPI This is a full-stack file manager built with FastAPI and a simple HTML/JavaScript frontend, allowing you to upload, list, download, and delete files from an AWS S3 bucket.
#S3 File Manager with FastAPI

A full-stack file manager built with **FastAPI** and a simple **HTML/JavaScript frontend**, enabling you to **upload**, **list**, **download**, and **delete** files from an **AWS S3 bucket**.

---
![Screenshot 2025-06-17 155623](https://github.com/user-attachments/assets/6913a939-716b-498f-92a8-0727ac09b1c2)


##  Features

-  Upload files to a selected S3 bucket  
-  List all objects in the bucket  
-  Download files directly from S3  
-  Delete files from the bucket  
-  Uses AWS credentials via `boto3`  
-  CORS-enabled for frontend-backend communication  
-  Serves static HTML frontend via FastAPI

---

## Tech Stack

- **Backend**: FastAPI + Boto3 (AWS SDK for Python)  
- **Frontend**: HTML + JavaScript (Fetch API)  
- **Cloud Storage**: AWS S3  
- **Server**: Uvicorn (for local development)


