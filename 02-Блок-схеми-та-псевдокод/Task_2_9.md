# Task 2.9

Check whether a natural number is prime. Trace for 21.

## 1. Pseudocode

```text
BEGIN
    INPUT n
    isPrime ← true
    IF n < 2 THEN
        isPrime ← false
    ELSE
        i ← 2
        WHILE i * i <= n DO
            IF n MOD i = 0 THEN
                isPrime ← false
                BREAK
            END
            i ← i + 1
        END
    END
    IF isPrime THEN
        OUTPUT "Prime"
    ELSE
        OUTPUT "Not prime"
    END
END
```
## 2. Trace Table
| Step | n | isPrime | i | i * i <= n | n MOD i = 0 | Output |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 21 | true | — | — | — | — |
| 1 | 21 | true | 2 | yes (4 <= 21) | no (21 MOD 2 = 1) | — |
| 2 | 21 | true | 3 | yes (9 <= 21) | yes (21 MOD 3 = 0) | — |
| 3 | 21 | false | 3 | — (BREAK) | — | "Not prime" |

**Output:** `"Not prime"`