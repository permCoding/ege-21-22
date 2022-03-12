with open("./27884.txt") as f:  # 26
    lines = f.readlines()

s, n = map(int, lines[0].split())
nums = sorted(map(int, lines[1:]))

sm = 0
for pos in range(0, n):
    if sm + nums[pos] <= s:
        sm += nums[pos]
    else:
        break

print(pos)
check = s - sm + nums[pos-1]

for end in range(n-1, pos-1, -1):
    if nums[end] <= check:
        print(nums[end])
        break
