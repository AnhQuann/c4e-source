n = int(input("Enter a number: "))

i = 2
is_prime = True

while i * i <= n:
    if (n % i) == 0:
        is_prime = False
        break
        
    i += 1

if is_prime:
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))
