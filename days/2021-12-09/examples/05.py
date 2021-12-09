from random import randint

file = open('data.txt', 'r')
lines = file.readlines()
nums = list(map(int, lines))
file.close()


file = open('data_out.txt', 'w')
nums = list(map(lambda x: -x, nums))
nums = sorted(nums, reverse=True)
lines = list(map(str, nums))
for line in lines:
    file.write(line+'\n')
file.close()