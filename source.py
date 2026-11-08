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
# PRELOADED ATHLETE RECORDS
# These records are available when the program starts.
# They are stored in memory for the current session.

athlete_records = {
    "AHMAD BELLO TOMIWA": {
        "training_plan": "Beginner",
        "current_weight_kg": 68.0,
        "competition_category": "Lightweight",
        "weekly_coaching_hours": 1.0,
        "competitions_entered": 0
    },

    "AISHA YUSUF": {
        "training_plan": "Intermediate",
        "current_weight_kg": 70.0,
        "competition_category": "Lightweight",
        "weekly_coaching_hours": 2.0,
        "competitions_entered": 1
    },

    "HALIAH POPOOLA": {
        "training_plan": "Elite",
        "current_weight_kg": 85.0,
        "competition_category": "Middleweight",
        "weekly_coaching_hours": 3.0,
        "competitions_entered": 2
    },

    "MARYAM BELLO": {
        "training_plan": "Beginner",
        "current_weight_kg": 60.0,
        "competition_category": "Flyweight",
        "weekly_coaching_hours": 0.0,
        "competitions_entered": 0
    },

    "SAMUEL ADE": {
        "training_plan": "Intermediate",
        "current_weight_kg": 78.0,
        "competition_category": "Light-Middleweight",
        "weekly_coaching_hours": 1.5,
        "competitions_entered": 2
    },

    "ZARA IBRAHIM": {
        "training_plan": "Elite",
        "current_weight_kg": 95.0,
        "competition_category": "Light-Heavyweight",
        "weekly_coaching_hours": 2.0,
        "competitions_entered": 3
    }
}



# Section 3: ENROLLING A NEW ATHLETE

def enrol_athlete():
    print("\n--- Enrol a New Athlete ---")

    # strip() removes unnecessary spaces at the beginning and at the end of the name
    # upper() cases the name to uppercase
    while True:
        athlete_name = input("Enter athlete name: ").strip().upper()

        if athlete_name == "":
            print("Athlete name cannot be empty.")
        else:
            break

    # Checks whether an athlete with this name already exists.
    # This prevents the same athlete from being registered twice.
    if athlete_name in athlete_records:
        print("This athlete is already registered.")
        return

    # Ask the user to choose one of the three available plans.
    print("\nTraining Plans: Beginner, Intermediate, Elite")

    # check if the training plans typed is valid
    while True:
        training_plan = input("Enter training plan: ").strip().title()

        if training_plan in TRAINING_FEES:
            break

        print("Invalid training plan. Please try again.")

    # Ask for the athlete's current weight in kilograms.
    # float() allows weights containing decimal places.
    while True:
        try:
            current_weight_kg = float(input("Enter current weight in kg: "))

            if current_weight_kg > 0:
                break

            print("Weight must be greater than zero.")

        # This message appears if the input cannot be converted into a numerical value.
        except ValueError:
            print("Please enter a valid weight.")

    print("\nWeight Categories:")

    for category_name in WEIGHT_CATEGORIES:
        print(category_name)

    # Ask the user to select the athlete's intended competition weight category and capitalise the first letter
    while True:
        competition_category = input(
            "Enter competition weight category: "
        ).strip().title()

        if competition_category in WEIGHT_CATEGORIES:
            break

        print("Invalid weight category. Please try again.")

    # This while true loop ensures that the loop doesn't end until the user enters an appropriate number
    while True:
        try:
            weekly_coaching_hours = float(
                input("Enter weekly private coaching hours: ")
            )

            if weekly_coaching_hours < 0 or weekly_coaching_hours > 5:
                print("Please enter between 0 and 5 hours.")
            else:
                break

        # The error message needs to be descriptive and useful hence the value error for invalid input
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



# VIEW REGISTERED ATHLETES

def view_athletes():
    print("\n--- Registered Athletes ---")

    if not athlete_records:
        print("No athletes have been registered.")
        return
 #All the athlete's details are printed out 
    for athlete_name, athlete_details in athlete_records.items():
        print("\nAthlete:", athlete_name)
        print("Training Plan:", athlete_details["training_plan"])
        print("Current Weight:", athlete_details["current_weight_kg"], "kg")
        print("Weight Category:", athlete_details["competition_category"])
        print("Coaching Hours:", athlete_details["weekly_coaching_hours"])
        print("Competitions:", athlete_details["competitions_entered"])


