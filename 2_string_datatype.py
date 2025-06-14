"""
What We learn Today

basic:
1.What is String?
>> String is a Sequence Of Characters enclosed within quotes

what i cover?
single coute,double coute,multiline string,f string
Unicode Characters
String Functions
String Methods
String Concatination
Row String
Escape Characters
ASCII Values
String Slicing In Python
"""

from ctypes import pythonapi
""" A String can containts:
Lettters, numbers, special symbols, Whitespace Characters ,Unicode Characters  """


""" unicode Characters """
print("\u0061")# u - combination of 4 digits
print("\U0001F600")# U - combination of 8 digits

language = "Python" # define a variable
""" python stored strings in memory sequantially along with indexes
 p    y     t     h     o     n
[0]  [1]   [2]   [3]   [4]   [5]
"""
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
# print(language[6]) #error :  index out of bound

print(" 1  + 2 + 3 + 4 ") # will print as it is because of sorunded with " "

name1 = "python"
name2 = "python"
print(name1 == name2)
print("\n")

""" multiline string """
line = ''' dhdfghdfghfdhffdghsg
fsgdgsds
       dhdfhhfghfdghdf '''
print(line)

"""Escape Sequence"""
print("C:\\Users\\Pawan Das\\Desktop")

"""String Concatination"""
a = "1"
b = "2"
print(b+a)

first_name = "Subham"
lastname = "Sharma"
print(first_name + "-" + lastname)

"""
age = 32
massage = "My age is :" + age                                # cannot concatinate string with int
print(massage)
"""

age = 32
massage = "My age is :" + str(age)  # convert int to string and then perform concatinate.so now concatinating string with string
print(massage)


""" f-string """
city = "New York"
temp = 75
weather_report = "The Temprature in " + city + " is " +  str(temp)
print(weather_report)
weather_report = f"The Temprature in {city} is {str(temp)}"
print(weather_report)

name = "Tufan Das"
print(f"first Character of {name} is {name[0]}")

# This is a curly brace : {
print(f"This is a curly brace : {{") # valid

a = "pyton"
res = a*3
print(res)  #pyhtonpyhtonpyhton     -- will print
print(res*0)
print(a*1)
print(a*-3)
""" pattern printing using string concatination """
star = "*"
print((star * 5 +"\n") * 5)
print("py"*2 + "thon"*2 )


""" len() function """
strlen = len(a)
print(strlen)

msg = "Hello!"
print(len(msg) == 6)
print("df")


print("apple" == "apple")
print("apple" == "Apple")
print("apple" == "orange")
print("apple" != "orange")
print(1 < 2)
print(11 > 2)
print(18 >= 2)
print(18 >= 2)


# check lexicographically
print("a" < "b")
print("apple" <= "apple")
print("apple" < "banana")
print("apple" < "ape")
print(ord("a"))
print(ord("A"))
print(chr(97))

""" String Indexing and slicing """
txt = "python"
# print(txt[len(txt)]) # string index out of range
print(txt[len(txt)-1])
print(txt[-1])

# slicing or substring
txt = "Python Programming"
slice = txt[:6]
print(slice)
print(txt[7:18])
print(txt[7:])
print(txt[:])

# pro
print(txt[-11:-8])

#Pto
print(txt[0:5:2])

# a negitive steps travarse the string in reverse direction
print(txt[::-2])#gimroPnhy

# reverse a string
print(txt[::-1])

""" String methods """
print(txt.upper())
print(txt.lower())

txt = "hello python programming"
print(txt.title())
print(txt.capitalize())
print()

txt = "         hello python programming          "
print(txt.strip())
print(txt.rstrip())
print(txt.lstrip())

# string.find(substring,start,end)
txt = "Python is amazing Python, is fun"
idx1  = txt.find("Python")
idx2  = txt.find("fun")
idx3  = txt.find("is",18)
print(idx1)
print(idx2)
print(idx3)

# count = string.count(substring,start,end)
count1 = txt.count("Python")
print(count1)
print("--------------")

# replace
txt = "hello world"
replace_txt = txt.replace("world","City")
print(replace_txt)
txt = "banana banana banana"
print(txt.replace("banana","apple"))#raplace all
print(txt.replace("banana","apple",1))#raplace 1
print(txt.replace("banana","apple",2))#raplace 3

# isalpha() -  check a string is purely alphabetically or not(containts numbers)
txt1 = "Python"
txt2 = "Pytho3"
print(txt1.isalpha()) # purely alphabetic string
print(txt2.isalpha()) # purely not alphabetic string,containts numbesr

# isdigit() -  check a string is containg pure digits or not (containts alphabets)
txt1 = "1234"
txt2 = "1234p"
print(txt1.isdigit())
print(txt2.isdigit())

# isalnum() -  check a string is alphanumeric(containts alphabets or numbers)
txt1 = "1234asdgs"
txt2 = "1234"
txt3 = "sfdgfdgp3"
txt4 = "1234"
txt5 = " "

print(txt1.isalnum())
print(txt2.isalnum())
print(txt3.isalnum())
print(txt4.isalnum())

# islower(),isupper(),isspace(),startwith("str",3,6),endwith("str",3,6),split()
print(txt5.isspace()) # check a string is containg only spaces

#split()
abcd = "banana,mango,apple,nuts"
li = abcd.split(",")
print(li)
ss =  " | ".join(li)
print(ss)

"""-----------------------------------> Praicice string questions <----------------------------------------------"""
"""
Q1.String method chaining
# strip, capitalized the first letter  of each word and replace skill to experts
"""
q1_str = "   python programming skills   "
print(q1_str.strip().title().replace("Skills","experts"))

"""
Q2.Advanced Slicing challange.
- print every second character using slice
- print the string in reverse order using slice
- extract and print  just "Programming" using negetive indexes
"""
s = "Python Programming Language"
print(f"printing every second character of the string 'Python Programming Language' using slice :{s[::2]}")
print(f"printing the string 'Python Programming Language' in  reverse order using slice :{s[::-1]}")
print(f"extract the part 'Programming' and printing using negetive indexes :{s[-20:-9]}")

""" Q3.create a new string by extracting the first letter from each word and concatinate them """
text  = "Python is easy to learn"
print(text[0] + text[7] + text[10] + text[15] + text[18])

""" Q3.String palindrom check
 malayalam,
 madam
 """

word = "madam"
print(word == word[::-1]) # True -- so simple as compare to java


""" Q5.Find the count occurence of "i","s","p" and "m" in string "misisipi"
"""
text_abcd = "misisipi"
count_i = text_abcd.count("i")
count_s = text_abcd.count("s")
count_p = text_abcd.count("p")
count_m = text_abcd.count("m")
print(count_i)
print(count_s)
print(count_p)
print(count_m)

# ______________________________     DONE      ____________________________________

