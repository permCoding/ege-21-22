# demo
"""В файле содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от –10000 до 10000
включительно. Определите количество пар последовательности, в которых
хотя бы одно число делится на 3, а сумма элементов пары не более
максимального элемента последовательности, кратного 3. В ответе запишите
количество найденных пар, затем максимальную из сумм элементов таких
пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности."""

with open("./17.txt") as f:
    nums = list(map(int, f.readlines()))
n = len(nums)

max3 = max(filter(lambda num: num%3==0 , nums))
count, max_sm = 0, -10000*n
for i in range(n-1):
    a, b = nums[i], nums[i+1]
    if (a%3==0 or b%3==0) and (a+b<=max3):
        count += 1      
        sm = nums[i] + nums[i+1]
        max_sm = max(max_sm, sm)

print(count, max_sm)