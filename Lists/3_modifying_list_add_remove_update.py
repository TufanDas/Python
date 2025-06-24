fruites = ["apple", "banana", "cherry"]

fruites[1] = "bluebery"
print(fruites) #['apple', 'bluebery', 'cherry']

fruites[1:2] = ["watermelon","cucumber","carrot"] # ending index is excluded
print(fruites) # ['apple', 'watermelon', 'cucumber', 'carrot', 'cherry']

fruites.append("mango")
print(fruites) # ['apple', 'bluebery', 'cherry', 'mango']

fruites.insert(3,"banana")
print(fruites)#['apple', 'bluebery', 'cherry', 'banana', 'mango']

fruites2 = ["pinaple","kiwi"]
fruites.extend(fruites2)
print(fruites)#['apple', 'bluebery', 'cherry', 'banana', 'mango', 'pinaple', 'kiwi']

fruites.append("banana")
print(fruites)# ['apple', 'bluebery', 'cherry', 'banana', 'mango', 'pinaple', 'kiwi', 'banana']

print(fruites.remove("banana")) # returning None -> nothing
print(fruites)#['apple', 'bluebery', 'cherry', 'mango', 'pinaple', 'kiwi', 'banana']

print(fruites.pop())   # default -1  # banana
print(fruites.pop(-2)) # pinaple
print(fruites.pop(-3)) # cherry
print(fruites) #['apple', 'bluebery', 'mango', 'kiwi']

del fruites[2]
print(fruites)#['apple', 'bluebery', 'kiwi']

fruites.extend(["cherry", "banana", "mango", "pinaple", "banana"])
print(fruites) #['apple', 'bluebery', 'kiwi', 'cherry', 'banana', 'mango', 'pinaple', 'banana']

del fruites[2:5] # 5 is excluded
print(fruites)# ['apple', 'bluebery', 'mango', 'pinaple', 'banana']

fruites.clear()
print(fruites)