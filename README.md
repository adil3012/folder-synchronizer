# Folder Synchronization Script

This Python script synchronizes two folders by copying files from the source folder to the replica folder. It will copy new or updated files from the source and remove files from the replica that no longer exist in the source. This is useful for backup or file management systems.

## Features
- Syncs files from a source folder to a replica folder.
- Recursively syncs subdirectories.
- Deletes files in the replica that do not exist in the source.
- Logs the synchronization actions to a specified logfile.

## Installation

### Prerequisites
- Python 3.x (Tested with Python 3.6 and above)
- The script uses Python's built-in `argparse`, `os`, `shutil` libraries, so there are no additional dependencies.

