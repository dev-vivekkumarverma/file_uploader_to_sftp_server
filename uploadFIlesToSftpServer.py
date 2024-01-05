import os
import pysftp
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def upload_to_sftp(local_folder, sftp_host, sftp_username, sftp_password, sftp_folder):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  # Skip host key verification

    with pysftp.Connection(
        host=sftp_host, username=sftp_username, password=sftp_password, cnopts=cnopts
    ) as sftp:
        print("Connection successfully established... ")

        with sftp.cd(sftp_folder):
            for root, dirs, files in os.walk(local_folder):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    sftp.put(local_file_path)
                    print(f"Uploaded: {local_file_path} to {sftp_folder}/{file}")


# Retrieve credentials from environment variables
local_files_folder = "files"  # Replace with your local folder name
sftp_host = os.getenv("SFTP_HOST")
sftp_username = os.getenv("SFTP_USERNAME")
sftp_password = os.getenv("SFTP_PASSWORD")
sftp_folder = os.getenv("SFTP_DESTINATION_FOLDER")

upload_to_sftp(local_files_folder, sftp_host, sftp_username, sftp_password, sftp_folder)
