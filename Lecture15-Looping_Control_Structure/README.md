# 📘 Lecture 15: Python Looping Control Structure (While & For Loops)

In this lesson, we explored **looping in Python** — an essential part of programming that allows us to **repeatedly execute a block of code** under certain conditions.

---

## 🔄 What is Looping?

Looping is used when we want to **repeat a set of instructions** multiple times. In Python, the two main types of loops are:

### 1️⃣ `while` Loop
- Executes a block **as long as a given condition is `True`**.
- Useful when we **don't know in advance** how many times to run the loop.

```python
x = 1
while x <= 5:
    print(x)
    x += 1
```

### 2️⃣ `for` Loop
- Used to **iterate over a sequence** (like a list, string, or `range()`).
- Best when we **know the number of repetitions**.

```python
for i in range(5):
    print(i)
```

---

## 🧠 Key Concepts Covered

- `while` loop basics and real-world examples
- Taking user input in a loop
- Using loops to build guessing games
- `for` loop with `range(start, stop, step)`
- Conditional checks inside loops
- Difference between `while` and `for` loops

---

## 📂 Files in This Lecture

- `while_loop.py` – Examples using the `while` loop
- `for_loop.py` – Examples using the `for` loop

---

## 📌 Notes

- Use `while` loop when you only know the condition, **not the number of repetitions**.
- Use `for` loop when you know **how many times** you want to repeat something.
- `range()` is commonly used with `for` loops:
  - `range(stop)`
  - `range(start, stop)`
  - `range(start, stop, step)`

---

## 📝 Assignments

### ✅ Guess the Player
Write a program where the user must **guess the name of a current Pakistani cricket player** (e.g. "Shaheen Afridi") using a `while` loop. Display the total number of attempts.

### ✅ Even or Odd Check (Using `for` Loop)
Take a number from the user and use a `for` loop to check if the number is **even or odd**.

---

## 🎯 Outcome

By the end of this lecture, you should be able to:
- Use `while` and `for` loops effectively
- Decide which loop type fits best in a given situation
- Use `range()` for iteration
- Combine loops with `if-else` for dynamic programs
