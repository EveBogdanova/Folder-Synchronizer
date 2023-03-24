import os
import hashlib

def compare_files_with_hash(file1, file2):
    with open(file1, 'rb') as f1:
        with open(file2, 'rb') as f2:
            if hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest():
                return True
            else:
                return False

def compare_folders_with_hash(source, replica):
    """
    compare source and replica folders
    return True if list of source folder files is identical to list of replica folder files 
    return False if lists are different
    """
    files = os.listdir(source)
    files_replica = os.listdir(replica)
    if len(files) != len(files_replica):
        return False
    for file in files:
        if os.path.isfile(source+'/'+file):
            if file in files_replica:
                if not compare_files_with_hash(source+'/'+file, replica+'/'+file):
                    return False
            else:
                return False
        if os.path.isdir(source+'/'+file):
            if not compare_folders_with_hash(source+'/'+file, replica+'/'+file):
                return False
    return True
