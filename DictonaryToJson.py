import json

# the JSON module can take certain Python data structures like dictionaries and convert them to JSON
import json
data = {"grape": "Cabernet Franc", "species": "Vitis vinifera", "origin": "Bordeaux, France"}
print(type(data))
print(data)

# Convert Python data to JSON. The `.dumps()` method takes a data structure as input and provides a JSON string as output
print(type(json.dumps(data)))
print(json.dumps(data))

# Convert a JSON string into a Python data structure
# first, define the json data with the string data
# Now load it into Python
json_data = json.dumps(data)
print(type(json.loads(json_data)))


# define a nested data structure in a single line
grape_data = {"name": "Cabernet France", "regions": [{"country": "France", "sub-regions": ["Bordeaux", "Loire Valley"]},{"country": "Italy", "sub-regions": ["Apulia", "Tuscany"]}, {"country": "Argentina", "sub-regions": ["Mendoza", "Lujan de Cuyo", "Salta"]}]} 
# Serialize the Python dictionary to a JSON string, but using extra formatting options, like sorted keys
# and using 4 spaces for indentation
data_as_json = json.dumps(grape_data, sort_keys=True, indent=4)
print(data_as_json)
