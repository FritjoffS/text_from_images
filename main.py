import os
import sys
from PIL import Image
import pytesseract
from pytesseract import TesseractError
import subprocess

def check_tesseract_installed():
    """
    Check if Tesseract OCR is installed and accessible.
    
    Returns:
    bool: True if Tesseract is installed, False otherwise.
    """
    try:
        subprocess.run(['tesseract', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def extract_text_from_image(image_path):
    """
    Extract text from an image file.
    
    Args:
    image_path (str): Path to the image file.
    
    Returns:
    str: Extracted text from the image.
    """
    try:
        # Open the image using PIL (Python Imaging Library)
        with Image.open(image_path) as img:
            # Use pytesseract to extract text from the image
            text = pytesseract.image_to_string(img)
            return text.strip()
    except IOError as e:
        print(f"Error opening image file: {e}")
        return None
    except TesseractError as e:
        print(f"Tesseract error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def process_images_in_directory(directory):
    """
    Process all image files in a given directory.
    
    Args:
    directory (str): Path to the directory containing image files.
    
    Returns:
    dict: A dictionary with image filenames as keys and extracted text as values.
    """
    results = {}
    supported_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')
    
    try:
        for filename in os.listdir(directory):
            if filename.lower().endswith(supported_formats):
                file_path = os.path.join(directory, filename)
                text = extract_text_from_image(file_path)
                if text:
                    results[filename] = text
                else:
                    print(f"No text extracted from {filename}")
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Permission denied to access directory: {directory}")
    except Exception as e:
        print(f"An unexpected error occurred while processing directory: {e}")
    
    return results

def main():
    # Check if Tesseract is installed and accessible
    if not check_tesseract_installed():
        print("Error: Tesseract is not installed or not in the system PATH.")
        sys.exit(1)

    # Get the directory path from the user
    directory = input("Enter the path to the directory containing images: ").strip()
    
    # Process images and get results
    results = process_images_in_directory(directory)
    
    # Print results
    if results:
        print("\nExtracted text from images:")
        for filename, text in results.items():
            print(f"\nFilename: {filename}")
            print("Extracted text:")
            print(text)
            print("-" * 50)
    else:
        print("No text was extracted from any images in the specified directory.")

if __name__ == "__main__":
    main()
