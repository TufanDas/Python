person = {
    'name' : "Tufan das",
    'age':23
}

# modifying the name id exists
person['name'] = "Rajat Sutradhar"
print(person['name'])

# create a new key value pair for person if not exists
person['city'] = "madarihat"
print(person['city'])

""" deleting a key from the dictionery  """
del person['name'] # deleting the key value from the dictionery
print(person)

""" deleting and also returning the value of the deletd element of the dictionery"""
print(person.pop('age'))
print(person)

""" clearing all the element of the dictionery and dictionery remains empty dictionery"""
person.clear()
print(person) # {}

person = {
    'name' : "Tufan das",
    'age':23
}
""" popitem() method delete the last insert key value pair and also return the deleted key value pair as tuple """
print(person.popitem()) # ('age', 23)


''' updating dictionery using update() method
syntax : dict1.update(dict2)
# dict1: The dictioney to be updated
# dict2: The dictionery (or key value iterable) provoding updated
'''
profile = {"name":"agasgsg","age":23, "city":"sbdsghsdhg"}
updates = {"name" : "Tufan Das", "city" : "madarihat"}
profile.update(updates)
print(profile)


