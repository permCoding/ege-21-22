# найти все простые числа от 2 до n, используя функцию
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = 100
print([number for number in range(2, n+1) if is_prime(number)])
