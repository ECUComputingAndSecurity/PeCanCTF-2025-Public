# (C) 2025 Jordan 'Starnsworth' Hawkes for Pecan+ CTF2025
# Starns@starnsworth.com

from flask import Flask, request, render_template, url_for
import os
import subprocess
from werkzeug.utils import secure_filename
import threading
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    metadata = ''
    uploaded_file = None
    filepath = None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Run exiftool on file
            metadata = extract_metadata(filepath)
            uploaded_file = f"uploads/{filename}"

    response = render_template('index.html', metadata=metadata, file=uploaded_file)

    # Clean up the file after rendering (if it exists)
    if filepath and os.path.exists(filepath):
        delete_file_later(filepath, delay=10)

    return response

def delete_file_later(path, delay=10):
    def delete():
        time.sleep(delay)
        try:
            os.remove(path)
            print(f"[+] Deleted {path}")
        except Exception as e:
            print(f"[!] Failed to delete {path}: {e}")
    threading.Thread(target=delete, daemon=True).start()

def extract_metadata(filepath):
    return subprocess.getoutput(f"exiftool {filepath}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)