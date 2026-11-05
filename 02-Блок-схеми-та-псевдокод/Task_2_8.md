# Task 2.8

Output all divisors of a natural number n. Trace for n = 12.

## 1. Pseudocode

```text
BEGIN
    INPUT n
    d ← 1
    WHILE d <= n DO
        IF n MOD d = 0 THEN
            OUTPUT d
        END
        d ← d + 1
    END
END
```
## 2. Trace Table

| Step | n | d | d <= n | n MOD d = 0 | Output |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 12 | 1 | — | — | — |
| 1 | 12 | 1 | yes (1 <= 12) | yes (12 MOD 1 = 0) | 1 |
| 2 | 12 | 2 | yes (2 <= 12) | yes (12 MOD 2 = 0) | 2 |
| 3 | 12 | 3 | yes (3 <= 12) | yes (12 MOD 3 = 0) | 3 |
| 4 | 12 | 4 | yes (4 <= 12) | yes (12 MOD 4 = 0) | 4 |
| 5 | 12 | 5 | yes (5 <= 12) | no (12 MOD 5 = 2) | — |
| 6 | 12 | 6 | yes (6 <= 12) | yes (12 MOD 6 = 0) | 6 |
| 7 | 12 | 7 | yes (7 <= 12) | no (12 MOD 7 = 5) | — |
| 8 | 12 | 8 | yes (8 <= 12) | no (12 MOD 8 = 4) | — |
| 9 | 12 | 9 | yes (9 <= 12) | no (12 MOD 9 = 3) | — |
| 10 | 12 | 10 | yes (10 <= 12) | no (12 MOD 10 = 2) | — |
| 11 | 12 | 11 | yes (11 <= 12) | no (12 MOD 11 = 1) | — |
| 12 | 12 | 12 | yes (12 <= 12) | yes (12 MOD 12 = 0) | 12 |
| 13 | 12 | 13 | no (13 <= 12) | — | — |

**Output:** `1, 2, 3, 4, 6, 12`