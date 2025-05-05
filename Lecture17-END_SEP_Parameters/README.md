# Lecture 17: Python `end` & `sep` Parameters  
*Customizing the `print()` Function*

---

## 🔹 What You'll Learn

In this lecture, we explored how to customize Python’s `print()` function using two optional parameters:

### ✅ `end` Parameter
- Controls **what to print at the end** of the output.
- **Default:** `\n` (new line).
- Example:
  ```python
  print("Hello", end=" ")
  print("World")  # Output: Hello World
````

### ✅ `sep` Parameter

* Controls **what to print between items**.
* **Default:** `" "` (single space).
* Example:

  ```python
  print("Hello", "World", sep="-")  # Output: Hello-World
  ```

---

## 📁 Code Files

### `main.py`

Demonstrates use of `end` to:

* Prevent line breaks.
* Simulate email IDs.
* Combine user input with text.

---

### `sep.py`

Shows how `sep` can:

* Change separators between values.
* Format text like `"index:0"` in a loop.

---

## 📝 Assignments

### `assignment01.py`

✔ **Task:** Print numbers `1 2 3 4 5` in one line using a loop.
✔ **Only** use `print()` and the `end` parameter — no string concatenation.


---

### `assignment02.py`

✔ **Task:**

* Print your full name with dashes.
* Print date as `DD-MM-YYYY`.
* Print email using `sep`.


---

### `assignment03.py`

✔ **Task:**

* Print: `[1] [2] [3] [4]`
* Print: `Option 1 | Option 2 | Option 3`






