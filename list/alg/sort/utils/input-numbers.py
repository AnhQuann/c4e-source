s = input("Enter a sequence of number, separated by space:")
words = s.strip().split(' ')

nums = []
for word in words:
    nums.append(int(word))

print(nums)
