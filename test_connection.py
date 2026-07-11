from database import connect_database
con = connect_database()

if con:
    print("Connection Successful!")
    con.close()
    print("Connection Closed Successfully!")
else:
    print("Connection Failed!")

#Executing Insert query 

from database import execute_query

query = """
INSERT INTO users
(name, username, password, role, age, gender, height)
VALUES (%s,%s,%s,%s,%s,%s,%s)
"""

values = (
    "Test User",
    "test123",
    "pass123",
    "user",
    20,
    "Male",
    175
)

if execute_query(query, values):
    print("Inserted Successfully")

#Execute fetch query

from database import fetch_one

query = "SELECT * FROM users WHERE username=%s"

user = fetch_one(query, ("test123",))

print(user)

#Execute fetch all

from database import fetch_all

query = "SELECT * FROM users"

users = fetch_all(query)

for user in users:
    print(user["name"])
