import os

mainPath=os.listdir('E:\Data 365 Course\Credit Card')

dic={'File':[], 'Folder': []}

fullPath=[os.path.join('E:\Data 365 Course\Credit Card', fileFolder) for fileFolder in mainPath]
for i in fullPath:
    if os.path.isdir(i):
        dic['Folder'].append(i)
    elif os.path.isfile(i):
        dic['File'].append(i)

for item in dic['File']:
    print(item)

