# Foldersync

Hello everyone! Foldersync is a very simple synchronization tool that takes the status of a source folder and clones it onto a destination folder, regularly every given time.

## Installation

To install the package, first clone this repository:

 -- todo add git clone command

Then to install said package is as easy as running:

`make install`

## Usage

### To start the synchronization process you have 2 options:

1 - You can manually start the program by running in your terminal:
    
    `folder_sync /path/to/source /path/to/replica 3600 /path/to/log.txt`
    this will synchronize the /path/to/source folder with the /path/to/replica folder every 3600 seconds (1 hour), and log the file operations to /path/to/log.txt.

2 - You can simply run, always in your terminal while in the root of your repo´s local directory:

    `make test`
    this will run the same command as in the previous point, but pointing the test_X folders contained in this repo, syncing every 10 seconds, so you can see by yourself the behaviour of this app without waiting as much.

## Note:
The program will only copy the files from source to replica, it won't remove or delete the files from source. It is also one way synchronization and will only make the replica folder identical to the source folder.

It is also important to note that the package uses a while loop to continuously check the contents of the source and replica folders, and copies new and modified files from the source folder to the replica folder. It also removes files from the replica folder that no longer exist in the source folder. The package also logs the file creation/copying/removal operations to a file and the console output.