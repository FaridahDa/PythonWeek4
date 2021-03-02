import random

lotto_nums = set()


while len(lotto_nums) < 6:
    number = random.randint(1, 50)
    lotto_nums.add(number)

print(lotto_nums)
# redo this! collection of lotto numners, sets to store the numbers
