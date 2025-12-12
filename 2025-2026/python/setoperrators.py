A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
union_set = A.union(B)
print(union_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
union_set = A.union(B)
print(union_set)
# Expected output: {1, 2, 3, 4, 5, 6, 7, 8}

A = {2, 4, 6, 8, 10}
B = {1, 2, 3, 4, 5}
intersection_set = A.intersection(B)
print(intersection_set)

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
difference_set = A.difference(B)
print(difference_set)
# Expected output: {1, 2}