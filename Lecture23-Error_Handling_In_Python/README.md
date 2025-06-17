# Lecture 23: Error Handling in Python

---

## 🧠 What You’ll Learn

This lecture introduces **exception handling** in Python, which allows your program to manage and respond to errors without crashing.

---

## ⚠️ Why Error Handling?

Errors are common in real-world programs, such as:

* Trying to divide by zero
* Accessing a non-existent file
* Using wrong data types or undefined variables

**Without handling, these will crash your program.**

---

## 🔍 Types of Errors

| Type              | Description                       | Example                |
| ----------------- | --------------------------------- | ---------------------- |
| **Syntax Error**  | Code is not written properly      | Missing parenthesis    |
| **Runtime Error** | Error occurs during execution     | Division by zero       |
| **Logical Error** | Code runs, but gives wrong result | Incorrect formula used |

---

## 🧩 Python Exception Handling Keywords

| Keyword   | Purpose                                          |
| --------- | ------------------------------------------------ |
| `try`     | Wraps code that might raise an error             |
| `except`  | Handles the specific error if it occurs          |
| `else`    | Runs when no error occurs inside the `try` block |
| `finally` | Always runs, whether an error occurs or not      |
| `raise`   | Manually raises a custom error                   |

---

## 🧪 Common Exceptions Demonstrated

### ✅ `main.py` covers:

* **ZeroDivisionError**
  → Attempt to divide by zero
* **ValueError**
  → Non-integer entered when expecting an integer
* **IndexError**
  → Accessing an out-of-range index from a list
* **Raise Exception**
  → Manually raising an exception for negative age
* **Multiple Exceptions Handling**
  → Handling both `ValueError` and `ZeroDivisionError` separately

---

## 📁 Code File

### `main.py`

This file contains examples of how to handle various Python exceptions using `try`, `except`, `else`, and `raise`. Each block demonstrates a different type of error and how to prevent your program from crashing due to it.

---


