import os
import pprint

mainRoot = 'E:\Data 365 Course\Credit Card\8'
fileDic = {}

for root, directories, files in os.walk(mainRoot):
    for file in files:
        absulatePath = os.path.join(root, file)
        fileSize = os.path.getsize(absulatePath)
        fileDic[absulatePath] = fileSize
        #print(f"File Path: {absulatePath}, Size: {fileSize} KB")
pprint.pprint(fileDic)

x = type(sorted(fileDic))
print(x)

i=0
for path, size in sorted(fileDic.items(), key = lambda arg:arg[1], reverse=False):
    if i>2:
        break
    print(f"File Path: {path}, Size: {size} KB")
    i=i+1

