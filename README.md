# Image Text Extractor

This Python script extracts text from images using Optical Character Recognition (OCR) technology. It processes all supported image files in a specified directory and outputs the extracted text for each image.

## Features

- Extracts text from multiple image formats (PNG, JPG, JPEG, GIF, BMP, TIFF)
- Processes all images in a specified directory
- Checks for Tesseract OCR installation
- Provides error handling for various scenarios
- Outputs extracted text with corresponding filenames

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Tesseract OCR installed and accessible from the command line
- The following Python libraries:
  - Pillow (PIL)
  - pytesseract

## Installation

1. Clone this repository:

git clone https://github.com/yourusername/image-text-extractor.git
cd image-text-extractor
text

2. Install the required Python libraries:

pip install Pillow pytesseract
text

3. Install Tesseract OCR:
- For Windows: Download and install from [GitHub Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki)
- For macOS: `brew install tesseract`
- For Linux: `sudo apt-get install tesseract-ocr`

## Usage

1. Run the script:

python image_text_extractor.py
text

2. When prompted, enter the full path to the directory containing your images.

3. The script will process all supported image files in the specified directory and display the extracted text for each image.

## Supported Image Formats

- PNG
- JPG/JPEG
- GIF
- BMP
- TIFF

## Contributing

Contributions to the Image Text Extractor are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text extraction.
- Thanks to the developers of Pillow and pytesseract for their excellent libraries.
