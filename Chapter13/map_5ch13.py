# # # Method 1 # # #

# def square(num):
#     return num*num

# l = [1, 2, 4, 3]
# l2 = []
# for item in l:
#     l2.append(square(item))
# print(l2)

# # # Method 2 # # #

def square(num):
    return num*num
l = [1, 2, 4, 3]
print(list(map(square, l)))
