import os, time
import shutil
from comparing_folders import compare_files_with_hash
from input_functions import log


# function for synchronizing folders
# uses recursion to synchronize subfolders

def synchronize_folders(src, repl, cur_time, LOG):
    # counters for synchronized items
    synchronized_items = 0
    updated_items = 0
    deleted_items = 0

    try:
        files = os.listdir(src)
        files_replica = os.listdir(repl)
        # compare 2 lists
        for file in files_replica:
            if os.path.isdir(repl+'/'+file):
                if file in files:
                    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    synchronize_folders(src+'/'+file,repl+'/'+file,now,LOG)                
                else:
                    log(f'{file} is deleted',LOG)
                    shutil.rmtree(repl+'/'+file)
                    deleted_items +=1 
            if os.path.isfile(repl+'/'+file):
                if file in files:
                    if compare_files_with_hash(src+'/'+file, src+'/'+file):
                        log(f'{file} is synchronized',LOG)
                        synchronized_items += 1
                    else:
                        # copy file from source to replica
                        updated_items += 1
                        os.remove(repl+'/'+file)
                        os.system('copy '+src+'/'+file+' '+repl)
                        shutil.copy2(src+'/'+file, repl) 
                        log(f'{file} is updated',LOG)
                if file not in files:
                    # delete file in replica
                    log(f'{file} is deleted',LOG)
                    deleted_items += 1
                    os.remove(repl+'/'+file)
        for file in files:
            if os.path.isdir(src+'/'+file):
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                synchronize_folders(src+'/'+file,repl+'/'+file,now,LOG)
            if os.path.isfile(src+'/'+file):
                if file not in files_replica:
                    # copy file from source to replica
                    updated_items += 1
                    log(f'{file} is copied',LOG)
                    shutil.copy2(src+'/'+file, repl)
        print(f'[{cur_time}] sync: {synchronized_items}; update: {updated_items}; delete: {deleted_items};')
    
    except FileNotFoundError as fe:
        files = os.listdir(src)
        files_replica = os.listdir(repl)
        for file in files:
            if os.path.isdir(src+'/'+file):
                log(f'{file} is copied',LOG)
                os.makedirs(repl+'/'+file)
                copy_folder(src+'/'+file,repl+'/'+file)

# function for creating a copy of a folder
def copy_folder(src, repl):

    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        repl_item = os.path.join(repl, item)

        if os.path.isfile(src_item):
            shutil.copy2(src_item, repl_item)
        elif os.path.isdir(src_item):
            if not os.path.exists(repl_item):
                os.makedirs(repl_item)
            copy_folder(src_item, repl_item)