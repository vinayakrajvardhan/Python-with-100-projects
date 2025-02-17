import os
import dropbox
import dotenv

# Load environment variables
dotenv.load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Initialize Dropbox client
d = dropbox.Dropbox(ACCESS_TOKEN)

# Directory containing files to upload
local_directory = "files"

# Iterate through all files in the directory
for filename in os.listdir(local_directory):
    # Build the full local file path
    local_filepath = os.path.join(local_directory, filename)

    # Check if it's a file (not a directory)
    if os.path.isfile(local_filepath):
        with open(local_filepath, 'rb') as file:
            content = file.read()
            # Upload to Dropbox with the same filename
            dropbox_path = f'/{filename}'
            d.files_upload(content, dropbox_path, mode=dropbox.files.WriteMode('overwrite'))
            print(f'File {filename} uploaded successfully!')