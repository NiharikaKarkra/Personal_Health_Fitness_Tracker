"""auth.py"""
from database import fetch_one,execute_query
from calculations import is_valid_age
def login():
    username=input("Username: ").strip()
    password=input("Password: ").strip()
    q="SELECT * FROM users WHERE username=%s AND password=%s;"
    user=fetch_one(q,(username,password))
    if not user:
        print("Invalid username/password.")
        return None
    print(f"Welcome {user['name']}!")
    return user

def register():
    name=input("Name: ")
    username=input("Username: ")
    existing = fetch_one(
            "SELECT * FROM users WHERE username=%s;",
            (username,)
            )
    if existing:
        print("Username already exists.")
        return False
    
    password=input("Password: ")

    age=input("Age: ")
    
    if is_valid_age(age):
        print("Invalid age.")
        return False
    age = int(age)
    

    gender=input("Gender (Male/Female): ").title()
    if gender not in ("Male", "Female"):
        print("Invalid Gender.")
        return False
    
    height=float(input("Height(cm): "))
    try:
        height = float(height)
    except ValueError:
        print("Invalid height.")
        return False
   
    
    q="""INSERT INTO users(name,username,password,role,age,gender,height)
         VALUES(%s,%s,%s,'user',%s,%s,%s);"""
    ok=execute_query(q,(name,username,password,age,gender,height))
    print("Registration successful." if ok else "Registration failed.")
    return ok

def is_admin(user): return user and user.get("role")=="admin"

