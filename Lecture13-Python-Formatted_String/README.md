# 🧵 Lecture 13: Python f-String (Formatted String)

---

## 🧠 What is an f-String?

- An **f-string** is a modern and powerful way to format strings in Python.
- Introduced in **Python 3.6**.
- Syntax: Add an **`f`** before the string and wrap variables or expressions inside **curly braces `{}`**.

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

---

## 🕰️ Old Methods (Now Outdated)

### 1. **% Formatting**  
```python
message = "My name is %s and I am %d years old." % (name, age)
```

### 2. **Concatenation**  
```python
print(name + " is " + age + " years old")
```

Both of these are longer, messier, and more error-prone compared to f-strings.

---

## ✨ Why Use f-Strings?

- **Cleaner and easier to read**
- **Supports expressions** like math inside `{}`  
  ```python
  print(f"5 * 3 = {5 * 3}")
  ```
- **Supports dictionary and list values**  
  ```python
  data = {"name": "Babar", "age": 30}
  print(f"Name: {data['name']}, Age: {data['age']}")
  ```

---

## 📏 Formatting Values

You can format numbers easily:

```python
pi = 3.1415926535
print(f"The value of pi is {pi:.2f}")  # Output: 3.14
```

---

## 📄 Multiline f-Strings

Use triple quotes to create multi-line formatted strings:

```python
name = "John"
age = 28
bio = f"""
Name: {name}
Age: {age}
"""
```

---

## 🧪 Example (User Input & f-String)

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
```

---

## ✅ Summary

| Feature            | f-String                 | Old Methods (% / format / +) |
|--------------------|--------------------------|-------------------------------|
| Easy to Read       | ✅                        | ❌                            |
| Supports Expressions | ✅                      | ❌                            |
| Introduced in       | Python 3.6              | Older versions                |
| Multiline Support   | ✅                        | ❌ (harder to write)          |

➡️ Use **f-strings** for modern, clean, and efficient string formatting.

---
