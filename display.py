def show_all(items):
    print("=====================")
    print("----- ALL ITEMS -----")
    print("=====================")
    for item in items:
        print(item["item_id"], "-", item["name"], "-", item["status"], "-", item["location"])


def search_item(items):
    print("=======================")
    print("----- SEARCH ITEM -----")
    print("=======================")
    keyword = input("Enter item name or category: ")

    for item in items:
        if keyword.lower() in item["name"].lower() or keyword.lower() in item["category"].lower():
            print(item["item_id"], "-", item["name"], "-", item["status"], "-", item["location"])