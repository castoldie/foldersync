import os
import shutil
import argparse
import time

def sync_folders(src, dst, interval, log_file):
    
    while True:
        # get list of files in the source folder
        src_files = set(os.listdir(src))
        dst_files = set(os.listdir(dst))

        # find new and modified files in the source folder
        new_files = src_files - dst_files
        modified_files = src_files & dst_files

        # copy new and modified files to the replica folder
        for file in new_files:
            src_path = os.path.join(src, file)
            dst_path = os.path.join(dst, file)
            shutil.copy2(src_path, dst_path)
            with open(log_file, 'a') as f:
                f.write(f'{src_path} copied to {dst_path}\n')
            print(f'{src_path} copied to {dst_path}')

        for file in modified_files:
            src_path = os.path.join(src, file)
            dst_path = os.path.join(dst, file)
            if os.path.getmtime(src_path) > os.path.getmtime(dst_path):
                shutil.copy2(src_path, dst_path)
                with open(log_file, 'a') as f:
                    f.write(f'{src_path} copied to {dst_path}\n')
                print(f'{src_path} copied to {dst_path}')

        # remove files from the replica folder that no longer exist in the source folder
        for file in dst_files - src_files:
            dst_path = os.path.join(dst, file)
            os.remove(dst_path)
            with open(log_file, 'a') as f:
                f.write(f'{dst_path} removed\n')
            print(f'{dst_path} removed')

        # wait for the specified interval
        time.sleep(interval)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sync folders')
    parser.add_argument('src', help='Source folder')
    parser.add_argument('dst', help='Replica folder')
    parser.add_argument('interval', type=int, help='Sync interval in seconds')
    parser.add_argument('log', help='Log file')
    args = parser.parse_args()

    sync_folders(args.src, args.dst, args.interval, args.log)
