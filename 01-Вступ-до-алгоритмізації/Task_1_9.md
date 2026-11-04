# Task 1.9

Given:
  a > 0, b > 0, c > 0 — sides of the triangle (real numbers)

Constraints:
  a + b > c
  a + c > b
  b + c > a

Find:
  S — area of the triangle

Model:
  p = (a + b + c) / 2
  S = sqrt(p * (p - a) * (p - b) * (p - c))

Algorithm:
  1. Input a, b, c.
  2. Compute p = (a + b + c) / 2.
  3. Compute S = sqrt(p * (p - a) * (p - b) * (p - c)).
  4. Output S.
  5. End.

Tests:
  (3, 4, 5) -> S = 6
  (6, 8, 10) -> S = 24
  (5, 5, 6) -> S = 12
