day = input("What day is it? ")
time = input("What time of day is it? ")

day = day.strip().lower()
time = time.strip().lower()

if day!= "friday" and day!= "saturday" and day != "sunday": 
    print("Sorry, we only recognize weekend days here.")
elif time != "morning" and time != "afternoon" and time != "night":
    print("Sorry, try a time of day like morning, afternoon, or night.")

if day == "friday" and time == "morning":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Morning lesson work with a cup of coffee!")
if day == "friday" and time == "afternoon":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Afternoon lesson work with a cup of coffee!")
if day == "friday" and time == "night":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Go for a walk around the neighborhood!")

if day == "saturday" and time == "morning".lower():
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Morning lesson work with a cup of tea!")
if day == "saturday" and time == "afternoon":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Explore the city!")
if day == "saturday" and time == "night":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Go out with friends tonight!")

if day == "sunday" and time == "morning":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Read the news!")
if day == "sunday" and time == "afternoon":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Cook a great meal!")
if day == "sunday" and time == "night":
    print(f"What day is it? {day}")
    print(f"What time of day? {time}")
    print(f"Suggestion: Unwind with your favorite show!")