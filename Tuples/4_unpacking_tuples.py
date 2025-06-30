"""
tuple unpacking, allows you to assigning tuple elements to individual variable into a single operation.
python does this by matching the structure (number of item) on both side of the assignment operator
any iterable(list,String, set) object can be unpacked
"""

# a, b, c = 1, 2, 3,4  #ValueError: too many values to unpack (expected 3)
a, b, c = 1,2,3 # here tuple(1,2,3) is unpacking and assigning to individual variable
print(a)
print(b)
print(c)

q, *w, e, r = 1,2,3,4,5,6,7,8,9,0
print(q)
print(w) # 2,3,4,5,6,7,8 assigning to the variable w in list format
print(e)
print(r)
9
0






data = ("jhon", 30, "Manager", 5000, "New York")
name, age, designation, salary, city = data
print(name) #  jhon
print(age)#    30
print(designation)#   Manager
print(salary)#    5000
print(city)#    New York

""" unpacking nested tuple """
a, b, c, (d,f) = ((1,2),(3,4),(5,6),(7,8))
print(a) # (1,2)
print(b) # (3,4)
print(d) # 7
print(f) # 8

