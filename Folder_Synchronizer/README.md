# Folder-Synchronizer

## Program that synchronizes two folders: source and replica

> - The program maintains a full, identical copy of source folder at replica folder
> - Implemented synchronization is one-way
> - Synchronization is performed periodically (interval is provided with the command line arguments)
> - File creation/copying/removal operations are logged to a file and to the console output



## Project directory structure
```
Folder_Synchronizer
├── main.py                   # File that contains Main Function
├── comparing_folders.py      # File that contains functions to compare files and directories (folders)
├── input_functions.py        # File that contains functions to get correct input from console
├── synch_folders.py          # File that contains functions to synchronize and copy directories (folders)
└── README.md
```
