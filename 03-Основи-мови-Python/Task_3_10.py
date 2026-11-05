minutes, price, vat_percent = input().split()
minutes = float(minutes)
price = float(price)
vat_percent = float(vat_percent)

without_vat = minutes * price
vat_amount = without_vat * (vat_percent / 100)
total = without_vat + vat_amount

print(f"без ПДВ: {without_vat:.2f}")
print(f"ПДВ:     {vat_amount:.2f}")
print(f"разом:   {total:.2f}")