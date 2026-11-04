# Task 1.7

Given:
  t > 0 — travel time in hours (real number)
  v > 0 — speed in km/h (real number)
  q > 0 — fuel consumption rate in liters per 100 km (real number)

Find:
  s — distance traveled in km
  f — total fuel consumed in liters

Model:
  s = v * t
  f = (s / 100) * q

Algorithm:
  1. Input t, v, q.
  2. Compute s = v * t.
  3. Compute f = (s / 100) * q.
  4. Output s, f.
  5. End.

Tests:
  (t = 2, v = 60, q = 8) -> s = 120, f = 9.6
  (t = 1.5, v = 100, q = 7) -> s = 150, f = 10.5
  (t = 0.5, v = 80, q = 10) -> s = 40, f = 4
