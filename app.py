#!/usr/bin/env python3
# © 2025 HEIC Converter

import io
from pathlib import Path
from typing import Set
from flask import Flask, request, render_template, send_file, flash, redirect
import secrets
from converter_core import HeicConverter

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Generate a secure random secret key

# Allow only HEIC/HEIF file extensions for upload
ALLOWED_EXTENSIONS: Set[str] = {"heic", "heif", "jpg", "jpeg", "png", "webp", "bmp"}
ALLOWED_FORMATS: Set[str] = {"HEIC", "JPEG", "PNG", "WEBP", "BMP"}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename: str) -> bool:
    """Check if the file extension is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

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

        if not file.filename or not allowed_file(file.filename):
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
            output_bytes = HeicConverter.convert_heic(file_bytes, output_format=target_format)

            # Create a safe output filename using the preferred extension
            extension = HeicConverter.get_extension_for_format(target_format)
            output_filename = f"{Path(file.filename).stem}.{extension}"

            return send_file(
                io.BytesIO(output_bytes),
                mimetype=f"image/{target_format.lower()}",
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