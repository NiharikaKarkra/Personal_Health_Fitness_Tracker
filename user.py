from calculations import *
from database import fetch_all, fetch_one, execute_query
from reports import *

def user_menu(user_id):
    while True:
        print(f"\n" + "=" * 40)
        print("         User Panel")
        print("=" * 40)

        print("1. View My Profile")
        print("2. Update My Profile")
        print("3. Add Today's Health  Record")
        print("4. Update Today's Health Record")
        print("5. View My Health History")
        print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_profile(user_id)

        elif choice == "2":
            update_profile(user_id)
        
        elif choice == "3":
            add_record(user_id)

        elif choice == "4":
            update_record(user_id)

        elif choice == "5":
            view_history(user_id)

        elif choice == "6":
            print("Logging out...")
            break
        
        else:
            print("Invalid choice!")

#view profile
def view_profile(user_id):
    
    query = """
    SELECT 
        user_id, 
        name,
        username,
        role,
        age,
        gender,
        height
    FROM users
    WHERE user_id = %s;
    """

    user = fetch_one(query, (user_id,))

    if not user:
        print("\nUser not found.")
        input("\nPress Enter to continue...")
        return
    
    display_user(user)
    
    input("\nPress Enter to continue...")

#Update profile

def update_profile(user_id):
    
    query = """
    SELECT 
        user_id, 
        name,
        username,
        role,
        age,
        gender,
        height
    FROM users
    WHERE user_id = %s;
    """

    user = fetch_one(query, (user_id,))

    if not user:
        print("\nUser not found.")
        input("\nPress Enter to continue...")
        return
    
    display_user(user)

    print("""
        Select the field you want to update:-
          1. Name
          2. Age
          3. Gender
          4. Height
          5. Cancel
    """)

    choice = input("Enter the choice: ")

    if choice == "5":
        print("Update Cancelled.")
        input("\nPress Enter to continue...")
        return
    
    #Update Name
    elif choice == "1":
        new_name = input("Enter new name: ").strip()
        if not new_name:
            print("Name cannot be empty.")
            input("\nPress Enter to continue...")
            return
        query = """
        UPDATE users SET name = %s WHERE user_id = %s;
        """
        if(execute_query(query, (new_name, user_id))):
            print("Name Updated Successfully.")
        else:
            print("Update Failed")
        input("\nPress Enter to continue...")
    
    #Update age
    elif choice == "2":
        new_age = input("Enter new age: ")

        if not new_age.isdigit():
            print("Age must be a number.")
            input("\nPress Enter to continue...")
            return
        
        new_age = int(new_age)
        
        if new_age < 5 or new_age > 120:
            print("Unrealistic values!")
            input("\nPress Enter to continue...")
            return

        query = """
            UPDATE users SET age=%s WHERE user_id = %s;
        """
        if(execute_query(query, (new_age, user_id))):
            print("Age Updated Successfully.")
        else:
            print("Update Failed")
        input("\nPress Enter to continue...")

    #update gender
    elif choice == "3":
        new_gender = input("Enter Gender (Male/Female):").strip().title()

        if new_gender not in ("Male", "Female"):
            print("Please enter Male or Female.")
            input("\nPress Enter to continue...")
            return

        query = """
        UPDATE users SET gender=%s WHERE user_id=%s;
        """
        if(execute_query(query, (new_gender, user_id))):
            print("Gender Updated Successfully!")
        else:
            print("Update Failed")
        input("\nPress Enter to continue...")

    #Update height
    elif choice == "4":
        new_height = input("Enter new height (cm): ")
        try: 
            new_height = float(new_height)
        except ValueError:
            print("Height must be numeric.")
            input("\nPress Enter to continue...")            
            return

        if new_height < 50 or new_height >250:
            print("Height must be between 50 cm and 250 cm.")
            input("\nPress Enter to continue...")
            return
        
        query = """
        UPDATE users SET height=%s WHERE user_id=%s;
        """
        if(execute_query(query, (new_height, user_id))):
            print("Height Updated Successfully")
        else:
            print("Update Failed")
        input("\nPress Enter to continue...")
    
    else:
        print("Invalid choice.")
        input("\nPress Enter to continue...")


