# hash table- internely dictionery use a hash table to store things
student = {
    "name" : "Rahul",
    "age" : 21,
    "grade" : "A"
}
""" 
hash table ---> An array (called the "hash table") of fixed size.
returning the hash value of the given object suppose is the hash value 2955922551173146265
 index = 2955922551173146265 % size_of_the_hash_table = 8
 so 8 is the final result ,and 8 will be the position where the value stored
"""
index = hash("name") % 8
print(index) # 7 - th index | data stored

# here the overview of hash table storing the name of fruite as key and tha  prices as value
+--------+----------------+----------+--------+
| Index  | Hash           | Key      | Value  |
+--------+----------------+----------+--------+
|   0    | 928374         | 'apple'  |   10   |
|   1    |                |          |        |
|   2    | 182736         | 'banana' |   20   |
|   3    |                |          |        |
|   4    | 345678         | 'cherry' |   30   |
|   5    |                |          |        |
|   6    |                |          |        |
|   7    |                |          |        |
+--------+----------------+----------+--------+



