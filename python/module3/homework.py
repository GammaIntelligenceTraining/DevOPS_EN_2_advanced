"""
Module 3 Homework: Student Grade Analyzer

Overview:
In this assignment, you will write a script that processes a list of student 
records (represented as dictionaries). You will evaluate their scores using a 
custom Python function, and use a Set to find out which unique subjects have 
students who are failing.

This assignment reinforces:
1. Functions: Defining `def`, using conditional logic, and returning multiple values.
2. Dictionaries: Safe payload parsing using `.get()`.
3. Tuples: Returning and unpacking immutable pairs `(Name, Grade)`.
4. Sets: Automatically deduplicating overlapping data.

Execution:
    Run directly in VS Code by clicking the Play button, or run in the integrated terminal:
    - Windows (PowerShell): python homework.py
    - macOS (Terminal)    : python3 homework.py
"""

# ==============================================================================
# Provided Student Data (Do not modify this fixture)
# ==============================================================================
STUDENT_RECORDS = [
    {"name": "Alice", "score": 85, "subject": "Math"},
    {"name": "Bob", "score": 55, "subject": "History"},
    {"name": "Charlie", "score": 92, "subject": "Science"},
    {"name": "Diana", "score": 45, "subject": "Math"},
    {"name": "Eve", "score": 78, "subject": "History"},
    {"name": "Frank", "score": 30, "subject": "Science"},
    {"name": "Grace", "score": 40, "subject": "Math"}
]

TOTAL_EVALUATIONS = 0  # GLOBAL VARIABLE

# ==============================================================================
# TASK 1 & 2: Define the Evaluation Function (Dictionaries, Tuples & Scope)
# ==============================================================================
# 1. Define a function named `evaluate_student` that accepts a single parameter:
#    `student_dict` (which will be a dictionary).
# 2. Inside the function, use the `global` keyword to bring `TOTAL_EVALUATIONS` 
#    into the local scope, and increment it by 1.
# 3. Use `.get()` to safely extract the following values:
#    - "name" (default to "Unknown")
#    - "score" (default to 0)
# 4. Determine the letter grade based on these rules:
#    - If score is >= 90, grade is "A".
#    - If score is >= 80, grade is "B".
#    - If score is >= 70, grade is "C".
#    - Otherwise, grade is "F".
# 5. Return BOTH the extracted name AND the letter grade as a Tuple.

# TODO 1 & 2: Define the evaluate_student function here


# ==============================================================================
# TASK 3 & 4: Processing the List & Deduplication (for Loops & Sets)
# ==============================================================================
# 1. Initialize an empty Set named `failing_subjects`. (Hint: use set())
# 2. Write a `for` loop to iterate over the `STUDENT_RECORDS` list.
# 3. Inside the loop:
#    - Pass the current student dictionary to your `evaluate_student()` function.
#    - Unpack the returned tuple into two variables (e.g., `student_name` and `grade`).
#    - Print a message showing the student's name and their grade.
#    - If the grade is "F", extract their "subject" from the dictionary using `.get()`
#      and add that subject to the `failing_subjects` Set.

print("=" * 40)
print("STARTING GRADE ANALYSIS")
print("=" * 40)

# TODO 3 & 4: Initialize the set and write the for loop


# ==============================================================================
# TASK 5: Audit Reporting & Global Scope Verification
# ==============================================================================
# 1. Print a blank line.
# 2. Print the value of the `TOTAL_EVALUATIONS` global variable to prove your 
#    function correctly modified it (It should be 7).
# 3. Write a `for` loop to iterate over your deduplicated `failing_subjects` Set.
# 4. Print each unique subject that has at least one failing student.

print("\n" + "=" * 40)
print("SUBJECTS NEEDING IMPROVEMENT")
print("=" * 40)

# TODO 5: Print the total evaluations and the unique failing subjects
