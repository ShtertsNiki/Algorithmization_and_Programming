deposit, rate = map(float, input().split())

total = deposit * ((1 + rate / 100) ** 3)

print(f"{total:.2f}")