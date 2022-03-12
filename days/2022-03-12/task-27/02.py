""" 
Дана последовательность целых чисел. 
Необходимо найти максимально возможную сумму 
её непрерывной подпоследовательности. 
"""

line = "2 -3 5 -3 2 4 -8"

nums = list(map(int, line.split()))
n = len(nums)

# сложность решения = n**2
max_sum = -2*10**9
for left in range(0, n):
    sm = 0
    for right in range(left, n):
        sm += nums[right]
        max_sum = max(max_sum, sm)

print(max_sum)
