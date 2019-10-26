"""
This includes functions necessary to find duplicate files.
"""
__author__ = "David Taschjian"

import hashlib
import os
import datetime
import json
import csv


def hash_file(filename, hashtype):
   """
    This function returns a defined hash of a file
    
    :param filename: full path to file
    :type filename: string
    :param hashtype: The hashing function which should be used. It has to be defined in hashlib
    :type hashtype: String
    :return type: String representation of a hex number

   """
   # make a hash object.
   h = eval('hashlib.{}()'.format(hashtype))
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()

def discover_dir(rootdir, recursive = False):
    """
    Gethering paths for all files in a directory and sub-direcotries if required.
    Counts how many children a directory has and what its total size is.
    It can recursively traverse sub-directories as well.
    Size is in Bytes.

    :param rootdir: Path to directory which size should be determined
    :type rootdir: string
    :param recursive: True if size of subdirectories should be included as well.
    :type recursive: Boolean
    :return type: tripel of two integer and a list of strings
    """
    file_count = 0
    total_size = 0
    paths = []

    if recursive:
        #consider all files in directory and its sub-directories
        for root, dirs, files in os.walk(rootdir):
            for f in files:
                file_path = os.path.join(root,f)
                #skip symlinks
                if not os.path.islink(file_path):
                    file_count +=1
                    total_size += os.path.getsize(file_path)
                    paths.append(file_path)
    else:
        #Do not include sub-directories
        for f in os.listdir(rootdir):
            file_path = os.path.join(rootdir,f)
            #skip subdirectories
            if os.path.isfile(file_path):
                file_count +=1
                total_size += os.path.getsize(file_path)
                paths.append(file_path)

    return file_count, total_size, paths


def available_file(file_path):
    """
    Check if the file in interest already exists and suggeset a new name if so.

    :param file_path: filename of interest
    :type file_path: string
    :return type:  string
    """
    
    #return given path to file if there exists no such file in the directory
    if not os.path.exists(file_path):
        return file_path
    
    #check the same filename with the current date
    now = datetime.datetime.now()
    file_path = file_path[:file_path.rfind('.')] + now.strftime("_%Y-%m-%d_%H:%M") + file_path[file_path.rfind('.'): ] 
    #check if file with current time is available 
    if not os.path.exists(file_path):
       return file_path
    
    #Append a new to the file path until we have a filename which is available
    while True:
        file_path = file_path[:file_path.rfind('.')] + '_new' + file_path[file_path.rfind('.'): ]
        #check if output file already exists
        if not os.path.exists(file_path):
            return file_path
    
def save_dict(file_path, dictonary):
    """
    Saving dictonary as txt, json or csv file

    :param file_path: Path to file
    :type file_path: string
    :param dictonary: dictonary which should be saved
    :type dictonary: dict
    :return type: None
    """
    if file_path.endswith('.txt'):
        with open(file_path, 'w', encoding = 'utf-8') as f:
            f.write(str(dictonary))
    elif file_path.endswith('.json'):
    #dumping json file
        with open(file_path, 'w', encoding = 'utf-8') as f:
            json.dump(dictonary, f, ensure_ascii=False, indent=4)
    elif file_path.endswith('.csv'):
    #dumping csv file
        with csv.writer(open(file_path, 'w', encoding = 'utf-8')) as w:
            for fileHash, paths in dictonary.items():
                w.write([fileHash] + [p for p in paths])
    else:
        raise Exception('File type not supported')