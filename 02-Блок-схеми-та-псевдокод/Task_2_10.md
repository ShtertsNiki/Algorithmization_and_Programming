# Task 2.10

Compute the sum of the series 1 + 1/2 + 1/3 + ... + 1/n. Trace for n = 4.

## 1. Pseudocode

```text
BEGIN
    INPUT n
    sum ← 0.0
    i ← 1
    WHILE i <= n DO
        sum ← sum + (1 / i)
        i ← i + 1
    END
    OUTPUT sum
END
```
## 2. Trace Table

| Step | n | i | sum | i <= n | Output |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 4 | 1 | 0.0 | — | — |
| 1 | 4 | 1 | 1.0 | yes (1 <= 4) | — |
| 2 | 4 | 2 | 1.5 | yes (2 <= 4) | — |
| 3 | 4 | 3 | 1.833 | yes (3 <= 4) | — |
| 4 | 4 | 4 | 2.083 | yes (4 <= 4) | — |
| 5 | 4 | 5 | 2.083 | no (5 <= 4) | 2.083 |

**Output:** `2.083`