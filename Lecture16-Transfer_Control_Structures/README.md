# 🔀 Lecture 16: Python Transfer Control Structures (`break`, `continue`, `pass`)

In this lecture, we explored **transfer control statements** in Python, which are used to **change the normal flow** of loops. These include:

* `break` – exits the loop completely
* `continue` – skips the current iteration and moves to the next
* `pass` – does nothing (used as a placeholder)

---

## 🧠 Why Use Transfer Statements?

Sometimes, you need to:

* **Exit a loop early** (e.g. once a condition is met)
* **Skip certain iterations** (e.g. skip even numbers)
* **Leave a block empty** while planning logic (without getting errors)

---

## 🔓 `break` Statement

Used to **immediately stop** a loop.

```python
x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1
```

📌 Useful when:

* A **goal is met early**
* A **user guess is correct**
* You want to **exit an infinite loop**

---

## ⏭️ `continue` Statement

Used to **skip the current loop iteration** and continue with the next one.

```python
for num in range(1, 10):
    if num == 6:
        continue
    print(num)
```

📌 Useful when:

* You want to **avoid specific values**
* You want to **filter inputs**
* You want to **skip some logic** under a condition

---

## 🛑 `pass` Statement

Used when a statement is **syntactically required** but **no action is needed**.

```python
if True:
    pass
```

📌 Useful for:

* Writing **placeholder code**
* Avoiding errors in **empty blocks**
* Planning **future logic**

---

## 📂 Files in This Lecture

* `break.py` – Examples using the `break` statement
* `continue.py` – Examples using the `continue` statement
* `pass.py` – Examples using the `pass` statement
* `assignment01.py` – Stop on user input using `break`
* `assignment02.py` – Print numbers divisible by 3 using `continue`
* `assignment03.py` – Skip a number using `pass`
* `assignment04.py` – Combine all three statements in one loop

---

## 📝 Assignments

### ✅ Stop on Zero

Write a loop that **keeps asking for a number**. Stop the loop when the user enters `0`.

### ✅ Print Numbers Divisible by 3

Use a `for` loop to print numbers **from 1 to 100**, **skipping all** that are **not divisible by 3** using `continue`.

### ✅ Use of `pass`

Write a loop from **1 to 5**. Do **nothing** if the number is `3`, otherwise print the number.

### ✅ Combine All Transfer Statements

Write a loop from 1 to 20:

* If number is divisible by 7 → `break`
* If divisible by 3 → `continue`
* If even and < 10 → use `pass`
* Otherwise → print the number

---

## 🎯 Outcome

By the end of this lecture, you should be able to:

* Exit loops early using `break`
* Skip iterations using `continue`
* Use `pass` to create placeholder blocks
* Choose the **right control transfer** statement based on your loop logic


