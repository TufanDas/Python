"""The most common way to create a dictionery is using curly brackets {} with key value pairs seperated by commas"""

"""creating dictionery"""
student = {
    "name":"Alice",
    "age" : 23,
    "grade" : "A"
}

fruite_colors = {
    "mango" : "yellow",
    "apple" : "red",
    "watermelon" : "green",
}

""" creating dictionery using dictionery constructor """
my_dictionery = dict(apple = "red",banana = "yellow", brown = "kiwi", green = "watermelon")
print(my_dictionery)

""" dictionery of list containing tuple"""
d = dict([("apple","red"),("banana","yellow"),("kiwi","brown")])
print(d["apple"]) # red


