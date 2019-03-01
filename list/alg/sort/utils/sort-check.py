s = input("Enter a sequence of number: ")
words = s.strip().split(' ')

nums = []
for word in words:
    num = int(word)
    nums.append(num)

list_sorted = True
for i in range(0, len(nums) - 1):
    if nums[i] > nums[i + 1]:
        list_sorted = False
        break

if list_sorted:
    print("Your sequence is already sorted")
else:
    print("Your sequence is not sorted yet")
    
