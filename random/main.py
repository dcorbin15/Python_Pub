# Darius Corbin
# PA 6
# Date: 03/11/2023

#Instructions:
#Step 1: Select option 1 in the main menu and input a random name ex. John Doe
#Step 2: Repeat step 1 and enter a new gues name ex. Jane Doe
#Step 3: Explore menu features like removing guests, displaying guest table, sorting guest etc.

# create an empty list to store the guests
guest_list = []

# function to add a guest to the list
def add_guest(name, city, state, relation):
    if (name, city, state, relation) not in guest_list:
        guest_list.append((name, city, state, relation))
        print(name, "from", city + ", " + state, relation + "", "has been added to the guest list.")
    else:
        print(name, "from", city + ", " + state, relation + "", "is already on the guest list.")

# function to remove a guest from the list
def remove_guest(name):
    for guest in guest_list:
        if name in guest:
            guest_list.remove(guest)
            print(name, "has been removed from the guest list.")
            return
    print(name, "is not on the guest list.")

# function to display the guest list
def display_guests():
    if guest_list:
        print("Guest list:")
        print("+----+----------------------+----------------------+------------+------------+")
        print("| ID | Name                 | City                 | State      | Relation   |")
        print("+----+----------------------+----------------------+------------+------------+")
        for i, guest in enumerate(guest_list):
            name, city, state, relation = guest
            print(f"| {i+1:<2} | {name:<20} | {city:<20} | {state:<10} | {relation:<10} |")
        print("+----+----------------------+----------------------+------------+------------+")
    else:
        print("The guest list is empty.")

# function to sort the guest list
def sort_guests():
    guest_list.sort()
    print("Guest list has been sorted ALPHABETICALLY by first name.")

# function to edit a guest's information
def edit_guest(old_name, new_name, new_city, new_state, new_relation):
    for i, guest in enumerate(guest_list):
        if old_name in guest:
            guest_list[i] = (new_name, new_city, new_state, new_relation)
            print(old_name, "has been changed to", new_name, "from", new_city + ", " + new_state, new_relation + "")
            return
    print(old_name, "is not on the guest list.")

# prompt the user for action
while True:
    print("\n[MAIN MENU] What would you like to do?")
    print("1. Add a guest")
    print("2. Remove a guest")
    print("3. Display guest list")
    print("4. Sort guest list")
    print("5. Edit guest information")
    print("6. Quit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter the name(fname, lname) of the guest: ")
        city = input("Enter the city of origin: ")
        state = input("Enter the state of origin(initials): ")
        relation = input("Enter guest affiliation to either bride or groom:")
        add_guest(name, city, state, relation)
    elif choice == "2":
        name = input("Enter the name of the guest: ")
        remove_guest(name)
    elif choice == "3":
        display_guests()
    elif choice == "4":
        sort_guests()
    elif choice == "5":
        old_name = input("Enter the name of the guest you want to edit: ")
        new_name = input("Enter the new name (fname, lname) of the guest: ")
        new_city = input("Enter the new city of origin: ")
        new_state = input("Enter the new state of origin(initials): ")
        new_relation = input("Enter guest affiliation to either bride or groom:")
        edit_guest(old_name, new_name, new_city, new_state, new_relation)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
