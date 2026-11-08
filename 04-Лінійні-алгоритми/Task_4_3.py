min = int(input())

days = min // 1440
hours = (min % 1440) // 60
minutes = min % 60

print(f"{days} діб {hours} год {minutes} хв ")