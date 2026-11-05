# Task 2.1

Find the maximum of three numbers. Trace for (5, 9, 2).

## 1. Pseudocode

```text
BEGIN
    INPUT a, b, c
    max ← a
    IF b > max THEN
        max ← b
    END
    IF c > max THEN
        max ← c
    END
    OUTPUT max
END
 ```
## 2. Trace Table

| Step | a | b | c | max | b > max | c > max |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 5 | 9 | 2 | 5 | — | — |
| 1 | 5 | 9 | 2 | 9 | yes (9 > 5) | — |
| 2 | 5 | 9 | 2 | 9 | — | no (2 > 9) |

**Output:** `9`