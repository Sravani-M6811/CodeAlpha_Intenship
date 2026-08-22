import os
import shutil

source_folder = "source_images"
destination_folder = "jpg_files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

moved_files = 0

print("================================")
print("       FILE AUTOMATION")
print("================================")

if not os.path.exists(source_folder):
    print("Source folder does not exist.")
    print("Please create the 'source_images' folder first.")
else:

    for filename in os.listdir(source_folder):

        source_path = os.path.join(source_folder, filename)

        if filename.lower().endswith(".jpg"):

            destination_path = os.path.join(
                destination_folder,
                filename
            )

            shutil.move(source_path, destination_path)

            print("Moved:", filename)
            moved_files += 1

    print("\nTotal JPG files moved:", moved_files)
    print("Automation completed successfully!")