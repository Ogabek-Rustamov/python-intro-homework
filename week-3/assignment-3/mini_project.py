day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day not in ["monday", "tuesday", "saturday"]:
    print("Sorry, I don't recognize that day. Try Monday, Tuesday, or Saturday.")

elif time not in ["morning", "afternoon", "evening"]:
    print("Sorry, I don't recognize that time. Try morning, afternoon, or evening.")

else:
    if day == "monday":
        if time == "morning":
            print("Suggestion: Plan your weekly goals.")
        elif time == "afternoon":
            print("Suggestion: Work on a Python exercise.")
        else:
            print("Suggestion: Read a book and relax.")

    elif day == "tuesday":
        if time == "morning":
            print("Suggestion: Attend your Python class.")
        elif time == "afternoon":
            print("Suggestion: Practice writing conditional statements.")
        else:
            print("Suggestion: Review what you learned today.")

    else:  # Saturday
        if time == "morning":
            print("Suggestion: Go for a walk.")
        elif time == "afternoon":
            print("Suggestion: Meet friends or explore a new place.")
        else:
            print("Suggestion: Watch a movie or try a new recipe.")
