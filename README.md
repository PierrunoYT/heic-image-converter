# HEIC Image Converter

A modern web application for bi-directional image conversion between HEIC and other popular formats (JPEG, PNG, WEBP, BMP). Convert your images to HEIC for better compression, or convert HEIC files to widely supported formats for better compatibility.

## Features

- Two-way conversion support:
  - Convert HEIC images to JPEG, PNG, WEBP, or BMP formats
  - Convert JPEG, PNG, WEBP, or BMP images to space-efficient HEIC format
- Modern, responsive web interface with drag-and-drop support
- Dark/light theme support
- Clean error handling with user-friendly messages
- Handles both `.jpg` and `.jpeg` extensions consistently (default is `.jpg` for JPEG)
- Preserves image quality during conversion

## Project Structure

- `app.py`: The main Flask web application that handles image conversion
- `converter_core.py`: Contains the core conversion functionality
- `templates/`: Contains HTML templates for the web application
- `static/`: Contains static assets (CSS, JavaScript) for the web interface
- `README.md`: This file
- `.gitignore`: Specifies which files Git should ignore
- `LICENSE`: MIT License file

## Requirements

- Python 3.6 or higher

### Python Packages

- [pyheif](https://pypi.org/project/pyheif/) - For reading HEIC image files
- [Pillow](https://pypi.org/project/Pillow/) - For processing images
- [Flask](https://pypi.org/project/Flask/) - Web framework for the application

Install the required packages with:

```bash
pip install pyheif Pillow Flask
```

## Usage

To run the web application:

```bash
python app.py
```

Then open your browser and navigate to [http://localhost:5000](http://localhost:5000) to use the interface.

The web interface allows you to:
1. Drag and drop any supported image file (HEIC, JPEG, PNG, WEBP, or BMP) or click to select files
2. Choose your desired output format:
   - Convert from HEIC to JPEG, PNG, WEBP, or BMP for better compatibility
   - Convert from JPEG, PNG, WEBP, or BMP to HEIC for efficient storage
3. Convert and download the processed image instantly
4. Toggle between dark and light themes for comfortable viewing

## Platform-Specific Instructions

### Windows

1. **Install Python:**
   - Download the latest Python installer from [python.org](https://www.python.org/downloads/windows/)
   - Run the installer and choose the option to add Python to your PATH

2. **Open a Command Prompt or PowerShell:**
   ```cmd
   cd path\to\your\project
   pip install pyheif Pillow Flask
   python app.py
   ```

### macOS

1. **Install Python:**
   ```bash
   brew install python3
   ```
   Or download from [python.org](https://www.python.org/downloads/mac-osx/)

2. **Open Terminal:**
   ```bash
   cd /path/to/your/project
   pip3 install pyheif Pillow Flask
   python3 app.py
   ```

### Linux

1. **Install Python:**
   ```bash
   sudo apt-get update && sudo apt-get install python3 python3-pip
   ```

2. **Open Terminal:**
   ```bash
   cd /path/to/your/project
   pip3 install pyheif Pillow Flask
   python3 app.py
   ```

For all platforms, after starting the application, open your browser and navigate to [http://localhost:5000](http://localhost:5000) to use the web interface.

## Notes on JPEG/JPG

- **JPEG** stands for "Joint Photographic Experts Group"
- Both `.jpg` and `.jpeg` refer to the same image format
- This application uses `.jpg` as the default extension for JPEG files

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 PierrunoYT

Feel free to modify or extend this project based on your needs. 