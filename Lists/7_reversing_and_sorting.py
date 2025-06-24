nums = [1, 2, 3, 4, 5]
nums.reverse() # reverse by reference | reverse in place
print(nums) # [5, 4, 3, 2, 1]

print(reversed(nums)) # returning a new list

words = ["banana","mango","chery","apple"]
words.sort() # sort by reference
print(words) # ['apple', 'banana', 'chery', 'mango']
words.sort(reverse=True)
print(words)# ['mango', 'chery', 'banana', 'apple']

words.sort(key= len, reverse=True)
print(words)# ['banana', 'mango', 'chery', 'apple']

sorted_words1 = sorted(words) # returning a new list
print(sorted_words1) # ['apple', 'banana', 'chery', 'mango']
sorted_words2 = sorted(words, key=len, reverse=True) # returning a new list
print(sorted_words2) # ['banana', 'mango', 'chery', 'apple']


nums = [-10, 5, -3, 2, -1]
nums.sort(key=abs) # [-1, 2, -3, 5, -10]
print(nums)

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(fruits.count("apple")) # 3
print(fruits[:3].count("apple")) # 2
print(fruits.index("banana", 2)) # 4
print(fruits.index("banana", -3)) # 4
