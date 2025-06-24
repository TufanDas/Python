"""
using list constructor
using slicing
using .copy() function
"""

# all the changes of list a will reflect to the list b
""" deep copy """
a = [1, 2, 3]
b = a
a.append(33)
a.remove(2)
a.remove(1)
print(a)
print(b)

""" all the changes of a is not reflect to the b """
""" Shallo copy """
a = [1, 2, 3, 4, 5]
b = a[:]
print("A = ", a)
a.append(99)
print("A = ",a)
print("B = ",b) # remain the same list not mpdified

"""nested list"""
a = [
        [1,2],
        [3,4],
        [5,6]
             ]
b = a[:] # copying outer list inner list is a objet of list type actually copying the adresses of inner list
print(a)
a[0][1] = 90
print(a)
print(b)