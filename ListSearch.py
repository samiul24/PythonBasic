def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False


streaming = ['netflix', 'hulu', 'disney+', 'appletv+']
platform = 'netflix'

if search(streaming, platform):
    print("Platform is found")
else:
    print("Platform does not found")