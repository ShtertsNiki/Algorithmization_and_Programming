# Task 2.5

Compute the number of digits of a natural number. Trace for 70500.

## 1. Pseudocode

```text
BEGIN
    INPUT n
    count ← 0
    IF n = 0 THEN
        count ← 1
    ELSE
        WHILE n > 0 DO
            count ← count + 1
            n ← n DIV 10
        END
    END
    OUTPUT count
END
```
## 2. Trace Table

| Step | n | count | n > 0 | count + 1 | n DIV 10 | Output |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 70500 | 0 | — | — | — | — |
| 1 | 70500 | 0 | yes (70500 > 0) | 1 | 7050 | — |
| 2 | 7050 | 1 | yes (7050 > 0) | 2 | 705 | — |
| 3 | 705 | 2 | yes (705 > 0) | 3 | 70 | — |
| 4 | 70 | 3 | yes (70 > 0) | 4 | 7 | — |
| 5 | 7 | 4 | yes (7 > 0) | 5 | 0 | — |
| 6 | 0 | 5 | no (0 > 0) | — | — | 5 |

**Output:** `5`