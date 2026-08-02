students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

#find the top scorer
highest_score = 0

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]

top_scorer = []
for student in students:
    if student["score"] == highest_score:
        top_scorer.append(student["name"])
#print(top_scorer)

# find class average
total_of_scores = 0
for student in students:
    total_of_scores += student["score"]
average = total_of_scores / len(students)
print(f"Class average: {average}")

# List all unique subjects — use a set to collect subjects as you loop, then print them.
unique_subjects = set()
for student in students:
    unique_subjects.add(student["subject"])
print(unique_subjects)

# find high scores (above 75)
high_scores = []
for student in students:
    if student["score"] > 75:
        high_scores.append(student["name"])
print(high_scores)

#print section
print(f"Top scorer: {', '.join(top_scorer)} ({highest_score})")
print(f"Class average: {average:.1f}")
print(f"Subjects offered: {unique_subjects}")
print(f"High scorers: {high_scores}")