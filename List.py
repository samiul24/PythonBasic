planets = ["Mercury", "Venus1", "Earth", "Mars", "Jupiter","Venus", "Saturn", "Uranus", "Neptune"]
SearchingValue='Venus1'

try:
    FindLocation=planets.index('Venus')
    print(FindLocation)
except:
    print('Value does not exist')

Count=planets.count("Venus")
print(Count)

def search(list, SearchingValue):
    print(list)
    for i in range(len(planets)):
        print(list[i])
        if list[i]==SearchingValue:
            return list.index(list[i])
    return -1
            

print(search(planets, SearchingValue))