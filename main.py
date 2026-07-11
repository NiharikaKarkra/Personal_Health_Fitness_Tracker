from auth import login, register, is_admin
from user import user_menu
from admin import admin_menu


while True:

    print("\n" + "=" * 40)
    print("PERSONAL HEALTH FITNESS TRACKER")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        register()

    elif choice == "2":

        user = login()

        if user:

            if is_admin(user):
                admin_menu()
            
            else:
                user_menu(user["user_id"])

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")