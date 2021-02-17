def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


a = [1,2,3,4,5]
a.sort()
a.reverse()
b, c = split_list(a)
b.reverse()
b.extend(c)

print(b)



# Input [1, 2, 3, 4, 5, 6]
# Output [4, 5, 6, 3, 2, 1]
