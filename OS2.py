import os
from os.path import abspath, join, getsize

# producing absolute paths, instead of a tuple of three items
for top_dir, directories, files in os.walk('.'):
    print(top_dir)

    for directory in directories:
        print('Path: ' + abspath(join(top_dir, directory)) + ', Size: ' +  str(getsize(abspath(join(top_dir, directory)))))
        
    for _file in files:
        print('Path: ' + abspath(join(top_dir, _file)) + ', Size: ' +  str(getsize(abspath(join(top_dir, _file)))))
    break