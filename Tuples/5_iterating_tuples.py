colors = ("red", "green", "blue")

for color in colors:
    print(color, (type(color)))

"""enamurate returns a tuple and unpack the tuple in index and color"""
for index,color in enumerate(colors,start=1):
    print(index,color)

""" unpacking tuple in list """
pairs = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]
# unpacking each tuple
for number,letter in pairs:
    print(number,letter)
