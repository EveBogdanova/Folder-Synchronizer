import os, time

# function for checking if source folder exist
# returns path to the source folder
def input_source(LOG):
    loop = True
    while loop:
        source = input('Enter path to the source folder: ')
        if not os.path.exists(source):
            log('source folder: NOT FOUND',LOG)
            print(f"Error: Source folder '{source}' does not exist.")    
        else:
            log('source folder: ONLINE',LOG)
            print(f"Source folder: '{source}'")  
            loop = False
    return source

    
# function for checking if replica folder exist (if not - creates replica folder)
# returns path to the replica folder
def input_replica(LOG):
    loop = True
    while loop:
        replica = input('Enter path to the replica folder: ')
        if not os.path.exists(replica):  
            log('replica folder: NOT FOUND',LOG)
            choice = input("The directory is not exist. Enter 1 to create this directory: ")
            if choice == '1':
                os.makedirs(replica)
                log('replica folder: ONLINE',LOG)
                print(f"Created replica folder: '{replica}'")
                loop = False
        else:
            log('replica folder: ONLINE',LOG)
            print(f"Replica folder: '{replica}'")
            loop = False
    return replica  


# function for entering path to the log file
def path_to_log_file():

    LOG = 'log.txt'
    loop = True
    while loop:
        path = input('Enter path to the directory to create the log file: ')
        if not os.path.isdir(path):    
            choice = input("The directory is not exist. Enter 1 to create this directory: ")
            if choice == '1':
                os.makedirs(path)
                print(f"The directory '{path}' is created!")
                loop = False
        else:
            loop = False
    LOG = path + '/'+ LOG
    print("Log file location: " + LOG)
    log('Program execution started',LOG)
    return LOG
    


# function for writing logs to the log file
def log(message, LOG):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(LOG, 'a') as file:
        file.write('['+current_time+']'+message+'\n')


# function for getting synchronization interval
# returns int - time interval in seconds
def get_interval():
    loop = 0
    while (loop==0):
        try:
            res = int(input('Enter synchronization interval (in minutes): '))
            if (res<=0):
                print('You should enter a positive number')
            else:
                print(f'Entered synchronization interval is {res} minutes or {res*60} seconds')
                loop += 1
        except ValueError as ve:
            print('You should enter a positive number')
        return res*60
