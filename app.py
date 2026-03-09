#!/usr/bin/env python3
# © 2025 HEIC Converter

import io
import os
from pathlib import Path
from typing import Set
from flask import Flask, request, render_template, send_file, flash, redirect, url_for
import secrets
from converter_core import HeicConverter

# Define constants before app initialization
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS: Set[str] = {"heic", "heif", "jpg", "jpeg", "png", "webp", "bmp"}
ALLOWED_FORMATS: Set[str] = {"HEIC", "JPEG", "PNG", "WEBP", "BMP"}
MIME_TYPES: dict = {
    "JPEG": "image/jpeg",
    "PNG": "image/png",
    "WEBP": "image/webp",
    "BMP": "image/bmp",
    "HEIC": "image/heif",
}

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH  # Set the maximum upload size

# Allow only HEIC/HEIF file extensions for upload

def allowed_file(filename: str) -> bool:
    """Check if the file extension is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file uploads that exceed the size limit."""
    flash("File too large. Maximum file size is 16MB.")
    return redirect(url_for("index"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part in the request")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash("Unsupported file type. Please select a valid image file (HEIC, JPEG, PNG, WEBP, or BMP).")
            return redirect(request.url)

        # Get and validate target format
        target_format = request.form.get("format", "JPEG").upper()
        if target_format not in ALLOWED_FORMATS:
            flash("Unsupported target format")
            return redirect(request.url)

        try:
            # Read and process the file using the core converter
            file_bytes = file.read()
            quality = int(request.form.get("quality", 85))
            quality = max(1, min(quality, 100))
            output_bytes = HeicConverter.convert_heic(file_bytes, output_format=target_format, quality=quality)

            # Create a safe output filename using the preferred extension
            extension = HeicConverter.get_extension_for_format(target_format)
            output_filename = f"{Path(file.filename).stem}.{extension}"

            return send_file(
                io.BytesIO(output_bytes),
                mimetype=MIME_TYPES[target_format],
                as_attachment=True,
                download_name=output_filename,
                max_age=0
            )
        except ValueError as e:
            flash(str(e))
            return redirect(request.url)
        except Exception as e:
            flash("An unexpected error occurred while processing the file")
            app.logger.error(f"Error processing file: {str(e)}")
            return redirect(request.url)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # Run the web application