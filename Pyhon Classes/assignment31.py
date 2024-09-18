# write a programme to calculate the series 1+1/4+1/7+1/10+1/13+1/16+1/19+1/22+1/25
total = 0
denominator = 1
for i in range(9):
    total += 1 / denominator
    denominator += 3
print("Sum of series:", total)
