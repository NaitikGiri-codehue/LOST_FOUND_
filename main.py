import student
import login
import report
import claim
import display

user = None

while True:
    print("\n===== LOST AND FOUND SYSTEM =====")
    print("1. Register Student")
    print("2. Login")
    print("3. Report Item")
    print("4. Claim Item")
    print("5. View All Items")
    print("6. Search Item")
    print("7. Exit")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        student.register_student()
    elif choice == 2:
        user = login.login()
    elif user == None:
        print("Please login first!")
    elif choice == 3:
        report.report_item(user)
    elif choice == 4:
        claim.claim_item(report.items, user)
    elif choice == 5:
        display.show_all(report.items)
    elif choice == 6:
        display.search_item(report.items)
    elif choice==7:
        print("Thank You")
        break
    else:
        print("Invalid choice")