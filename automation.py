import os
import shutil

# Please create an images folder within th same directory

source_folder = "images"
destination_folder = "jpg_files"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)

    if filename.lower().endswith(".jpg"):
        destination_path = os.path.join(
            destination_folder, filename
        )

        shutil.move(source_path, destination_path)

        print("Moved:", filename)
print("Finished moving JPG files.")