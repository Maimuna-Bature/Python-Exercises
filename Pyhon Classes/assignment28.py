#write a programme to calculate Simple Interest
def calculate_si(p,n,r):
    si = (p * n * r) / 100
    return si
for i in range(3):
    p = float(input(f"Enter Principal for set {i+1}: "))
    n = float(input(f"Enter Time for set {i+1}: "))
    r = float(input(f"Enter Rate for set {i+1}: "))
    si = calculate_si(p, n, r)
    print(f"Simple Interest for set {i+1}: {si}")
calculate_si(p,n,r)


