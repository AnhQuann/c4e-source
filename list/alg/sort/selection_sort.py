s = input('Enter a sequence: ')
words = s.split(' ')
nums = [int(word) for word in words]

for i in range(0, len(nums) - 1):
    min_index = i
    for j in range(i + 1, len(nums)):
        if nums[min_index] > nums[j]:
            min_index = j
    if min_index != i:
        nums[i], nums[min_index] = nums[min_index], nums[i]

print(*nums, sep=", ")
