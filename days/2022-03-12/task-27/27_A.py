with open("./27_A.txt") as f:
    lines = f.readlines()

n = int(lines[0])
nums = list(map(int, lines[1:n+1]))

max_sum, min_len = 0, len(nums)
for a in range(n):
    for b in range(a+1, n+1):
        sm = sum(nums[a:b])
        if sm%43 == 0:
            if sm > max_sum:
                max_sum = sm
                min_len = b-a
            if sm == max_sum:
                min_len = min(min_len, b-a)
            
print(min_len)
