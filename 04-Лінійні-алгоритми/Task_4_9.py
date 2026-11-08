n = int(input())

d1 = n // 10
d2 = n % 10

result = d2 * 10 + d1
sum = n + result

print(f"{result}, сума = {sum}")