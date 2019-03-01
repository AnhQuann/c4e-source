n = int(input("Enter a number:"))

result = 0
for i in range(1, n + 1):
    result +=  1 / i
print("1/1 + 1/2 + ... + 1/n = ")
print(result)
