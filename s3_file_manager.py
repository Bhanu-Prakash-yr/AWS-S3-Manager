import boto3
import sys
import os

# Create S3 client using default credentials
s3 = boto3.client('s3')

# Upload file to bucket
def upload_file(bucket, file_path):
    try:
        file_name = os.path.basename(file_path)  # Extract file name
        s3.upload_file(file_path, bucket, file_name)
        print(f"Uploaded {file_name} to {bucket}")
    except Exception as e:
        print(f"Upload failed: {e}")

# Download file from bucket
def download_file(bucket, file_name, download_path="."):
    try:
        full_path = os.path.join(download_path, file_name)
        s3.download_file(bucket, file_name, full_path)
        print(f"Downloaded {file_name} to {full_path}")
    except Exception as e:
        print(f"Download failed: {e}")

# List files in bucket
def list_files(bucket):
    try:
        response = s3.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            print(f"📄 Files in {bucket}:")
            for obj in response['Contents']:
                print(f"- {obj['Key']}")
        else:
            print("📂 Bucket is empty.")
    except Exception as e:
        print(f"❌ Could not list files: {e}")

# Delete file from bucket
def delete_file(bucket, file_name):
    try:
        s3.delete_object(Bucket=bucket, Key=file_name)
        print(f"🗑️ Deleted {file_name} from {bucket}")
    except Exception as e:
        print(f"❌ Delete failed: {e}")

# Menu interface
def menu():
    print("\nS3 File Manager")

    bucket = input("Enter your S3 bucket name: ")

    while True:
        print("\n1. Upload File")
        print("2. Download File")
        print("3. List Files")
        print("4. Delete File")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            path = input("Enter path to file for upload: ")
            upload_file(bucket, path)
        elif choice == "2":
            key = input("Enter file name to download: ")
            dest = input("Enter destination folder (press Enter for current): ") or "."
            download_file(bucket, key, dest)
        elif choice == "3":
            list_files(bucket)
        elif choice == "4":
            key = input("Enter file name to delete: ")
            delete_file(bucket, key)
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")
if __name__ == "__main__":
    menu()
