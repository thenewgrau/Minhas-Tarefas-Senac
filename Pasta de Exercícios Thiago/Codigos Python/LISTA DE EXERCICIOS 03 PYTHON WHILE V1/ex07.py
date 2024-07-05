nums = []
num = 0
while num < 10:
    nums.append(int(input("Digite seu número para somar ")))
    num += 1

print(sum(nums)/len(nums))