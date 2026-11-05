# Task 2.3

Compute n! (factorial). Trace for n = 5.

## 1. Pseudocode

```text
BEGIN
    INPUT n
    fact ← 1
    i ← 1
    WHILE i <= n DO
        fact ← fact * i
        i ← i + 1
    END
    OUTPUT fact
END
```
## 2. Trace Table

| Step | n | i | fact | i <= n | Output |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 5 | 1 | 1 | — | — |
| 1 | 5 | 1 | 1 | yes (1 <= 5) | — |
| 2 | 5 | 2 | 2 | yes (2 <= 5) | — |
| 3 | 5 | 3 | 6 | yes (3 <= 5) | — |
| 4 | 5 | 4 | 24 | yes (4 <= 5) | — |
| 5 | 5 | 5 | 120 | yes (5 <= 5) | — |
| 6 | 5 | 6 | 120 | no (6 <= 5) | 120 |

**Output:** `120`