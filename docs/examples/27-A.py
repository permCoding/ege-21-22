# https://inf-ege.sdamgia.ru/problem?id=41002  86097
""" Дана последовательность целых чисел. 
Необходимо найти максимально возможную сумму 
её непрерывной подпоследовательности, в которой 
количество положительных нечётных элементов кратно k=30."""


with open("./27-A.txt") as f:
    nums = list(map(int, f.readlines()))
n = nums[0]
nums = nums[1:n+1]
max_sm = -999999999
for i in range(n-1):
    for j in range(i+1, n):
        cnt = len(list(filter(lambda x: (x%2==1 and x>0), nums[i:j])))
        if cnt%30==0:
            sm = sum(nums[i:j])
            max_sm = max(max_sm, sm)
print(max_sm)
