from database import fetch_all, fetch_one, execute_query

#Display Admin Menu

def admin_menu():
    while True:
        print("\n" + "=" * 40)
        print("              ADMIN PANEL")
        print('=' * 40)

        print("1. View All Users")
        print("2. Search User")
        print("3. Delete User")
        print("4. View Daily Records")
        print("5. Logout")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            view_all_users()

        elif choice == "2":
            search_user()

        elif choice == "3":
            delete_user()

        elif choice == "4":
            view_daily_records()

        elif choice == "5":
            print("Logging out... ")
            break
        
        else:
            print("Invalid Choice!")

#View All Users

def view_all_users():
    
    query = """
    Select 
        user_id,
        name,
        username,
        role,
        age,
        gender,
        height
    From users;
    """    

    users = fetch_all(query)

    if not users:
        print("\nNo users found.")
        input("\nPress Enter to continue...")
        return

    for user in users:
        display_user(user)
    input("\nPress Enter to return to admin menu...")

# Search User

def search_user():
    
    print("""

        Search User
          1. By User ID
          2. By Username
          3. By Name
          4. Back to Admin Menu
    """)

    choice = input("\nEnter your choice: ")

#Search user by ID

    if choice == "1":
        user_id = input("Enter User ID: ")
        query = """
        SELECT * FROM users WHERE user_id = %s;
        """
        user = fetch_one(query, (user_id,))

        if user:
                display_user(user)
        else:
                print("User not found.")
            
        input("\nPress Enter to continue...")

#Search user by username

    elif choice == "2":
        username = input("Enter Username: ")
        query = """
        SELECT * FROM users WHERE username = %s;
        """
        user = fetch_one(query, (username,))

        if user:
                display_user(user)
        else:
                print("User not found.")
    
        input("\nPress Enter to continue...")

#Search user by name

    elif choice == "3":
        name = input("Enter Name: ")
        query = """
        SELECT * FROM users WHERE name LIKE %s;
        """
        users = fetch_all(query, (f"%{name}%",))

        if users:
            for user in users:
                display_user(user)
        else:
            print("User not found.")
        
        input("\nPress Enter to continue...")
    
    else:
        print("Returning to Admin Menu...")
        return

# deleting user

def delete_user():
    
    #check whether user is present or not

    user_id = input("Enter User ID to delete: ")
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
        print(f"User with ID {user_id} not found.")
        input("\nPress Enter to continue...")
        return
    
    else:
        display_user(user)

    #check whther user is admin or not, if yes then do not delete
    if user["role"] == "admin":
        print("\nAdministrator account cannot be deleted.")
        input("\nPress Enter to continue...")
        return

    while True:
        confirm = input("\nAre you sure you want to delete this user? (Y/N): ").strip().upper()

        if confirm in ("Y", "N"):
            break
        print("Invalid input. Please enter only Y or N.")
             
    #if user confirms deletion, then delete the user from database    
    if confirm != 'Y':
            print("Deletion cancelled.")
            input("\nPress Enter to continue...")
            return
        
    delete_query = "DELETE FROM users WHERE user_id = %s;"
        
    if execute_query(delete_query, (user_id,)):
            print(f"User with ID {user["name"]} has been deleted.")
    else:
            print("Failed to delete user.")

    input("\nPress Enter to continue...")

# Daily Records Table

def view_daily_records():
    
    query = """
    SELECT 
        u.user_id,
        u.name,
        d.record_date,
        d.weight,
        d.steps,
        d.water,
        d.sleep
    FROM users u
    JOIN daily_records d
        ON u.user_id = d.user_id
    ORDER BY d.record_date DESC, u.name;
    """

    records = fetch_all(query)

    if not records:
         print("\nNo record found.")
         input("\nPress Enter to continue...")
         return
    
    for record in records:
         display_daily_record(record)

    input("\n Press Enter to continue...")

def display_user(user):

    print("-" * 40)
    print(f"User ID  : {user['user_id']}")
    print(f"Name     : {user['name']}")
    print(f"Username : {user['username']}")
    print(f"Role     : {user['role']}")
    print(f"Age      : {user['age']}")
    print(f"Gender   : {user['gender']}")
    print(f"Height   : {user['height']}")
    print("-" * 40)

def display_daily_record(record):
     
    print("-" * 40)
    print(f"User ID     : {record['user_id']}")
    print(f"Name        : {record['name']}")
    print(f"Date        : {record['record_date']}")
    print(f"Weight      : {record['weight']} kg")
    print(f"Steps       : {record['steps']}")
    print(f"Water       : {record['water']} L")
    print(f"Sleep       : {record['sleep']} hrs")
    print("-" * 40)

if __name__ == "__main__":
    admin_menu()