import os

fullPathSize = {}

for root, directories, files in os.walk('E:\Data 365 Course\Credit Card\8'):
    for file in files:
        absulatePath = os.path.join(root, file)
        size =  os.path.getsize(absulatePath)
        fullPathSize[absulatePath] = size

for path, size in fullPathSize.items():
    print(f"Path: {path}, Size: {size}")


#Exercise: Now that the metadata is captured and stored in a suitable data structure like a dictionary, 
#report back the results with only the four largest files. Try using other quantities to report on, 
#like the 10 largest files instead of 4.

i=0
for path, size in sorted(fullPathSize.items(), key=lambda x:x[1], reverse=True):
    if i>2:
        break
    print(f"Path: {path}, Size: {size}")
    i=i+1
