import tkinter as tk
#Initialising all the constants in the program 
#PROGRAM CONSTANTS
#Uppercase names distinguish constants from normal variables
# Weekly training fees
TRAINING_FEES = {
    "Beginner": 25.00,
    "Intermediate": 30.00,
    "Elite": 35.00
}

# Additional fees 
COMPETITION_FEE = 22.00
COACHING_FEE = 9.50

# Competition weight categories and upper weight limits
WEIGHT_CATEGORIES = {
    "Heavyweight": float("inf"),
    "Light-Heavyweight": 100,
    "Middleweight": 90,
    "Light-Middleweight": 81,
    "Lightweight": 73,
    "Flyweight": 66
}

# Section 2: Store athlete records
#This dictionary stores all athletes  registered during the current program session
#They are not saved permanetly to a file or database
athlete_records = {}


# Section 3: ENROLLING A NEW ATHLETE
def enrol_athlete():
    print("\n--- Enrol a New Athlete ---")
     # strip() removes unnecessary spaces at the beginning and at the end of the name
     #upper() cases the name to uppercase
    athlete_name = input("Enter athlete name: ").strip().upper()

    if athlete_name == "":
        print("Athlete name cannot be empty.")
        return
     # Checks whether an athlete with this name already exists.
    # This prevents the same athlete from being registered twice.
    if athlete_name in athlete_records:
        print("This athlete is already registered.")
        return
    # Ask the user to choose one of the three available plans.
    print("\nTraining Plans: Beginner, Intermediate, Elite")
    training_plan = input("Enter training plan: ").strip().title()
    #check if the training plans typed is valid 
    if training_plan not in TRAINING_FEES:
        print("Invalid training plan.")
        return
    
    # Ask for the athlete's current weight in kilograms.
    # float() allows weights containing decimal places.
    try:
        current_weight_kg = float(input("Enter current weight in kg: "))
    # This message appears if the input cannot be converted into a numerical value.
    except ValueError:
        print("Please enter a valid weight.")
        return

    if current_weight_kg <= 0:
        print("Weight must be greater than zero.")
        return

    print("\nWeight Categories:")

    for category_name in WEIGHT_CATEGORIES:
        print(category_name)
     # Ask the user to select the athlete's intended competition weight category and capitalise the first letter
    competition_category = input(
        "Enter competition weight category: "
    ).strip().title()

    if competition_category not in WEIGHT_CATEGORIES:
        print("Invalid weight category.")
        return

    while True:
        try:
            weekly_coaching_hours = float(
                input("Enter weekly private coaching hours: ")
            )

            if weekly_coaching_hours < 0 or weekly_coaching_hours > 5:
                print("Please enter between 0 and 5 hours.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Store all details together under the athlete's name.
    athlete_records[athlete_name] = {
        "training_plan": training_plan,
        "current_weight_kg": current_weight_kg,
        "competition_category": competition_category,
        "weekly_coaching_hours": weekly_coaching_hours,
        "competitions_entered": 0
    }

    print("Athlete registered successfully!")

