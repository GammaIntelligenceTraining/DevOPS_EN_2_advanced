STUDENT_RECORDS = [
    {"name": "Alice", "score": 85, "subject": "Math"},
    {"name": "Bob", "score": 55, "subject": "History"},
    {"name": "Charlie", "score": 92, "subject": "Science"},
    {"name": "Diana", "score": 45, "subject": "Math"},
    {"name": "Eve", "score": 78, "subject": "History"},
    {"name": "Frank", "score": 30, "subject": "Science"},
    {"name": "Grace", "score": 40, "subject": "Math"}
]

for s in STUDENT_RECORDS:
    print(f"Hello {s["name"]}. Your score is {s["score"]}")

print(s)