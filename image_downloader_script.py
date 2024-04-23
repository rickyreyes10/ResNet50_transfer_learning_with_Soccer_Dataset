import os
from bing_image_downloader import downloader

def download_and_rename(category, output_dir, round_number, limit):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Use the downloader to download images
    downloader.download(query=category, limit=limit, output_dir=output_dir, 
                        adult_filter_off=True, force_replace=False, timeout=60)

    # Get all the files in the directory
    files = os.listdir(output_dir)
    
    # Filter out any non-JPEG files if necessary
    files = [f for f in files if f.endswith('.jpg')]
    
    # Sort files by creation time
    files.sort(key=lambda x: os.path.getmtime(os.path.join(output_dir, x)))
    
    # Only keep the most recently downloaded files to rename
    files = files[-limit:]
    
    # Rename the files
    for i, file_name in enumerate(files, start=1):
        new_name = f"image_{i}_r{round_number}.jpg"
        os.rename(os.path.join(output_dir, file_name), os.path.join(output_dir, new_name))
    
# Example usage
category = "images of soccer turf shoes only"
output_dir = "dataset/train/soccer_turf_shoe"  # Adjust this path as necessary

# First round of downloads and rename
download_and_rename(category, output_dir, round_number=1, limit=100)

# Second round of downloads and rename
#download_and_rename(category, output_dir, round_number=2, limit=50)
