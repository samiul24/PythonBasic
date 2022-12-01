import os

MainRoot = 'E:\Data 365 Course\Python Boot Camp'
FileFolderDic = {'File':[], 'Folder':[]}

for FileFolder in os.listdir(MainRoot):
    FileFolder = os.path.join(MainRoot,FileFolder)
    if os.path.isdir(FileFolder):
        FileFolderDic['File'].append(FileFolder)
    else:
        FileFolderDic['Folder'].append(FileFolder)
print(FileFolderDic)