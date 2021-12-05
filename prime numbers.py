a = int(input("Enter the range of prime no. 0- "))
primes = list(filter(lambda x:
                     all(x%y != 0 for y in range(2, x)),
                     range(2, a)))
print(primes)