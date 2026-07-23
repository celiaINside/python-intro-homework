day = input("What day is it? ")
time = input("What time of day is it? ")

day = day.strip().lower()
time = time.strip().lower()

if day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "saturday" and day != "sunday":
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
elif time != "morning" and time != "afternoon" and time != "evening":
   print("Sorry, I don't recognize that time. Try: morning, afternoon, evening...")

if day == "friday" and time == "morning":
    print(f"Suggestion: Morning lesson work with a cup of coffee!")
elif day == "friday" and time == "afternoon":
    print(f"Suggestion: Afternoon lesson work with a cup of coffee!")
elif day == "friday" and time == "evening":
    print(f"Suggestion: Go for a walk around the neighborhood!")

if day == "saturday" and time == "morning":
    print(f"Suggestion: Morning lesson work with a cup of tea!")
elif day == "saturday" and time == "afternoon":
    print(f"Suggestion: Explore the city!")
elif day == "saturday" and time == "evening":
    print(f"Suggestion: Go out with friends tonight!")

if day == "sunday" and time == "morning":
    print(f"Suggestion: Read the news!")
elif day == "sunday" and time == "afternoon":
    print(f"Suggestion: Cook a great meal!")
elif day == "sunday" and time == "evening":
    print(f"Suggestion: Unwind with your favorite show!")