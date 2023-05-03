three_digits_num = input("Please enter three digits (each digit for one pig): ")
a, b, c = int(three_digits_num[0]), int(three_digits_num[1]), int(three_digits_num[2])

total_bricks = a + b + c
bricks_per_pig = total_bricks // 3
remainder = total_bricks % 3
even_distribution = remainder == 0

print("Total number of bricks collected:", total_bricks)
print("Number of bricks per pig:", bricks_per_pig)
print("Remainder of brick distribution:", remainder)
print("Bricks evenly distributed:", even_distribution)
