
# File Uploader to SFTP Server

This project serves as a practical demonstration of efficiently uploading files to SFTP servers using provided credentials.

## Features

- **startFileReplicator.sh**: 
  - Execute using the following command:
    ```bash
    ./startFileReplicator.sh
    ```
  - This script duplicates files from the `originalFiles` folder, creating multiple copies with distinct names but identical extensions. These copies are then saved in a folder named `files`.

- **startSFTPFileUpload.sh**:
  - Execute using the following command:
    ```bash
    ./startSFTPFileUpload.sh
    ```
  - After triggering the command above, the script uploads files from the `files` folder to the specified file directory `SFTP_DESTINATION_FOLDER` on the SFTP server, as outlined in the `.env` file.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/dev-vivekkumarverma/file_uploader_to_sftp_server.git
   cd file_uploader_to_sftp_server
   ```

2. Configure your SFTP server credentials in the `.env` file.
  
  #### Content of .env looks like:
  
  ```
  SFTP_HOST=""
  SFTP_USERNAME=""
  SFTP_PASSWORD=""
  SFTP_DESTINATION_FOLDER=""
  ```
3. Run the file replication script:
   ```bash
   ./startFileReplicator.sh
   ```

4. Upload files to the SFTP server:
   ```bash
   ./startSFTPFileUpload.sh
   ```

## Contributing

We welcome contributions! Please check out the [Contribution Guidelines](CONTRIBUTING.md) for detailed instructions on how to contribute to this project.



