# Task 2.2

Determine the sign of a number (positive, negative, or zero). Trace for x = -4.

## 1. Pseudocode

```text
BEGIN
    INPUT x
    IF x > 0 THEN
        OUTPUT "Positive"
    ELSE IF x < 0 THEN
        OUTPUT "Negative"
    ELSE
        OUTPUT "Zero"
    END
END
```
## 2. Trace Table

| Step | x | x > 0 | x < 0 | Output |
| :---: | :---: | :---: | :---: | :---: |
| 0 | -4 | — | — | — |
| 1 | -4 | no (-4 > 0) | — | — |
| 2 | -4 | — | yes (-4 < 0) | "Negative" |

**Output:** `"Negative"`