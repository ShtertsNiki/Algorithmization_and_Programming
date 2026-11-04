# Task 1.10

Given:
  price > 0 — unit price of the item (real number)
  quantity > 0 — number of items purchased (integer or real number)
  discount >= 0 — discount in percent (real number)

Find:
  total — final cost of the purchase

Model:
  subtotal = price * quantity
  total = subtotal * (1 - discount / 100)

Algorithm:
  1. Input price, quantity, discount.
  2. Compute subtotal = price * quantity.
  3. Compute total = subtotal * (1 - discount / 100).
  4. Output total.
  5. End.

Tests:
  (price = 100, quantity = 2, discount = 10) -> total = 180
  (price = 50, quantity = 5, discount = 0) -> total = 250
  (price = 200, quantity = 1, discount = 25) -> total = 150