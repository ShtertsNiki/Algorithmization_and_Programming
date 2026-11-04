# Task 1.6

Given:
  x1, y1 — coordinates of the first point (real numbers)
  x2, y2 — coordinates of the second point (real numbers)

Find:
  d — distance between two points on a plane

Model:
  d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

Algorithm:
  1. Input x1, y1.
  2. Input x2, y2.
  3. Compute d = sqrt((x2 - x1)^2 + (y2 - y1)^2).
  4. Output d.
  5. End.

Tests:
  (0, 0), (3, 4) -> d = 5
  (1, 1), (1, 1) -> d = 0
  (-1, -1), (2, 3) -> d = 5