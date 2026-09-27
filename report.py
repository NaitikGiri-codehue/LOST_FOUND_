items = []

def report_item(user):
    print("=======================")
    print("----- REPORT ITEM -----")
    print("=======================")
    print("1. Report Lost Item")
    print("2. Report Found Item")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter Item Name: ")
        category = input("Enter Category (Electronics/Books/ID Card/Other): ")
        location = input("Enter Location: ")

        if choice == 1:
            status = "Lost"

        item = {
            "item_id": len(items) + 1,
            "name": name,
            "category": category,
            "location": location,
            "status": status,
            "reported_by": user["name"],
            "claimed": False
        }

        items.append(item)
        print("====================================================")
        print("Okay , Your lost item has been reported succesfully!")
        print("====================================================")
    
    elif choice==2:
        name = input("Enter Item Name: ")
        category = input("Enter Category (Electronics/Books/ID Card/Other): ")
        location = input("Enter Location: ")
        if choice==2:
            status="Found"
        item = {
                "item_id": len(items) + 1,
                "name": name,
                "category": category,
                "location": location,
                "status": status,
                "reported_by": user["name"],
                "claimed": False
                }
        
        items.append(item)
        print("====================================================")
        print("Gotcha , Found item has been reported suucessfully!" )
        print("====================================================")
    else:
        print("==============================================")
        print("INVALID CHOICE,Enter the correct choice again!")
        print("==============================================")