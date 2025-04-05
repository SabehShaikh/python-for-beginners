# Python `.copy()` Method – Lecture 11 Notes

## 🔍 What is `.copy()`?

- `.copy()` is used to create a **shallow copy** of mutable objects like lists and dictionaries.
- A **shallow copy** means:
  - The outer object is copied.
  - **Inner mutable elements still refer to the same memory address** as the original.

## ⚠️ Important Points:

- `.copy()` **does not work** on immutable types like:
  - Numbers (`int`, `float`)
  - Strings (`str`)
  - Tuples (`tuple`)
- Trying to modify an inner mutable object (like a list inside a list) **will affect both copies**.

---

## ✅ Examples:

### Shallow Copy with Immutable Elements:
```python
orig_list = [1, 'hello', (20, 30)]
new_list = orig_list.copy()
new_list[1] = 'world'  # Works
# new_list[2][0] = 25  # ❌ Not allowed (tuple is immutable)

print("Original list:", orig_list)
print("New list:", new_list)
