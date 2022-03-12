""" 
Дана последовательность целых чисел. 
Необходимо найти максимально возможную сумму 
её непрерывной подпоследовательности. 
"""

line = "2 -3 5 -3 2 4 -8"

nums = list(map(int, line.split()))
n = len(nums)

# сложность решения = n**3
max_sum = -2*10**9
for left in range(0, n):
    for right in range(left+1, n+1):
        sm = sum(nums[left: right])
        if sm > max_sum:
            max_sum = sm

print(max_sum)
