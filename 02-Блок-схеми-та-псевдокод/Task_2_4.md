# Task 2.4

Compute the sum of the digits of a natural number. Trace for 1234.

## 1. Pseudocode

```text
BEGIN
    INPUT n
    sum ← 0
    WHILE n > 0 DO
        digit ← n MOD 10
        sum ← sum + digit
        n ← n DIV 10
    END
    OUTPUT sum
END
```
## 2. Trace Table

| Step | n | sum | n > 0 | digit (n MOD 10) | sum + digit | n DIV 10 | Output |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1234 | 0 | — | — | — | — | — |
| 1 | 1234 | 0 | yes (1234 > 0) | 4 | 4 | 123 | — |
| 2 | 123 | 4 | yes (123 > 0) | 3 | 7 | 12 | — |
| 3 | 12 | 7 | yes (12 > 0) | 2 | 9 | 1 | — |
| 4 | 1 | 9 | yes (1 > 0) | 1 | 10 | 0 | — |
| 5 | 0 | 10 | no (0 > 0) | — | — | — | 10 |

**Output:** `10`