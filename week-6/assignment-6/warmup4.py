def is_valid_score(score):
    if isinstance(score, int) and 0 <= score <= 100:
        return True
    else: 
        return False

score = int(input("Enter a score: "))

if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")