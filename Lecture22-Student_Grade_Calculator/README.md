# Lecture 22: Student Grade Calculator 📊

---

## 🧠 What You’ll Learn

In this lecture, you’ll learn how to:

* Take input for multiple subjects
* Calculate the **average**
* Determine the **letter grade**
* Validate user input
* Loop through multiple students (in assignment)

This teaches important concepts like **lists**, **loops**, **input validation**, and **decision-making** in Python.

---

## 📂 Files Included

### ✅ `main.py`

A **simple grade calculator** for a single student.

* Takes marks for **5 subjects**
* Ensures marks are between **0 and 100**
* Calculates:

  * Total Marks
  * Average Score
  * Letter Grade

| Average Range | Grade |
| ------------- | ----- |
| 90 – 100      | A     |
| 80 – 89       | B     |
| 70 – 79       | C     |
| 60 – 69       | D     |
| Below 60      | F     |

---

### 📝 `assignment.py`

A more advanced **Student Performance Report System**:

* Asks for the **number of students**
* Inputs:

  * Student’s **Name**
  * **Roll Number**
  * Marks for **6 subjects**: Math, Science, English, History, Computer, Physics
* Validates marks using `try-except` and range checking

### 📊 Outputs:

* Total Marks
* Average (rounded to **2 decimal places**)
* Letter Grade (based on average)

| Average Range | Grade |
| ------------- | ----- |
| 95 – 100      | A+    |
| 85 – 94       | A     |
| 75 – 84       | B     |
| 65 – 74       | C     |
| 50 – 64       | D     |
| Below 50      | F     |

---

## 💡 Concepts Practiced

* `for` loops and nested input
* List data structure for storing marks
* Conditional statements (`if-elif-else`)
* Error handling with `try-except`
* User input validation
* Use of `round()` function for formatting

---

