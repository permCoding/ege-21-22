'''
как задание №17
найти пару чисел идущих подряд
с минимальной разницей между ними
'''

nums = [int(line) for line in open('data.txt')]

mn = 10000
for i in range(1, len(nums)):
    mn = min(mn, abs(nums[i-1] - nums[i]))

print(mn)
