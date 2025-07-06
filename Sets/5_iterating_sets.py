set_a = {1, 2, 3, 4, 5}
for ele in set_a:
    print(ele)


print()
print()
print()
""" print even sets """
for x in set_a:
    if x % 2 == 0:
        print(x)

""" frozen sets """
# Frozen set frozene are immutable version of sets

regular_sets = {1,2,3,4}
frozen_set = frozenset(regular_sets)
print("Regular sets : ", regular_sets)
print("Frozen set : ", frozen_set)

""" cannot implement any tupe of modification methods on frozen sets """


#-------------------------------------------
""" Difference between set and frozen set
------------------------------------------- 
| Feature                         | `set` | `frozenset`      |
| ------------------------------- | ----- | ---------------- |
| Mutable                         | ✅ Yes | ❌ No (Immutable) |
| Hashable                        | ❌ No  | ✅ Yes            |
| Can be a dict key               | ❌ No  | ✅ Yes            |
| Supports `.add()` / `.remove()` | ✅ Yes | ❌ No             |

"""