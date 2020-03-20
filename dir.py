# from __future__ import print_function
import os,sys
 
path = '/home/albus/Downloads/'
 
if len(sys.argv) == 2:
    path = sys.argv[1]
 
 
files = os.listdir(path)    
for name in files:
    # print(name)

    full_path = os.path.join(path, name)
    print(full_path)

    # inode = os.stat(full_path)
    # print('  ' + str(inode.st_size))
    # print('  ' + str(inode.st_mode))

    if os.path.isdir(full_path):
        print('    dir')
    elif os.path.isfile(full_path):
        print('    file')
    print('    ' + str(os.path.getsize(full_path)))