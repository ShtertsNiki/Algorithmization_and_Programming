n = int(input())

d1 = n // 10000
d2 = (n // 1000) % 10
d3 = (n // 100) % 10
d4 = (n // 10) % 10
d5 = n % 10

sum = d1 + d2 + d3 + d4 + d5
prod = d1 * d2 * d3 * d4 * d5

print(f"сума = {sum}, добуток = {prod}")