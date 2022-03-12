""" 
Дана последовательность целых чисел. 
Необходимо найти максимально возможную сумму 
её непрерывной подпоследовательности. 
"""

line = "2 -3 5 -3 2 4 -8"

nums = list(map(int, line.split()))
n = len(nums)

# сложность решения = n
max_sum, sm = -2*10**9, 0
for i in range(n):
    sm = max(nums[i], sm + nums[i])
    max_sum = max(max_sum, sm)

print(max_sum)
