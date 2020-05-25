# List operations and manipulations


# Reverse a list
aList = [100, 200, 300, 400, 500]
print(aList[::-1])

# Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

# Turn every item of a list into its square
squareList = [i * i for i in aList]
print(squareList)

# Concatenate two lists in the following order
# Expected output - ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [i + j for i in list1 for j in list2]
print(list3)

# Iterate both lists simultaneously
# such that list1 should display item in original order and list2 in reverse order.
list1 = [1, 2, 3, 4, 5]
list2 = [100, 200, 300, 400, 500]
for x, y in zip(list1, list2[::-1]):
    print(x, y)
