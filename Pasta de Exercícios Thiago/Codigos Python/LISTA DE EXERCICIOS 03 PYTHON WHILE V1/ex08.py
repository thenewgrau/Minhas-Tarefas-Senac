nums = []
num = 0
while num < 10:
    n = int(input("Digite seu número para somar "))
    if n < 0:
        continue
    else:
        nums.append(n)
        num += 1

print(sum(nums) / len(nums))