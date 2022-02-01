nums = list(map(int, open("17.txt").readlines()))

max_num = max([num for num in nums if num % 3 == 0])

count, max_sum = 0, -20000
for i in range(len(nums)-1):
    a, b = nums[i], nums[i+1]
    if (a % 3 == 0 or b % 3 == 0) and (a + b <= max_num):
        count += 1
        max_sum = max(a + b, max_sum) 

print(count, max_sum)
