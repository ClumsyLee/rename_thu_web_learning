# -*- coding: UTF-8 -*-

# rename_files_from_learn.tsinghua.py

import os, sys

def isDate(string):
    """len(string) == 8"""
    if len(string) != 8 or not string.isdigit():
        return False
    year = int(string[:4])
    month = int(string[4:6])
    day = int(string[6:])
    if year >= 2000 and year <= 3000 and month > 0 and month < 13 and day > 0 and day < 32:
        return True
    return False

def delTrash(filename):
    """delete trailing trash numbers in filename"""
    hyphen = filename.rfind('_')
    period = filename.rfind('.')
    if hyphen > 0 and period > 0 and hyphen < period:
        trash = filename[hyphen+1:period]
        if trash.isdigit() and len(trash) >= 8 and not isDate(trash):
            new_filename = filename[:hyphen]+filename[period:]
            os.rename(filename, new_filename)
            return new_filename
    return None

if __name__ == '__main__':
    working_dir = sys.argv[1]
    count = 0
    new_files = []
    for root, dirs, files in os.walk(working_dir):
        for name in files:
            count += 1
            new_filename = delTrash(os.path.join(root, name))
            if new_filename != None:
                new_files.append(new_filename)
    print
    print 'List of changed files:'
    for name in new_files:
        print name
    print 'Total: ', len(new_files), '/', count, 'files changed.'
