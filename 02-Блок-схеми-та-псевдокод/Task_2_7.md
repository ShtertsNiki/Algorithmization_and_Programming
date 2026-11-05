# Task 2.7

Find the greatest common divisor of two natural numbers (the Euclidean algorithm with subtraction). Trace for (48, 18).

## 1. Pseudocode

```text
BEGIN
    INPUT a, b
    WHILE a ≠ b DO
        IF a > b THEN
            a ← a - b
        ELSE
            b ← b - a
        END
    END
    OUTPUT a
END
```
## 2. Trace Table

| Step | a | b | a ≠ b | a > b | Output |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 48 | 18 | — | — | — |
| 1 | 48 | 18 | yes (48 ≠ 18) | yes (48 > 18) | — |
| 2 | 30 | 18 | yes (30 ≠ 18) | yes (30 > 18) | — |
| 3 | 12 | 18 | yes (12 ≠ 18) | no (12 > 18) | — |
| 4 | 12 | 6 | yes (12 ≠ 6) | yes (12 > 6) | — |
| 5 | 6 | 6 | no (6 ≠ 6) | — | 6 |

**Output:** `6`