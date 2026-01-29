n = int(input())
i = 2
is_prime = True

while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

print(is_prime)
