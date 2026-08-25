list_1 = ["Python", "Javascript", "C++"]
list_2 = ["Solidity", "Python", "C++", "HTML"]

list_1_set = set(list_1)
list_2_set = set(list_2)

print(list_1_set.union(list_2_set))
print(list_1_set.intersection(list_2_set))
print(list_1_set.difference(list_2_set))