def add_record(user_id):
    query = '''
        SELECT * from daily_records WHERE user_id = %s AND record_date = CURDATE();
    '''

    record = fetch_one(query, (user_id,))

    if record:

        user = fetch_one(
            "SELECT age, gender, height FROM users WHERE user_id=%s;",
            (user_id,)
        )

        print("\nToday's record already exists.")

        display_analysis(
            record["weight"],
            record["steps"],
            user["height"],
            user["age"],
            user["gender"]
        )

        print("\nUse option 4 to update today's record.")

        input("\nPress Enter to continue...")
        return
               
    
    weight = input("Enter Weight(Kg): ")
    steps = input("Enter Steps: ")
    water = input("Enter Water Intake (L): ")
    sleep = input("Enter Sleep Hours: ")
    
    
    if not is_valid_weight(weight):
        print("Invalid weight.")
        input("\nPress Enter to continue...")
        return

    if not is_valid_steps(steps):
        print("Invalid steps.")
        input("\nPress Enter to continue...")
        return

    if not is_valid_water(water):
        print("Invalid water intake.")
        input("\nPress Enter to continue...")
        return

    if not is_valid_sleep(sleep):
        print("Invalid sleep hours.")
        input("\nPress Enter to continue...")
        return
    
    weight = float(weight)
    steps = int(steps)
    water = float(water)
    sleep = float(sleep)

    query = """
    INSERT INTO daily_records
    (
        user_id,
        record_date,
        weight,
        steps,
        water,
        sleep
    )
    VALUES
    (
        %s,
        CURDATE(),
        %s,
        %s,
        %s,
        %s
    )
    """

    success = execute_query(
        query,
        (
            user_id,
            weight,
            steps,
            water,
            sleep
        )
    )

    if not success:
        print("\nFailed to save record.")
        input("\nPress Enter to continue...")
        return
    
    query = '''
    SELECT age, gender, height FROM users WHERE user_id = %s;
    '''
    user = fetch_one(query, (user_id,))

    display_analysis(weight, steps, user["height"], user["age"], user["gender"])
    input("\nPress Enter to continue...")

    

def update_record(user_id):

    query = """
        SELECT *
        FROM daily_records
        WHERE user_id = %s
        AND record_date = CURDATE();
        """

    record = fetch_one(query, (user_id,))

    if not record:
        print("\nToday's record not found.")
        print("Please add today's record first.")
        input("\nPress Enter to continue...")
        return

    print("\nCurrent Record")
    print("-" * 40)
    print(f"Weight : {record['weight']} kg")
    print(f"Steps  : {record['steps']}")
    print(f"Water  : {record['water']} L")
    print(f"Sleep  : {record['sleep']} hrs")
    print("-" * 40)

    weight = input("Enter New Weight (Kg): ")
    steps = input("Enter New Steps: ")
    water = input("Enter New Water Intake (L): ")
    sleep = input("Enter New Sleep Hours: ")

    if not is_valid_weight(weight):
        print("Invalid Weight.")
        input("\nPress Enter to continue...")
        return

    if not is_valid_steps(steps):
        print("Invalid Steps.")
        input("\nPress Enter to continue...")
        return

    if not is_valid_water(water):
        print("Invalid Water Intake.")
        input("\nPress Enter to continue...")
        return

    if not is_valid_sleep(sleep):
        print("Invalid Sleep Hours.")
        input("\nPress Enter to continue...")
        return

    weight = float(weight)
    steps = int(steps)
    water = float(water)
    sleep = float(sleep)

    query = """
    UPDATE daily_records
    SET
        weight = %s,
        steps = %s,
        water = %s,
        sleep = %s
    WHERE
        user_id = %s
    AND
        record_date = CURDATE();
    """

    success = execute_query(
        query,
        (
            weight,
            steps,
            water,
            sleep,
            user_id
        )
    )

    if not success:
        print("\nFailed to update record.")
        input("\nPress Enter to continue...")
        return

    user = fetch_one(
        "SELECT age, gender, height FROM users WHERE user_id=%s;",
        (user_id,)
    )

    display_analysis(
        weight,
        steps,
        user["height"],
        user["age"],
        user["gender"]
    )

    input("\nPress Enter to continue...")

def view_history(user_id):

    query = """
    SELECT
        record_date,
        weight,
        steps,
        water,
        sleep
    FROM daily_records
    WHERE user_id = %s
    ORDER BY record_date DESC;
    """

    records = fetch_all(query, (user_id,))

    if not records:
        print("\nNo health records found.")
        input("\nPress Enter to continue...")
        return
    
    steps_list = []
    weight_list = []

    for record in records:

        print("-" * 40)
        print("Record History: ")
        print(f"Date   : {record['record_date']}")
        print(f"Weight : {record['weight']} kg")
        print(f"Steps  : {record['steps']}")
        print(f"Water  : {record['water']} L")
        print(f"Sleep  : {record['sleep']} hrs")
        print("-" * 40)

        steps_list.append(record["steps"])
        weight_list.append(record["weight"])

    query = """
        SELECT height FROM users WHERE user_id =%s
    """

    user = fetch_one(query, (user_id,))
    
    latest_weight = records[0]["weight"]
    bmi = calculate_bmi(latest_weight, user["height"])
    category = get_bmi_category(bmi)
    
    display_summary(
        steps_list,
        weight_list,
        bmi,
        category
    )
    input("\nPress Enter to continue...")


def display_user(user):

    print("-" * 40)
    print(f"User ID  : {user['user_id']}")
    print(f"Name     : {user['name']}")
    print(f"Username : {user['username']}")
    print(f"Role     : {user['role']}")
    print(f"Age      : {user['age']}")
    print(f"Gender   : {user['gender']}")
    print(f"Height   : {user['height']} cm")
    print("-" * 40)