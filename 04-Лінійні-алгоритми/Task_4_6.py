n = int(input())

cash = n // 100
coin = n % 100

print(f"{cash} грн {coin:02d} коп ")