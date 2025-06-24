fruites = ["apple", "banana", "mango", "pinaple"]
print(fruites[-2]) # negetive index means from the last element

""" list slicing """
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5]) # ending index is excluding
print(numbers[1:11:2]) # start from 1 and pickup every second element upto index 11-1 = 10
print(numbers[::2]) # start from 0 and pickup every second element upto end of the list
print(numbers[:8:3]) # start from 0 and pickup every third element upto 8-1 = 7 index
print(numbers[3:80:2]) # no error 

# get the last element
print("The last Element is : ",numbers[len(numbers)-1])

# revderse the list
print(numbers[::-1])
print(numbers[(len(numbers)-1)-2::])
print(numbers[-3:])