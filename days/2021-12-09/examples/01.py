from random import randint

f = open('data.txt', 'w')

nums = [str(randint(1, 1000)) + '\n' for _ in range(10)]

f.writelines(nums)

f.close()
