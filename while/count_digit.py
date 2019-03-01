n = int(input("Enter a number:"))

digit_count = 0
while n > 0:
    n = n // 10
    digit_count += 1
print(digit_count)
