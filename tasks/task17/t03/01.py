lines = open("17.txt").readlines()
nums = list(map(int, lines))
n = len(nums)
max_num = -10000
for num in nums:
    if num % 3 == 0:
        if num > max_num:
            max_num = num
count, max_sum = 0, -20000
for i in range(n-1):
    a, b = nums[i], nums[i+1]
    if a % 3 == 0 or b % 3 == 0:
        if a + b <= max_num:
            count += 1
            if a + b > max_sum:
                max_sum = a + b

print(count, max_sum)
