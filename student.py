students = []

def register_student():
    print("================================")
    print("----- STUDENT REGISTRATION -----")
    print("=================================")
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    password = input("Enter Password: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "phone": phone,
        "password": password}
    

    students.append(student)
    print("Student registered successfully!")


def view_students():
    print("===============================")
    print("----- REGISTERED STUDENTS -----")
    print("================================")
    if len(students) == 0:
        print("No students registered yet.")

    for item in students:
        print("Roll Number:", item["roll_no"])
        print("Name:", item["name"])
        print("Phone:", item["phone"])
        print()