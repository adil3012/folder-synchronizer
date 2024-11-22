import logging
import os
import shutil
import argparse

def synch_files(source, replica):
    # Check if replica folder exists, if not create it
    if not os.path.isdir(replica):
        os.makedirs(replica)
        logging.info(f"Created replica directory: {replica}")

    # Ensure source folder exists
    if not os.path.isdir(source):
        raise argparse.ArgumentError(None, "Source does not exist.")

    # List items in source and replica
    source_items = os.listdir(source)
    replica_items = os.listdir(replica)

    for item in source_items:
        source_path = os.path.join(source, item)
        replica_path = os.path.join(replica, item)

        if os.path.isdir(source_path):
            # Recursively sync subdirectories
            synch_files(source_path, replica_path)
        else:
            # Copy file if not exists or is different from the one in replica
            if not os.path.exists(replica_path):
                shutil.copy2(source_path, replica_path)
                logging.info(f"Copied/Updated file: {source_path} -> {replica_path}")
    
    # Remove files in replica that are no longer in source
    for file in replica_items:
        if file not in source_items:
            os.remove(os.path.join(replica, file))
            log_message = f"{file} has been deleted."
            logging.info(log_message)

if __name__ == '__main__':
    print("Script is running...")
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Synchronize two folders.')
    parser.add_argument('--source', required=True, help='Path to the source folder.')
    parser.add_argument('--replica', required=True, help='Path to the replica folder.')
    parser.add_argument('--logfile', required=True, help='Path to the log file.')

    args = parser.parse_args()
    
    # Call the sync function
    synch_files(args.source, args.replica)
