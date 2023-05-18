#Sales and inventory management app for a house sales busines

# create a list to store the inventory
inventory = []

# function to add a new house to the inventory
def add_house():
    # get the house details from the user
    house_id = input("Enter the house ID: ")
    house_type = input("Enter the house type: ")
    house_price = input("Enter the house price: ")
    house_status = input("Enter the house status: ")
    # create a list of the house details
    house_details = [house_id, house_type, house_price, house_status]
    # add the house details to the inventory
    inventory.append(house_details)
    # display a message to the user
    print("House added to the inventory")

# function to remove a house from the inventory
def remove_house():
    # get the house ID from the user
    house_id = input("Enter the house ID: ")
    # loop through the inventory
    for house in inventory:
        # check if the house ID is in the inventory
        if house[0] == house_id:
            # remove the house from the inventory
            inventory.remove(house)
            # display a message to the user
            print("House removed from the inventory")
            # return the house details
            return house
    # display a message to the user
    print("House not found")

# function to update a house in the inventory
def update_house():
    # get the house ID from the user
    house_id = input("Enter the house ID: ")
    # loop through the inventory
    for house in inventory:
        # check if the house ID is in the inventory
        if house[0] == house_id:
            # get the house details from the user
            house_type = input("Enter the house type: ")
            house_price = input("Enter the house price: ")
            house_status = input("Enter the house status: ")
            # update the house details
            house[1] = house_type
            house[2] = house_price
            house[3] = house_status
            # display a message to the user
            print("House updated")
            # return the house details
            return house
    # display a message to the user
    print("House not found")
# function to display the inventory
def display_inventory():
    # display the inventory to the user
    print(inventory)

# function to search for a house in the inventory
def search_house():
    # get the house ID from the user
    house_id = input("Enter the house ID: ")
    # loop through the inventory
    for house in inventory:
        # check if the house ID is in the inventory
        if house[0] == house_id:
            # display the house details
            print(house)
            # display a message to the user
            print("House found")
            # return the house details
            return house
    # display a message to the user
    print("House not found")

# function to display the menu to the user until the user quits
def menu():
    # create a variable to store the user's choice
    choice = 0
    # loop until the user quits
    while choice != 5:
        # display the menu to the user
        print("1. Add a house")
        print("2. Remove a house")
        print("3. Update a house")
        print("4. Search for a house")
        print("5. Show inventory")
        print("6. Quit")
        # get the user's choice
        choice = int(input("Enter your choice: "))
        # check if the user's choice is 1
        if choice == 1:
            # call the add_house function
            add_house()
        # check if the user's choice is 2
        elif choice == 2:
            # call the remove_house function
            remove_house()
        # check if the user's choice is 3
        elif choice == 3:
            # call the update_house function
            update_house()
        # check if the user's choice is 4
        elif choice == 4:
            # call the search_house function
            search_house()
        # check if the user's choice is 5
        elif choice == 5:
            # display a message to the user
            display_sold_houses()
        # check if the user's choice is 6
        elif choice == 6:
            # display a message to the user
            print("Goodbye")
        # check if the user's choice is not 1, 2, 3, 4 or 5
        else:
            # display a message to the user
            print("Invalid choice")

#create a list to store the sold houses and who sold them
sold_houses = []

#function to sell a house
def sell_house(username):
    # get the house ID from the user
    house_id = input("Enter the house ID: ")
    # loop through the inventory
    for house in inventory:
        # check if the house ID is in the inventory
        if house[0] == house_id:
            # remove the house from the inventory
            inventory.remove(house)
            # add house to the sold houses list along with who sold it
            sold_houses.append(house + ["Sold by " + username])
            # display a message to the user
            print("House sold")
            # return the house details
            return house
    # display a message to the user
    print("House not found")

#function to display the sold houses
def display_sold_houses():
    # display the sold houses to the user
    print(sold_houses)

#function to search for a sold house
def search_sold_house():
    # get the house ID from the user
    house_id = input("Enter the house ID: ")
    # loop through the sold houses
    for house in sold_houses:
        # check if the house ID is in the sold houses
        if house[0] == house_id:
            # display the house details
            print(house)
            # display a message to the user
            print("House found")
            # return the house details
            return house
    # display a message to the user
    print("House not found")

#function to display the menu to the user until the user quits
def menuSalesman(username):
    # create a variable to store the user's choice
    choice = 0
    # loop until the user quits
    while choice != 4:
        # display the menu to the user
        print("1. Sell a house")
        print("2. Display sold houses")
        print("3. Search for a sold house")
        print("4. Quit")
        # get the user's choice
        choice = int(input("Enter your choice: "))
        # check if the user's choice is 1
        if choice == 1:
            # call the sell_house function
            sell_house(username)
        # check if the user's choice is 2
        elif choice == 2:
            # call the display_sold_houses function
            display_sold_houses()
        # check if the user's choice is 3
        elif choice == 3:
            # call the search_sold_house function
            search_sold_house()
        # check if the user's choice is 4
        elif choice == 4:
            # display a message to the user
            print("Goodbye")
        # check if the user's choice is not 1, 2, 3 or 4
        else:
            # display a message to the user
            print("Invalid choice")

# function to log into the system as a regular user or an admin
def login():
    # get the user's username
    username = input("Enter your username: ")
    # get the user's password
    password = input("Enter your password: ")
    # check if the user's username is admin and the user's password is admin
    if username == "admin" and password == "admin":
        # display a message to the user
        print("Welcome admin")
        # call the menu function
        menu()
    # check if the user's username is not admin and the user's password is not admin
    elif username == "salesman" and password == "salesman":
        # display a message to the user
        print("Welcome " + username)
        # call the menu function
        menuSalesman(username)
    # check if the user's username is admin and the user's password is not admin
    elif username == "admin" and password != "admin":
        # display a message to the user
        print("Invalid password")
    # check if the user's username is neither admin nor salesman
    elif username != "admin" and username != "salesman":
        # display a message to the user
        print("Invalid username")
    # check if the user's password is incorrect when the username is salesman or admin
    else:
        # display a message to the user
        print("Incorrect password")

#run main
def main():
    # call the login function until the user quits
    login()

main()