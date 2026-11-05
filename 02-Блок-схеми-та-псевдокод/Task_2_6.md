# Task 2.6

Compute a^n for an integer n >= 0 without using the exponentiation operator. Trace for a = 3, n = 4.

## 1. Pseudocode

```text
BEGIN
    INPUT a, n
    result ← 1
    i ← 1
    WHILE i <= n DO
        result ← result * a
        i ← i + 1
    END
    OUTPUT result
END
```
## 2. Trace Table

| Step | a | n | i | result | i <= n | Output |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 3 | 4 | 1 | 1 | — | — |
| 1 | 3 | 4 | 1 | 3 | yes (1 <= 4) | — |
| 2 | 3 | 4 | 2 | 9 | yes (2 <= 4) | — |
| 3 | 3 | 4 | 3 | 27 | yes (3 <= 4) | — |
| 4 | 3 | 4 | 4 | 81 | yes (4 <= 4) | — |
| 5 | 3 | 4 | 5 | 81 | no (5 <= 4) | 81 |

**Output:** `81`