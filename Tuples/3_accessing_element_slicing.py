"""
accessing elements
slicing
negetive index
nested accessing
"""

# accessing elements
fruites = ("apple", "banana", "cherry", "dates", "elderberry")
print(fruites[0])# apple
print(fruites[-1]) # elderberry

""" slicing - [start:end:steps] """
print(fruites[:4:2]) # ('apple', 'cherry')

""" reversee print  the tuple """
print(fruites[::-1])

""" accessing element of a  nested tuple """
nestes_tuple = ((1,2),(3,4),(5,6),(7,8))
print(nestes_tuple[0]) # (1, 2)
print(nestes_tuple[1]) # (3, 4)
print(nestes_tuple[2]) # (5, 6)

print(nestes_tuple[0][0]) # 1
print(nestes_tuple[0][1]) # 2
print(nestes_tuple[1][0]) # 3
print(nestes_tuple[1][1]) # 4
print(nestes_tuple[2][0]) # 5
print(nestes_tuple[2][1]) # 6