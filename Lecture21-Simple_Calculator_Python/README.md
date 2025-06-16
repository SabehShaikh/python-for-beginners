# Lecture 21: Create Simple Calculator in Python

---

## 🔹 What You'll Learn

This lecture focused on applying problem-solving skills to build a working calculator in Python using both procedural and functional approaches.

---

### ✅ **Problem Solving Steps for the Calculator**

1. Display the calculator menu
2. Take user input for the operation
3. Perform the operation based on user choice
4. Exit the program using a break condition

---

### 🔁 **Loop Concept Used**

* `while True` loop ensures the calculator keeps running until the user chooses to exit.
* Helps in continuously prompting the user without restarting the program manually.

---

## 📁 Code Files

### `main.py`

Implements a **menu-driven calculator** using a `while True` loop and `if-else` conditions.

**Operations included:**

* Addition
* Subtraction
* Multiplication
* Division (with zero check)
* Floor Division
* Percentage
* Exit option

---

### `calc_with_function.py`

A **function-based version** of the calculator. Includes:

* Menu displayed using a function
* Each arithmetic operation implemented as a separate function
* Cleaner and modular code with better structure

---

### `assignment01.py`

**Task:**
Write a program to compute:

> $(a + b)^2 = a^2 + 2ab + b^2$

**Approach:**

* Takes `a` and `b` as input from the user
* Performs calculation without using functions
* Displays the result

✅ **Completed without user-defined function**

---

### `assignment02.py`

**Task:**
Same formula as above:

> $(a + b)^2 = a^2 + 2ab + b^2$

**Approach:**

* Uses a user-defined function `calculate_square(a, b)`
* Function returns the result
* Final output is displayed using the returned value

✅ **Completed using a user-defined function**

---

