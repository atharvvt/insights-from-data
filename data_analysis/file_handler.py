import os
TEMP_DIR = "file_uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

def handle_uploaded_file(file):
    file_path = os.path.join(TEMP_DIR, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path