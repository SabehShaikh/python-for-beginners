# 📚 Lecture 9: Python List Methods

Python provides a variety of built-in methods to work with lists. These methods help in adding, removing, searching, and manipulating list elements.

---

## 🧩 Common List Methods (With Description)

### 🔹 `append(item)`
- Adds a single item to the **end** of the list.
- If the item is another list, it will be added as a **nested list**.

### 🔹 `extend(iterable)`
- Adds **multiple items** from another iterable (like a list) to the end.
- Unlike `append`, it does not create a nested list.

### 🔹 `insert(index, item)`
- Inserts an item at a **specific position** in the list.
- Existing elements are shifted to the right.

### 🔹 `remove(item)`
- Removes the **first occurrence** of the specified item.
- Raises an error if the item is not found.

### 🔹 `pop(index)`
- Removes and returns the item at the given index.
- If no index is specified, removes the **last item** by default.

### 🔹 `clear()`
- Removes **all items** from the list, making it empty.

### 🔹 `index(item)`
- Returns the **index** of the first matching item.
- Can also specify `start` and `end` range.

### 🔹 `count(item)`
- Returns how many times an item appears in the list.

### 🔹 `sort()`
- Sorts the list in **ascending order** by default.
- Use `reverse=True` to sort in **descending order**.

### 🔹 `reverse()`
- Reverses the current order of the list.

---

## 🧠 Notes:
- All these methods **modify the original list** (except `index()` and `count()`).
- Use these methods to effectively manage and manipulate list data in Python.

