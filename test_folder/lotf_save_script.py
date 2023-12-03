# it shall:
# 	1. Start on launch of exe (poll system processes every 1hr)
# 	2. copy Save00.sav & generalSave.sav to zip archive
# 	3. zip archive name set to Backup001
# 	4a. At end of session, store amount saved in ini file
# 	4b. At end of session, move all backups into seperate folder with timestamp, and delete all backups
########################################################################################################

import shutil
import os
import subprocess
from datetime import datetime, date, time
import time

# Checks if exe is active
def check_launch_status(e_name):
    if process_exists(e_name):
        return True
    else:
        return False

# Copies save game to folder
def archive_data(b_number, b_path):
    if os.path.isdir("backup" + str(b_number)):
        print("couunter " + str(b_number))
        print("1")
        print(exit)
        exit()

        return False
    else:
        os.makedirs(b_path)
        shutil.copy2("Save00.sav", b_path)
        shutil.copy2("GeneralSave.sav", b_path)
        b_number += 1
        print("couunter " + str(b_number))
        return True

# Copies all save of session to timestampe folder and deletes current folder
def archive_session(s_path):
    b_up = 0
    while os.path.isdir("backup" + str(b_up)):
        shutil.copytree(("backup" + str(b_up)), os.path.join(s_path, "backup" + str(b_up)))
        print("copied" + str(b_up))
        b_up += 1
        
#
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

# Main program
exec_name = "LOTF2-Win64-Shipping.exe"

backup_number = 0
 
while check_launch_status(exec_name):
    backup_name = "backup" + str(backup_number)
    backup_path = os.path.join(os.getcwd(), backup_name)    
    print("Begin archiving...")
    archive_data(backup_number, backup_path)
    time.sleep(5)
    backup_number += 1

session_name = "Session_" + str(datetime.now().strftime('%d_%b_%Y_%I_%M%p'))
session_path = os.path.join(os.getcwd(), session_name)    
archive_session(session_path)
print("Closing...")
exit()

    