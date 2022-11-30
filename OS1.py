import os

# yields the 'current' dir, then the directories, and then any files it finds
# for each level it traverses
for path_info in os.walk('.'):
    print(path_info)
    break