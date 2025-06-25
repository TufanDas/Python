li = [1,2,3,4,5,6,7]
res = [x*x for x in li]
print(res) # [1, 4, 9, 16, 25, 36, 49]

res = [i**2 for i in range(1,11)]
print(res) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

""" only squars of even numbers upto 1 - 10 """
res = [x**2 for x in range(1,11) if x%2==0]
print(res) # [4, 16, 36, 64, 100]

res = [x**2 if x%2==0 else x for x in range(1,11)]
print(res) # [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]


drinks = ["coffe", "tea"]
desert = ["cake", "cookies", "ice cream"]

res = [(i,j) for i in drinks for j in desert]
print(res) # [('coffe', 'cake'), ('coffe', 'cookies'), ('coffe', 'ice cream'), ('tea', 'cake'), ('tea', 'cookies'), ('tea', 'ice cream')]

text = "Python list comprehension is powerful and consice"
res = []
split_test = text.split()
for word in split_test:
    if len(word) > 5:
        res.append(word.upper())
print("Using for loop : ", res) # ['PYTHON', 'COMPREHENSION', 'POWERFUL', 'CONSICE']

res = [i.upper() for i in text.split() if len(i) > 5]
print("Using List comprehension : ",res) # ['PYTHON', 'COMPREHENSION', 'POWERFUL', 'CONSICE']