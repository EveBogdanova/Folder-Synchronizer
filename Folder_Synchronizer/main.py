import os, time
from comparing_folders import compare_folders_with_hash
from synch_folders import synchronize_folders
from input_functions import *



def main():

    print('Folder synchronization\n')
    LOG = path_to_log_file()
    source = input_source(LOG)
    replica = input_replica(LOG)
    synch_interval = get_interval()

    while True:
        # check if source folder exists
        if os.path.isdir(source):
            print('Source folder: ONLINE')
            log('source folder: ONLINE',LOG)
        else:
            print('Source folder: NOT FOUND')
            log('source folder: NOT FOUND',LOG)
            break
        # check if replica folder exists
        if os.path.isdir(replica):
            print('Replica folder: ONLINE')
            log('replica folder: ONLINE',LOG)
        else:
            print('Replica folder: NOT FOUND')
            log('replica folder: NOT FOUND',LOG)
            break
        # check if source and replica folders are identical
        if compare_folders_with_hash(source, replica):
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f'[{current_time}] source and replica folders are synchronized')
            log('source and replica folders are synchronized',LOG)
            time.sleep(synch_interval)
            continue    
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        synchronize_folders(source,replica,now,LOG)
        time.sleep(synch_interval)
        

    
if __name__ == "__main__":
    main()
