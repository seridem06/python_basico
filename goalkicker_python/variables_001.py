a, b, c = 1, 2, 3
print(a, b, c)

a, b, _ = 1, 2, 3
print(a, b)

a = b = c = 1
print(a, b, c)
# Output: 1 1 1

a = b = c = 1 # all three names a, b and c refer to same int object with value 1
print(a, b, c)
# Output: 1 1 1
b = 2 # b now refers to another int object, one with a value of 2
print(a, b, c)
# Output: 1 2 1 # so output is as expected.

x = y = [7, 8, 9] # x and y refer to the same list object just created, [7, 8, 9]
x = [13, 8, 9] # x now refers to a different list object just created, [13, 8, 9]
print(y) # y still refers to the list it was first assigned
# Output: [7, 8, 9]

x = y = [7, 8, 9] # x and y are two different names for the same list object just created, [7,8, 9]
x[0] = 13 # we are updating the value of the list [7, 8, 9] through one of its names, xin this case
print(y) # printing the value of the list using its other name
# Output: [13, 8, 9] # hence, naturally the change is reflected

