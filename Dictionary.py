contact={'FirstName': 'Md Samiul', 'LastName': 'Islam'}
print(contact['FirstName'])
print(contact.get('FirstName'))
print(contact.get('Phone', 'Unknown'))
print(contact.get('Phone', None))

print(contact.keys())
print(type(contact.keys()))

print(contact.values())

contact['phone']='01758466351'

print(contact)