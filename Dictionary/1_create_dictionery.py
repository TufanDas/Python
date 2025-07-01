"""The most common way to create a dictionery is using curly brackets {} with key value pairs seperated by commas"""

"""creating dictionery"""
student = {
    "name":"Alice",
    "age" : 23,
    "grade" : "A"
}
""" standered way to create a dictionery """
fruite_colors = {
    "mango" : "yellow",
    "apple" : "red",
    "watermelon" : "green",
}

""" creating dictionery using dictionery constructor  """
""" The dict() constructor accepts keyword arguments. """
my_dictionery = dict(apple = "red",banana = "yellow", brown = "kiwi", green = "watermelon")
print(my_dictionery)

""" creating dictionery from  list of tuple """
d = dict([("apple","red"),("banana","yellow"),("kiwi","brown")])
print(d["apple"]) # red

""" integers as key of the dictionery """
my_dict_int_key = {1 : "one", 200 : "two hundred", 0 : "zero"}

""" float as key of the dictionery """
my_dict_float_key = {
    1.99: "Apple",
    0.99: "Banana",
    2.49: "Mango"
}
print(my_dict_float_key[1.99])  # Output: Apple

""" boolean as key """
my_dict_bool_key = {True: "This is a true value", False:"This is a false value"}

""" tuple as key of the dictionery """
my_dict_tuple_key = {
    (23,54):"twenty three | fifty four",
    (73,99): "seventy three | ninty nine"
}
print(my_dict_tuple_key[(23,54)])

""" mix of different key types in a dictionary """
my_dict_mixed_key = {
    1:"one",
    "two":2,
    (3,4):"tuple as key"
}