# UPDATE ATHLETE INFORMATION
def update_athlete():
    print("\n--- Update Athlete ---")
    athlete_name = input("Enter athlete name: ").strip().upper()

    if athlete_name not in athlete_records:
        print("Athlete not found.")
        return
    print("1. Training Plan")
    print("2. Current Weight")
    print("3. Competition Weight Category")
    print("4. Private Coaching Hours")

    update_option = input("Choose the detail to update: ")

    if update_option == "1":
        updated_training_plan = input(
            "Enter new training plan: "
        ).strip().title()

        if updated_training_plan in TRAINING_FEES:
            #The updated training plan is being stored in the actaul training plan to ensure consistency of data 
            athlete_records[athlete_name]["training_plan"] = updated_training_plan
            print("Training plan updated.")
        else:
            print("Invalid training plan.")

    elif update_option == "2":

        while True:
            try:
                updated_weight_kg = float(
                    input("Enter new weight: ")
                )

                if updated_weight_kg > 0:
                    athlete_records[athlete_name]["current_weight_kg"] = updated_weight_kg
                    print("Weight updated.")
                    break

                print("Weight must be greater than zero.")

            except ValueError:
                print("Please enter a valid weight.")

    elif update_option == "3":
        updated_category = input(
            "Enter new competition weight category: "
        ).strip().title()

        if updated_category in WEIGHT_CATEGORIES:
            athlete_records[athlete_name]["competition_category"] = updated_category
            print("Weight category updated.")
        else:
            print("Invalid weight category.")

    elif update_option == "4":
        while True:
            try:
                updated_coaching_hours = float(
                    input("Enter new coaching hours: ")
                )

                if updated_coaching_hours >= 0 and updated_coaching_hours <= 5:
                    athlete_records[athlete_name]["weekly_coaching_hours"] = updated_coaching_hours
                    print("Coaching hours updated.")
                    break
                else:
                    print("Hours cannot be negative or greater than 5.")
                    updated_coaching_hours = float(
                                        input("Enter new coaching hours: ")
                                    )

            except ValueError:
                print("Please enter a valid number.")
                updated_coaching_hours = float(
                                    input("Enter new coaching hours: ")
                                )

    else:
        print("Invalid option.")

# REMOVING AN ATHLETE

def remove_athlete():
    print("\n--- Remove Athlete ---")

    athlete_name = input("Enter athlete name: ").strip().upper()

    if athlete_name in athlete_records:
        #seeks confirmation from user before deleting athlete 
        confirmation = input(f"Are you sure you'd like to remove{athlete_name}").lower()
        if confirmation == "yes":    
            del athlete_records[athlete_name]
            #outputs a success message so user knows that the athlete has been removed
            print("Athlete removed successfully.")
        else:
            print("Removal cancelled")
            return
    else:
        print("Athlete not found.")

# ENTER COMPETITIONS

def enter_competitions():
    print("\n--- Enter Competitions ---")

    athlete_name = input("Enter athlete name: ").strip().upper()

    if athlete_name not in athlete_records:
        print("Athlete not found.")
        return

    athlete_details = athlete_records[athlete_name]
    #Only Elite and Intermediate athlete can enter competition, the if loop is to filter out beginner athletes
    if athlete_details["training_plan"] not in ["Intermediate", "Elite"]:
        print("Beginners cannot enter competitions.")
        return

    while True:
        try:
            competitions_entered = int(
                input("Enter number of competitions this month: ")
            )
            #continue is used after both error messages so that the program can exit the current loop and start the next one prompting
            #the user to enter the correct value.
        except ValueError:
            print("Please enter a whole number.")
            continue 

        if competitions_entered < 0:
            print("The number cannot be negative.")
            continue

        athlete_details["competitions_entered"] = competitions_entered
        print("Competition entries updated.")
        break

# Section 8: Generate monthly cost report

def generate_monthly_report():
    print("\n--- Monthly Cost Report ---")

    athlete_name = input("Enter athlete name: ").strip()

    if athlete_name not in athlete_records:
        print("Athlete not found.")
        return

    athlete_details = athlete_records[athlete_name]
    #The weekly training fee is a fixed cost depending on the athletes training plan 
    weekly_training_fee = TRAINING_FEES[athlete_details["training_plan"]]

   #This varies depending on the number of competitions entered but the base price is a constant
    competition_cost = (
        athlete_details["competitions_entered"] *  COMPETITION_FEE
    )

   #The coaching cost is the base coaching fee multiplied by the number of private coaching hours
    coaching_cost = (
        athlete_details["weekly_coaching_hours"] * COACHING_FEE
    )
    #  There are four weeks in a month so we multiply the fee by 4
    training_cost = weekly_training_fee * 4

    total_monthly_cost = (
        training_cost + competition_cost + coaching_cost
    )

    print("\nAthlete:", athlete_name)
    print("Training Cost: £{:.2f}".format(training_cost))
    print("Competition Cost: £{:.2f}".format(competition_cost))
    print("Private Coaching Cost: £{:.2f}".format(coaching_cost))
    print("Total Monthly Cost: £{:.2f}".format(total_monthly_cost))

    selected_category = athlete_details["competition_category"]
    current_weight_kg = athlete_details["current_weight_kg"]
    category_upper_limit_kg = WEIGHT_CATEGORIES[selected_category]
    #This is to help the user know if an athlete needs more training
    if current_weight_kg <= category_upper_limit_kg:
        print("Weight is within the selected competition category.")
    else:
        print("Weight is above the selected competition category limit.")


# SECTION: MAIN MENU
def main_menu():
    while True:
        print("\n===== NORTH SUSSEX JUDO =====")
        print("1. Register New Athlete")
        print("2. View Athletes")
        print("3. Update Athlete Information")
        print("4. Remove Athlete")
        print("5. Enter Competitions")
        print("6. Generate Monthly Cost Report")
        print("7. Exit Program")


        choice = input("Choose an option: ")

        if choice == "1":
            enrol_athlete()
        elif choice == "2":
            view_athletes()
        elif choice == "3":
            update_athlete()
        elif choice == "4":
            remove_athlete()
        elif choice == "5":
            enter_competitions()
        elif choice == "6":
            generate_monthly_report()
        elif choice == "7":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")




main_menu()


