# Good morning! Write a function called commonElements that has parameters for two arrays.  Return an array of all items that are present in both arrays.  Do not modify the arrays that are passed in.

#  Input Example:  

# [1, 2, 3, 4] [3, 4, 5, 6]
# ['a', 'b', 'c'] ['x', 'y', 'z', 'a']
# [1, 2, 3] [4, 5, 6]

# Output Example:  

# [3, 4]
# ['a']
# []

def common(l1, l2):
    l3 = []
    for e in l1:
        if e in l2:
            l3.append(e)
    return l3

print(common([1,2,3],[3,4,5]))