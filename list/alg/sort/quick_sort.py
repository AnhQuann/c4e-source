user_input = input("Enter a sequence of number: ")
nums = [int(word) for word in user_input.split(',')]

def partition(nums, lo, hi):
    i = lo + 1
    j = hi
    while i < j:
        while nums[i] < nums[lo]:
            i += 1
        while nums[j] > nums[lo]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[j], nums[lo] = nums[lo], nums[j]
    return j

def sort(nums, lo, hi):
    if hi <= lo:
        return
    mid = partition(nums, lo, hi)
    sort(nums, lo, mid - 1)
    sort(nums, mid + 1, hi)

sort(nums, 0, len(nums) - 1)
print(nums)
