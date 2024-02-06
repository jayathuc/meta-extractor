import os
from datetime import datetime

# Specify the root folder path here
root_folder_path = 'path/to/your/folder'

# Specify the output file where the metadata will be saved
output_file_path = 'file_metadata.txt'

# Open the output file in write mode with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as file:
    # Write the header row
    file.write("FilePath,FileName,FileSize(Bytes),CreationDate,ModificationDate\n")

    # Use os.walk() to iterate over each directory in the directory tree
    for folder_path, _, filenames in os.walk(root_folder_path):
        for filename in filenames:
            # Check if the file is an MP4 file
            if filename.lower().endswith('.mp4'):
                # Get full file path
                file_path = os.path.join(folder_path, filename)
                
                # Get file size
                file_size = os.path.getsize(file_path)
                
                # Get file creation and modification dates
                creation_date = os.path.getctime(file_path)
                modification_date = os.path.getmtime(file_path)
                
                # Format dates for readability
                creation_date_formatted = datetime.fromtimestamp(creation_date).strftime('%Y-%m-%d %H:%M:%S')
                modification_date_formatted = datetime.fromtimestamp(modification_date).strftime('%Y-%m-%d %H:%M:%S')
                
                # Write file metadata to the output file, including relative file path for clarity
                relative_file_path = os.path.relpath(file_path, start=root_folder_path)
                file.write(f"{relative_file_path},{filename},{file_size},{creation_date_formatted},{modification_date_formatted}\n")
                
                # Print progress message
                print(f"Info of '{relative_file_path}' saved successfully.")

print("Metadata extraction complete. Check the file:", output_file_path)

# End
