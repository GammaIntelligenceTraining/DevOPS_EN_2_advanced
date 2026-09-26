#!/usr/bin/env python3
"""
Module 2 Homework: Student Gradebook & Performance Auditor

Overview:
In this assignment, you will write a complete Python script to process, grade,
audit, and summarize student exam records. This assignment reinforces core Python
fundamentals covered across Module 1 and Module 2:
1. Lists: indexing, sequence unpacking, slicing, .append(), .copy(), .remove(),
   sum(), min(), max(), and len().
2. Conditionals & Logic: if, elif, else, chained comparisons, and boolean
   operators (and, or, not).
3. Loops: for loops across lists and numerical sequences.
4. String methods: .strip(), .title(), and formatted f-strings.

Notice:
Do not use dictionaries, tuples, sets, or while loops in this assignment.
All state tracking, record structuring, and aggregations must be implemented
using lists, conditionals, strings, and for loops.

Execution:
    Run directly in VS Code by clicking the Play button, or run in the integrated terminal:
    - Windows (PowerShell): python homework.py
    - macOS (Terminal)    : python3 homework.py
"""

# ==============================================================================
# Provided Student Dataset (Do not modify this fixture)
# Format: [raw_name (str), exam_score (float), attendance_pct (float), course_track (str)]
# ==============================================================================
STUDENT_RECORDS = [
    ["  alice smith \n", 92.5, 95.0, "python"],
    ["BOB JONES\t",       78.0, 88.5, "python"],
    [" charlie brown ",   64.0, 72.0, "python"],
    ["diana prince",      88.5, 91.0, "python"],
    ["evan wright",       45.0, 48.0, "python"],
    ["frank castle\n",    85.0, 94.0, "python"],
    ["grace hopper ",     98.0, 99.0, "python"],
    ["henry cavill\t",    71.5, 82.0, "python"],
]


# ==============================================================================
# TASK 1: Initialize Tracking Lists, Unpack Records & Clean Names
# ==============================================================================
# 1. Initialize the following empty lists to accumulate data during iteration:
#    - 'cleaned_names'        : list to store sanitized student names
#    - 'all_scores'           : list to collect numeric exam scores for statistics
#    - 'honor_roll'           : list to store names of high-achieving students
#    - 'disqualified_students': list to store names of students with attendance < 50.0%
#    - 'audit_table_rows'     : list to store processed row lists for report printing
#
# 2. Loop over each record in STUDENT_RECORDS:
#    - Unpack each record into 4 variables on a single line:
#        raw_name, score, attendance, track = record
#    - Clean the student name: strip leading/trailing whitespace, tabs, and
#      newlines with .strip(), and format in title case using .title().
#    - Append the clean name to 'cleaned_names'.
#    - Append the numeric score to 'all_scores'.

# TODO 1: Initialize tracking lists
cleaned_names = []
all_scores = []
honor_roll = []
disqualified_students = []
audit_table_rows = []

# TODO 1: Loop, unpack, sanitize names, and populate cleaned_names and all_scores
for record in STUDENT_RECORDS:
    # Unpack record into variables:
    pass


# ==============================================================================
# TASK 2: Multi-Condition Grade Evaluation & Honors Qualification
# ==============================================================================
# In this task, you evaluate each student's performance:
#
# 1. Letter Grade Scale:
#    - "A" : score >= 90.0
#    - "B" : 80.0 <= score < 90.0
#    - "C" : 70.0 <= score < 80.0
#    - "F" : score < 70.0
#
# 2. Honor Roll Qualification:
#    A student earns an "HONORS" status badge and qualifies for 'honor_roll' if:
#    - Their exam score is at least 85.0 (score >= 85.0)
#    AND
#    - Their attendance percentage is at least 90.0 (attendance >= 90.0)
#    Otherwise, their status badge is "REGULAR".
#    If the student qualifies for honors, append their clean name to 'honor_roll'.
#
# 3. Attendance Disqualification Check:
#    - If attendance < 50.0, append their clean name to 'disqualified_students'.
#
# 4. Construct a row list for report printing:
#    Create a list containing: [clean_name, score, attendance, letter_grade, status_badge]
#    Append this row list to 'audit_table_rows'.
#
# Note: You can perform Task 2 inside the same loop as Task 1, or as a second loop
# over STUDENT_RECORDS.

# TODO 2: Implement letter grading, honors filtering, and audit_table_rows accumulation


# ==============================================================================
# TASK 3: Safe Collection Mutation (Demonstrating .copy() and .remove())
# ==============================================================================
# In systems automation, modifying a list while looping over it directly causes
# index shifting bugs that silently skip elements.
#
# 1. Create an independent shallow copy of 'cleaned_names' using .copy():
#    active_students = cleaned_names.copy()
#
# 2. Iterate over 'disqualified_students':
#    - For each disqualified name, safely remove them from 'active_students'
#      using the .remove() method.
#    - Hint: Guard with an 'if name in active_students:' check before removing.

# TODO 3: Create active_students via .copy() and safely remove disqualified students
active_students = []


# ==============================================================================
# TASK 4: Class Performance Statistics & Formatted Report Card
# ==============================================================================
# 1. Compute summary statistics:
#    - 'total_evaluated' : total number of student records (len(STUDENT_RECORDS))
#    - 'class_average'   : sum of all scores divided by total evaluated (sum() / len())
#    - 'highest_score'   : maximum score in the class using max()
#    - 'lowest_score'    : minimum score in the class using min()
#
# 2. Print an aligned tabular report matching this format:
#    Column widths:
#    - STUDENT NAME : 18 characters, left-aligned  ({name:<18})
#    - SCORE        : 6 characters, right-aligned, 1 decimal place ({score:>6.1f})
#    - ATTENDANCE   : 11 characters, right-aligned, 1 decimal place ({attendance:>10.1f}%)
#    - GRADE        : 8 characters, right-aligned  ({grade:>8})
#    - STATUS       : 11 characters, right-aligned ({status:>11})
#
# 3. Print the summary block matching the format below:
#    - Total Evaluated Students
#    - Active Enrolled Students count and Disqualified count
#    - Class Average Score, Highest Score, Lowest Score
#    - Honor Roll Graduates list

print("=" * 66)
print("STUDENT PERFORMANCE & GRADEBOOK AUDIT REPORT")
print("=" * 66)
print(f"{'STUDENT NAME':<18}{'SCORE':>6}{'ATTENDANCE':>12}{'GRADE':>8}{'STATUS':>11}")
print("-" * 66)

# TODO 4: Loop over audit_table_rows and print each student row with formatted column widths

print("-" * 66)
print()
print("-" * 66)
print("CLASS PERFORMANCE SUMMARY")
print("-" * 66)

# TODO 4: Print class statistics, active student counts, and honor roll graduates

print("=" * 66)
