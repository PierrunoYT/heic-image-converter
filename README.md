# HEIC Image Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/PierrunoYT/heic-image-converter)

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
- Git (for cloning the repository)

### Python Packages

- [pyheif](https://pypi.org/project/pyheif/) - For reading HEIC image files
- [Pillow](https://pypi.org/project/Pillow/) - For processing images
- [Flask](https://pypi.org/project/Flask/) - Web framework for the application

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PierrunoYT/heic-image-converter.git
   cd heic-image-converter
   ```

2. **Install Required Packages:**
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

1. **Install Python and Git:**
   - Download and install Git from [git-scm.com](https://git-scm.com/download/windows)
   - Download the latest Python installer from [python.org](https://www.python.org/downloads/windows/)
   - Run the installers and choose the option to add both to your PATH

2. **Open a Command Prompt or PowerShell:**
   ```cmd
   git clone https://github.com/PierrunoYT/heic-image-converter.git
   cd heic-image-converter
   pip install pyheif Pillow Flask
   python app.py
   ```

### macOS

1. **Install Required Tools:**
   ```bash
   # Install Homebrew if not already installed
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python and Git
   brew install python3 git
   ```
   Or download Python from [python.org](https://www.python.org/downloads/mac-osx/)

2. **Clone and Run:**
   ```bash
   git clone https://github.com/PierrunoYT/heic-image-converter.git
   cd heic-image-converter
   pip3 install pyheif Pillow Flask
   python3 app.py
   ```

### Linux

1. **Install Required Tools:**
   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-pip git
   ```

2. **Clone and Run:**
   ```bash
   git clone https://github.com/PierrunoYT/heic-image-converter.git
   cd heic-image-converter
   pip3 install pyheif Pillow Flask
   python3 app.py
   ```

For all platforms, after starting the application, open your browser and navigate to [http://localhost:5000](http://localhost:5000) to use the web interface.

## Notes on JPEG/JPG

- **JPEG** stands for "Joint Photographic Experts Group"
- Both `.jpg` and `.jpeg` refer to the same image format
- This application uses `.jpg` as the default extension for JPEG files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Repository

View the project on GitHub: [https://github.com/PierrunoYT/heic-image-converter](https://github.com/PierrunoYT/heic-image-converter)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 PierrunoYT

Feel free to modify or extend this project based on your needs.