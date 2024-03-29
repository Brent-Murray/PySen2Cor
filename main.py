import os
import shutil
import subprocess
import zipfile
from tqdm import tqdm

def unzip_directory(in_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(in_dir)
    for item in tqdm(
        os.listdir(in_dir), desc="Unzipping Folders", leave=True, colour="red"
    ):
        if item.endswith(".zip"):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(out_dir)
        zip_ref.close()
        
        
def run_l2a_process(input_folder, output_folder, l2a_bat):
    # Check if output folder exists, create if necessary
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the L2A_Process command
    l2a_process_cmd = f"{l2a_bat} {input_folder} --resolution 20 --tif --output_dir {output_folder}"
    # Run L2A_Process command
    try:
        subprocess.run(l2a_process_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running L2A_Process: {e}")
        
        
def delete_directory(directory):
    try:
        shutil.rmtree(directory)
    except OSError as e:
        print(f"Error: {e.filename, e.strerror}")
        
        
def main(directory, l2a_bat):
    unzip_folder = f"{directory}/unzip"
    output_folder = f"{directory}/L2A"
    unzip_directory(directory, unzip_folder)
    safe_folders = [
        f"{unzip_folder}/{file}"
        for file in os.listdir(unzip_folder)
        if file.endswith(".SAFE")
    ]
    for safe_folder in tqdm(
        safe_folders, desc="L2A Processing", leave=True, colour="green"
    ):
        run_l2a_process(safe_folder, output_folder, l2a_bat)
        delete_directory(safe_folder)
    delete_directory(unzip_folder)
    
if __name__ == "__main__":
    main("your/path/here", "path/to/Sen2Cor-02.11.00-win64/L2A_Process.bat")