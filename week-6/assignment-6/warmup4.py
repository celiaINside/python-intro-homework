def is_valid_score(score):
    try:
        score = int(score)
        return 0 <= score <= 100
    except ValueError:
        return False

score = input("Enter a score: ")

if is_valid_score(score) == True:
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")