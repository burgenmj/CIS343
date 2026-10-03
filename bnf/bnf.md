# BNF

Expression: `1 - (2 * 3) < 4 == false`

## Derivation

```
1.
expression -> binary -> expression "==" expression
                        \> 1 - (2 * 3) < 4      \> false

2. (right, false)
expression -> literal -> false

3. (left, 1 - (2 * 3) < 4, <)
expression -> binary -> expression "<" expression
                        \> 1 - (2 * 3)      \> 4

4. (right, 4)
expression -> literal -> NUMBER(4)

5. (left, 1 - (2 * 3), -)
expression -> binary -> expression "-" expression
                        \> 1                \> (2 * 3)

6. (left, 1)
expression -> literal -> NUMBER(1)

7. (right, (2 * 3), ())
expression -> grouping -> "(" expression ")"
                                \> 2 * 3

8. (2 * 3)
expression -> binary -> expression "*" expression 
                        \> literal NUMBER(2)    \> literal NUMBER(3)

9. 
1 - (2 * 3)                 = NUMBER(1) "-" "(" NUMBER(2) "*" NUMBER(3) ")"
1 - (2 * 3) < 4             = // NUMBER(1) "-" "(" NUMBER(2) "*" NUMBER(3) ")" // "<" NUMBER(4)
1 - (2 * 3) < 4 == false    = // NUMBER(1) "-" "(" NUMBER(2) "*" NUMBER(3) ")" "<" NUMBER(4) // "==" "false"

Final
NUMBER(1) "-" "(" NUMBER(2) "*" NUMBER(3) ")" "<" NUMBER(4) "==" "false"
```

## Parse Tree 

```
+-- expression
|   +-- binary
|   |   +-- expression
|   |       +-- binary
|   |           +-- expression - literal - NUMBER 1
|   |           +-- operator - "-"
|   |           +-- expression
|   |               +-- grouping
|   |                   +-- "("
|   |                   +-- expression
|   |                   |   +-- binary
|   |                   |       +-- expression - literal - NUMBER 2
|   |                   |       +-- operator - "*"
|   |                   |       +-- expression - literal - NUMBER 3
|   |                   +-- ")"
|   +-- operator - "<"
|   +-- expression - literal - NUMBER 4
+-- operator - "=="
+-- expression - literal - "false"
```

## AST

```
(== (< (- 1 (group (* 2 3))) 4) false)
```