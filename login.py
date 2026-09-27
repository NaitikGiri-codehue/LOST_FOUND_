import student

def login():
    print("----- STUDENT LOGIN -----")
    roll_no = input("Enter Roll Number: ")
    password = input("Enter Password: ")

    for item in student.students:
        if item["roll_no"] == roll_no and item["password"] == password:
            print("Login successful!")
            return item

    print("Wrong Roll Number or Password")
    return None