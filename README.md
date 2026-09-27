# 🔗 LOST AND FOUND COLLEGE MANAGEMENT SYSTEM

## 🔗 ABOUT THE PROJECT

The Lost and Found College Management System is a simple Python project made to help students report and manage lost and found items inside a college campus.

In college, students may lose things like wallets, ID cards, books, bags, keys, earphones, or other personal items. Finding these items can sometimes be difficult because there is no proper place to report or search for them.

This project provides a simple system where students can report lost items, enter information about found items, search for records, and claim an item.

The project is made using basic Python concepts such as functions, lists, dictionaries, conditional statements, loops, and modules.

## 🔗 OBJECTIVES

The main objectives of this project are:

* To maintain records of lost items.
* To maintain records of found items.
* To make searching for items easier.
* To allow students to provide information about lost belongings.
* To provide a simple claiming process.
* To display useful information about reported items.
* To organize the complete process in different Python files.

## 🔗 FEATURES

The system includes the following features:

1. Student Login
2. Report Lost Item
3. Report Found Item
4. Display Lost and Found Items
5. Search for Items
6. Claim an Item
7. Generate Simple Reports
8. Manage student information

The system is designed to be simple enough for beginners to understand and modify.

## 🔗 PROJECT FILES

The project is divided into different Python files.

```text
Lost and Found Management System
│
├── main.py
├── login.py
├── student.py
├── report.py
├── display.py
└── claim.py
```

### 🔗 main.py

This is the main file of the project.

It controls the overall flow of the program and connects the different modules together.

The user can select different options from the main menu.

### 🔗 login.py

This file handles the login part of the system.

It takes the required student information and checks the login details before allowing the user to use the system.

### 🔗 student.py

This module is used for handling student-related information.

It stores basic details of students who use the system.

### 🔗 report.py

This module is used to report lost or found items.

The user can enter details such as:

* Item name
* Category
* Location
* Date
* Description
* Student name
* Contact information

### 🔗 display.py

This module displays the available lost and found item records.

It helps the user view the items that have already been reported.

### 🔗 claim.py

This module handles the claiming process.

If a student finds an item that belongs to them, they can provide the required information to claim it.

## 🔗 HOW THE SYSTEM WORKS

The basic working of the system is:

```text
Start
  |
  v
Login
  |
  v
Main Menu
  |
  +---- Report Lost Item
  |
  +---- Report Found Item
  |
  +---- Display Items
  |
  +---- Search Items
  |
  +---- Claim Item
  |
  +---- Generate Report
  |
  v
Exit
```

The user first enters the system through the login section. After login, the main menu is displayed.

From the menu, the user can select the required operation. Each operation is handled by a separate Python module.

## 🔗 EXAMPLE OF A LOST ITEM

```text
Item Name: Black Wallet
Category: Personal
Location: Library
Date: 15-09-2026
Description: Black leather wallet
Student Name: Rahul
Contact: 9876543210
Status: Lost
```

The information is stored in the program and can later be displayed or searched.

## 🔗 EXAMPLE OF A FOUND ITEM

```text
Item Name: Blue Water Bottle
Category: Personal
Location: Block 2
Date: 16-09-2026
Description: Blue bottle found near classroom
Student Name: Aman
Contact: 9876543210
Status: Found
```

This record can later be checked by students who have lost a similar item.

## 🔗 PYTHON CONCEPTS USED

The project mainly uses basic Python concepts that are useful for beginners.

* Variables
* Input and output
* If-else statements
* For loops
* While loops
* Lists
* Dictionaries
* Functions
* Modules
* Conditional statements
* Basic searching
* Menu-driven programming

No complicated libraries or advanced programming concepts are required.

## 🔗 REQUIREMENTS

To run this project, you need:

* Python 3
* VS Code or any Python-supported IDE
* Basic knowledge of running Python programs

No external Python libraries are required.

## 🔗 HOW TO RUN THE PROJECT

1. Download or clone the project.
2. Open the project folder in VS Code.
3. Make sure all Python files are in the same folder.
4. Open `main.py`.
5. Run the program.
6. Use the menu displayed in the terminal.

Example:

```text
===== LOST AND FOUND SYSTEM =====

1. Login
2. Report Lost Item
3. Report Found Item
4. Display Items
5. Claim Item
6. Report
7. Exit

Enter your choice:
```

Enter the number according to the operation you want to perform.

## 🔗 ADVANTAGES

The system provides a simple way to manage lost and found items in a college.

Some advantages are:

* Easy to use
* Simple menu-based system
* Easy to understand for beginners
* Keeps lost and found information organized
* Makes searching easier
* Separates the program into different modules
* Can be modified and improved easily

## 🔗 LIMITATIONS

This project is mainly created as a beginner-level Python project, so it has some limitations.

* The system does not use a database.
* Data is mainly handled during program execution.
* The project does not have a graphical user interface.
* It is designed for basic college-level use.
* It does not provide online access.
* Multiple users cannot use the system at the same time.

## 🔗 FUTURE IMPROVEMENTS

The project can be improved in the future by adding:

* Database connectivity
* Graphical user interface
* Student registration
* Admin login
* Better search options
* Email notifications
* Automatic matching of lost and found items
* Online access
* Item image upload
* Better claim verification
* Permanent storage of records

## 🔗 PROJECT PURPOSE

This project was created as a beginner-friendly Python project to understand how different programming concepts can be combined to build a small real-world application.

Instead of keeping the whole program in one file, the project is divided into different modules. This makes the code easier to understand, manage, and update.

The main idea is to create a simple system that could be useful in a college environment while also helping students understand practical Python programming.

## 🔗 CONCLUSION

The Lost and Found College Management System provides a basic solution for managing lost and found items within a college campus.

The project demonstrates how Python concepts such as functions, lists, dictionaries, loops, conditions, and modules can be used together to create a practical application.

Although the current version is simple, it provides a good base for adding more features and developing the project into a larger management system.

## 🔗 AUTHOR
Name--Naitik Nishchal Giri
Course--B.Tech Computer Science Engineering
University--VIT Bhopal
Created as a college Python project.

This project is developed for learning and academic purposes.


