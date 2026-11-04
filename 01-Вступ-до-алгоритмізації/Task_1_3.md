# Task 1.3

Given:
  a > 0, b > 0, c > 0 — dimensions of the rectangular cuboid (real numbers)

Find:
  V — volume of the rectangular cuboid
  S — total surface area of the rectangular cuboid

Model:
  V = a * b * c
  S = 2 * (a*b + b*c + a*c)

Algorithm:
  1. Input a, b, c.
  2. Compute V = a * b * c.
  3. Compute S = 2 * (a*b + b*c + a*c).
  4. Output V, S.
  5. End.

Tests:
  (1, 2, 3) -> V = 6, S = 22
  (2, 2, 2) -> V = 8, S = 24
  (0.5, 1, 2) -> V = 1, S = 7