""" union of set """
set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(f"Union Using | operator : {set_a | set_b}")      #{1, 2, 3, 4, 5, 6}
print(f"Union Using Union() operator : {set_a.union(set_b) }")      # {1, 2, 3, 4, 5, 6}

set_c = {7, 8, 9}
print(f"Union multiple set Using | operator : {set_a | set_b | set_c}")     # {1, 2, 3, 4, 5, 6, 7, 8, 9}

union_with_list = set_a.union([7, 8, 9])
print("Union with list: ", union_with_list) #       {1, 2, 3, 4, 7, 8, 9}

user1_interests = {"movies", "books", "music"}
user2_interests = {"music", "sports", "games"}
user3_interests = {"books", "cooking", "travel"}
all_interst = user1_interests | user2_interests | user3_interests
print(f"All unique interests : ",all_interst)       # {'travel', 'cooking', 'music', 'sports', 'games', 'books', 'movies'}

""" intresection of sets """
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
intersection_result = set_a & set_b
print("Intersection using & : ", intersection_result)   # {4, 5}
intersection_result = set_a.intersection(set_b)
print("Intersection using intersection() :  ",intersection_result) #    {4, 5}

set_c = {3, 4, 5, 9, 10}
intersection_multiple = set_a & set_b & set_c
print(f"Intersection of multiple sets : {intersection_multiple}")   # {4, 5}
developer1_skills = {"python", "java", "sql", "git"}
developer2_skills = {"python", "javaScript", "sql", "docker"}
developer3_skills = {"python", "sql", "mongodb", "react"}
print(f"Common skills : ", developer1_skills & developer2_skills & developer3_skills)   # {'sql', 'python'}


""" difference between sets """
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("A-B using - :",set_a - set_b) #{1, 2, 3}
print("B-A using - :",set_b - set_a) #{8, 6, 7}
print("A-B using difference() : ",set_a.difference(set_b))  #{1, 2, 3}
set_c = {2, 3, 9, 10}
diffrence_multiple_set = set_a - set_b - set_c
print("Difference of multiple sets (a - b - c) : ", diffrence_multiple_set)     # {1}

""" symetric difference """
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
sym_diff_res = set_a ^ set_b
print("Symetric difference using ^ : ", sym_diff_res)       #{1, 2, 3, 6, 7, 8}
sym_diff_res = set_a.symmetric_difference(set_b)
print("Symetric difference using symmetric_difference()  : ", sym_diff_res)###{1, 2, 3, 6, 7, 8}

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2}
print("A is subset of B : ", set_a.issubset(set_b))    #  True
print("A is subset of C : ", set_a.issubset(set_c))    # False
print("B is subset of A : ", set_b.issubset(set_a))    # False
print("B is subset of C : ", set_b.issubset(set_c))    # False
print("C is subset of A : ", set_c.issubset(set_a))    #  True
print("C is subset of B : ", set_c.issubset(set_b))    #  True
print()
print("A is superset of B : ", set_a.issuperset(set_b))    # False
print("A is superset of C : ", set_a.issuperset(set_c))    #  True
print("B is superset of A : ", set_b.issuperset(set_a))    #  True
print("B is superset of C : ", set_b.issuperset(set_c))    #  True
print("C is superset of A : ", set_c.issuperset(set_a))    # False
print("C is superset of B : ", set_c.issuperset(set_b))    # False

# <= operator
# This operator chaeks if the laft set is a subset of(or equal to) the right set
print("A <= B : ",set_a <= set_b)    #  True
print("A <= A : ",set_a <= set_a)    #  True
print("C <= A : ",set_c <= set_a)    #  True
print("C < A  : ",set_c < set_a)    #  True
print("A < A  : ",set_a < set_a)    # False

""" Disjoint sets """
set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 4, 5}
print("A and B are disjoint : ", set_a.isdisjoint(set_b))    #  True
print("A and C are disjoint : ", set_a.isdisjoint(set_c))    # False
print("B and C are disjoint : ", set_b.isdisjoint(set_c))    # False
# same as disjoint
print(len(set_a & set_b) == 0)  # True