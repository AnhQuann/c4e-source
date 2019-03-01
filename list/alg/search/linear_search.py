nums = [12, 3, 4, 5, -1, 2, 30, 90, 86]
x = int(input("Enter a number: "))
found_index = -1

for index, num in enumerate(nums):
    if num == x:
        found_index = index

if found_index == -1:
    print("Not found")
else:
    print("Found {0} at index {1}".format(x, found_index))
