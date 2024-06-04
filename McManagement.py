import datetime
import logging
import sys
import argparse
import os
import subprocess
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-s", "--silent", help="Do not write any logs and execute all tasks in the background.",
                    action="store_true")
parser.add_argument("FolderPath", help="The path to where existing MC files can be found or where new files should be put. Ex. /var/lib/mc")
args = parser.parse_args()
FolderPath = args.FolderPath
MCPath = str(FolderPath) + "/"
print(MCPath)
if args.verbose and args.silent:
    print('FATAL: Both Verbose and Silent modes are on. Ending program. Please run with at most one of these variables.')
    quit()
if args.silent:
    pass
else:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)
    file_handler = logging.FileHandler("log.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
starttime = datetime.datetime.now()
if args.silent:
    McExists = os.path.isdir(args.FolderPath)
    if McExists == False:
        #print("Creating a directery for MC")
        subprocess.run(["mkdir", FolderPath])
    elif McExists == True:
        exit()
    else:
        exit()
else:
    logger.info(starttime)
if args.silent:
    pass
else:
    logger.info('Checking for Existing Server files...')