# Media Backup and Compression Tool

This Python script is designed to help you back up media files from your source directory, skip hidden folders, and optionally compress the backup into gzip files. It provides the flexibility to gzip folders individually or into a single archive, all within the "Media Backup" directory.

## Features

- Scans your source directory for media files (images and videos).
- Copies media files to a designated backup directory while ignoring hidden folders.
- Offers the choice to gzip the entire backup or individual media folders.
- Keeps track of backed-up files in a "backedup_media.txt" file.

## Prerequisites

- Python 3.x
- Ensure the required Python packages (`gzip`, `os`, `shutil`) are installed.

## Usage

1. Place the script in the directory where you want to back up your media files.

2. Open a terminal/command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

   ```shell
   python automate_media_backup.py
