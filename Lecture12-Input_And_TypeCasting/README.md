# 🧠 Lecture 12: `input()` and Type Casting

---

## 🧾 `input()` Function

- The `input()` function is used to take **user input**.
- It **always returns a string**, no matter what the user types.
- To use the input in mathematical operations, we often need to **convert (cast)** it into other data types like `int`, `float`, etc.

---

## 🔁 What is Type Casting?

Type casting means **converting one data type to another**.  
There are two types of type casting in Python:

---

## 🤖 1. Implicit Type Casting

- Done **automatically** by Python.
- Occurs in certain operations like arithmetic or combining `int` with `float`, or `bool` with `int`.
- Limited and cannot handle all conversions.

**Example:**  
`int + float = float`  
`True + 5 = 6` (since `True` is treated as `1`)

---

## ✋ 2. Explicit Type Casting

- Done **manually** by the programmer.
- Used to avoid errors and control how data behaves.

### Common Functions:
| Function   | Converts To        |
|------------|--------------------|
| `int()`    | Integer             |
| `float()`  | Float               |
| `str()`    | String              |
| `bool()`   | Boolean             |
| `list()`   | List                |
| `tuple()`  | Tuple               |
| `dict()`   | Dictionary (from key-value pairs) |
| `set()`    | Set                 |

---

## 🎯 Examples of Explicit Type Casting

| From → To     | Code Example                            |
|---------------|------------------------------------------|
| Float → Int   | `int(9.99)` → `9`                        |
| Int → Float   | `float(7)` → `7.0`                       |
| List → Tuple  | `tuple([1, 2, 3])` → `(1, 2, 3)`         |
| Tuple → List  | `list((1, 2, 3))` → `[1, 2, 3]`          |
| String → List | `list("hello")` → `['h', 'e', 'l', 'l', 'o']` |
| List → Set    | `set([1, 2, 3])` → `{1, 2, 3}`           |

---

## ✅ Summary

- `input()` gives **string** → use casting to convert.
- **Implicit casting** happens automatically (but limited).
- **Explicit casting** is done manually using functions like `int()`, `float()`, `bool()`, etc.



