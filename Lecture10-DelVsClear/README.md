# 🧹 Lecture 10: `del` vs `clear()`

Both `del` and `clear()` are used to remove data, but they behave differently in Python.

---

## 🔑 `del` Keyword

- `del` is a **keyword**, not a method.
- Used to **delete variables, list elements, or entire objects**.
- Deletes the **reference** from memory.
- Works with any variable type (list, int, string, etc.).

### ✅ Example:
```python
x = 10
del x
# print(x)  # ❌ Will raise NameError because x was deleted

```

```python
list2 = [10, 20, 30, 40]
del list2[2]
# Output: [10, 20, 40]
```

---

## 🧼 `clear()` Method

- `clear()` is a **method**, available for **lists, dictionaries, and sets**.
- It removes **all elements** but keeps the object reference intact.
- Useful when you want to **empty** a structure without deleting it.

### ✅ Example:
```python
list1 = [1, 2, 3]
list1.clear()
# Output: []
```

---

## ⚠️ Error Example (Incorrect Usage):
```python
list3 = [10, 20, 30, 40]
list3[2].clear()  
# ❌ AttributeError: 'int' object has no attribute 'clear'
```

---

## 🧠 Summary

| Feature      | `del`                       | `clear()`                      |
|--------------|-----------------------------|--------------------------------|
| Type         | Keyword                     | Method                         |
| Removes      | Reference + Data            | Only Data                      |
| Works On     | Any object                  | Lists, Sets, Dicts             |
| Keeps Ref?   | ❌ Deletes reference         | ✅ Keeps the reference          |
| Can delete by index? | ✅ Yes             | ❌ No                          |


