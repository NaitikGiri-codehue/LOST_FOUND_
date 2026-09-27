def claim_item(items, user):
    print("======================")
    print("----- CLAIM ITEM -----")
    print("======================")
    print("Found items:")
 
    for item in items:
        if item["status"] == "Found" and item["claimed"] == False:
            print(item["item_id"], "-", item["name"], "-", item["location"])
 
    item_id = int(input("Enter the item ID to claim: "))
 
    for item in items:
        if item["item_id"] == item_id:
            if item["claimed"] == True:
                print("This item is already claimed")
            else:
                item["claimed"] = True
                item["claimed_by"] = user["name"]
                print("Item claimed successfully!")
            return
 
    print("Item not found")
