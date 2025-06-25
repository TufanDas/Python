fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
for fruite in fruits:
    print(fruite)

print()

for i in range(len(fruits)):
    print(fruits[i])

""" count the apple """
count = 0
for i in range(len(fruits)):
    if fruits[i] == "apple":
        count += 1
print("Count of apple is : ",count)

""" reverse list """
reversed_fruites = []
for i in range(len(fruits)-1,-1,-1): # make sure for reversing you add -1 at the position of steps
    reversed_fruites.append(fruits[i])
print(reversed_fruites)

""" find minimum """
min = float('inf')
max = float('-inf')
nums = [1, 2, 3, 4, 600,5, 6, 7, 8, 9, 10]
for i in range(len(nums)):
    if nums[i] < min:
        min = nums[i]
    if nums[i] > max:
        max = nums[i]
print("The minimum value in the list is : ",min)
print("The maximum value in the list is : ",max)
