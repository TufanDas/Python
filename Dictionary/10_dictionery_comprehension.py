res = {i:i**2 for i in range(1,11)}
print(res)


res2 = {i : i**2 if i%2 == 0 else i for i in range(1,11)}
res3 = {i : i**2 for i in range(1,11) if i%2 == 0}
print(res2)
print(res3)


students = [("mark",90),("mike",89),("michel",70)]
result = {i:j for i,j in students}
print(result)

origional = {'a':1,'b':2,'c':3}
result2 = {j:i for i,j in origional.items()}
print(result2)

res = {}
for i in range(1,6):
    inner_dict = {}
    for j in range(1,11):
        inner_dict[j] = i*j
    res[i] = inner_dict
print(res)


res = {i:{j : i*j for j in range(1,11)} for i in range(1,6)}
print(res)
# res =