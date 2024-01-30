# metadata_analyzer.py

import os
from PIL import Image

def analyze_metadata(file_path):
    try:
        if file_path.lower().endswith(('.jpg', '.jpeg')):
            image = Image.open(file_path)
            exif_data = image._getexif()
            if exif_data:
                print("Metadata for", file_path)
                for tag, value in exif_data.items():
                    print(f"{tag}: {value}")
            else:
                print("No metadata found for", file_path)
        # Add support for other file types if needed (e.g., PDF)
        else:
            print("Unsupported file format:", file_path)
    except Exception as e:
        print(f"Error analyzing metadata for {file_path}: {e}")

if __name__ == "__main__":
    file_path = input("Enter path to the file to analyze metadata: ")
    if os.path.exists(file_path):
        analyze_metadata(file_path)
    else:
        print("File not found:", file_path)
