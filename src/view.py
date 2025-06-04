import os
import subprocess
from pathlib import Path
import platform

def open_first_image_in_folder(folder_path):
    p = Path(folder_path)
    # Image extensions to consider
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp']

    # List image files sorted by name
    images = sorted([f for f in p.iterdir() if f.is_file() and f.suffix.lower() in image_extensions])
    if not images:
        print(f"No image files found in {folder_path}")
        return

    first_image = images[0]
    # Open with default image viewer
    try:
        #os.startfile(str(first_image))
        open_file_cross_platform(str(first_image))
        print(f"Opened {first_image}")
    except Exception as e:
        print(f"Failed to open image: {e}")

def open_file_cross_platform(filepath):
    system = platform.system()
    filepath = str(filepath)

    if system == 'Windows':
        os.startfile(filepath)
    elif system == 'Darwin':  # macOS
        subprocess.run(['open', filepath])
    else:  # Linux and others
        subprocess.run(['xdg-open', filepath])

if __name__ == "__main__":
    open_first_image_in_folder('exports')
