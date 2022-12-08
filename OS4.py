import os

for root, directories, files in os.walk('E:\Data 365 Course\Credit Card\8'):
    print(root)
    print(directories)
    print(files)
    for file in files:
        absulatePath = os.path.join(root, file)
        print(absulatePath)

