# Takako Sekiya
# TP058659


# main menu ---------------------------------------
def home():
    while True:
        home_num = int(input(f"""Choose the number below:\n
                1.Admin\n
                2.Customer home\n
                3.New Customer\n
                4.Exit\n"""))

        if home_num == 1:
            # 1.Admin
            check_admin()

        elif home_num == 2:
            # 2.Customer home
            while True:
                check_user()
                break

        elif home_num == 3:
            # 3.New Customer
            new_user_menu()

        elif home_num == 4:
            # 4.Exit
            print("Thank you for visiting us!")
            quit()

        else:
            print("Please enter number correctly. ")


# admin -------------------------------------
def get_admin():
    with open("admin.txt", "r") as file:
        for line in file.readlines():
            adname, password = line.split()
            yield adname, password


def admin_authorised(adname, password):
    for ad in get_admin():
        if ad == (adname, password):
            return True
    return False


def is_admin(adname):
    for admin, pss in get_admin():
        if admin == adname:
            return True
    return False


def check_admin_info():
    print("Please enter")
    ad_name = str(input("Username: "))
    password = str(input("Password: "))
    return ad_name, password


def check_admin():
    ad_name, password = check_admin_info()

    if admin_authorised(ad_name, password):
        print(f"\nWelcome back, {ad_name}")
        admin_menu()

    elif is_admin(ad_name):
        print("\nWrong access information.")
        home()


def admin_menu():
    while True:
        admin_menu = int(input(
            f"""\n------ Admin Menu ------\n
                Choose the number below to continue:\n
                1 - Add Car with details, to be rented out.\n
                2 - Modify Car Details\n
                3 - Display All Records of Cars available for Rent\n
                4 - Search Specific record of Specific Car Booking & Customer Payment\n
                5 - Back \n"""))

        if admin_menu == 1:
            # Add Car with details
            print("\n---ADD A NEW CAR TO RENT OUT ---")
            add_car()

        elif admin_menu == 2:
            # Modify Car Details
            print("\n--- MODIFY CAR DETAILS ---")
            edit_car()

        elif admin_menu == 3:
            # Display All Records of Cars available for Rent
            print("\n--- Cars for Rent ---")
            show_cars()

        elif admin_menu == 4:
            # Search Specific record of Specific Car Booking & Customer Payment
            print("\n--- Search Car Booking & Customer Payment ---")
            search_booking()

        elif admin_menu == 5:
            home()

        else:
            print("Please enter number correctly. ")


# Sign up -------------------------------------
def signup():
    while True:
        with open("customer_list.txt", "a") as file:
            print("To create your account, enter usr_name and password:")
            usr_name = input("Usename: ")
            password = input("Password: ")
            customer = f"{usr_name} {password}\n"
            file.write(str(customer))
            print("You are successfully signed up!")
        break
    home()


def get_user():
    with open("customer_list.txt", "r") as file:
        for line in file.readlines():
            usr_name, password = line.split()
            yield usr_name, password


def authorised(usr_name, password):
    for user in get_user():
        if user == (usr_name, password):
            return True
    return False


def is_user(usr_name):
    for usr, pss in get_user():
        if usr == usr_name:
            return True
    return False


def check_usr_info():
    print("Please enter")
    usr_name = str(input("Username: "))
    password = str(input("Password: "))
    return usr_name, password


# -------------------------------------
# login
def check_user():
    usr_name, password = check_usr_info()

    if authorised(usr_name, password):
        print(f"\nWelcome back, {usr_name}")
        user_menu(usr_name)

    elif is_user(usr_name):
        print("\nWrong access information.")
        home()

    else:
        return f"\nUser not found. Please sign up first."
        home()


# -------------------------------------
# New Customer
def new_user_menu():
    while True:
        new_customer_menu = int(input(
            f"""\n------ Customer Menu------\n
            Choose the number below to continue:\n
            1 - View all cars available for rent\n
            2 - Register to Access other Details\n
            3 - Back\n"""))

        if new_customer_menu == 1:
            print("--- View all cars available for rent ---")
            print("Please sign up first")
            signup()

        elif new_customer_menu == 2:
            print("--- Sign up ---")
            signup()

        elif new_customer_menu == 3:
            home()

        else:
            print("\nPlease enter number correctly. ")


# -------------------------------------
# Registered Customer Menu
def user_menu(username):
    while True:
        customer_menu = int(input(
            f"""\n------ Customer Menu------\n
            choose the number below to continue:\n
            1 - View Personal Rental History\n
            2 - View Detail of Cars to be Rented Out\n
            3 - Select and Book a car for a specific duration\n
            4 - Return a Rented Car\n
            5 - Back\n"""))

        if customer_menu == 1:
            # View Personal Rental History
            print("\n--- Personal Rental History ---")
            show_history(username)

        elif customer_menu == 2:
            # View Detail of Cars to be Rented Out
            print("\n--- Car List ---")
            show_cars()

        elif customer_menu == 3:
            # Select and rental a car for a specific duration & do payment to confirm Booking
            print("\n--- Rental A Car ---")
            rental_car(username)

        elif customer_menu == 4:
            # Return a Rented Car
            print("\n--- Return a Rented Car ---")
            return_car(username)

        elif customer_menu == 5:
            home()

        else:
            print("\nPlease enter number correctly. ")


# -------------------------------------
# show rentaled car history
def show_history(username):
    while True:
        with open("customer_history.txt", "r") as file:
            for line in file.readlines():
                if username in line:
                    print(line)
        break
    return username


# -------------------------------------
# View Detail of Cars to be Rented Out

def show_cars():
    with open("car_list.txt", "r") as file:
        for count, line in enumerate(file):
            if not "OUT" in line:
                line = line.split(" ")
                print(
                    f"{count} - Car ID:{line[0]} Car Brand:{line[1]} Car Model:{line[2]} Number:{line[3]} Hourly Price:${line[4]} Daily Price:${line[5]} Weekly Price:${line[6]}")

# -------------------------------------
# rental a car


def rental_car(username):
    while True:
        with open("customer_history.txt", "a") as file:
            file.write(username)

        with open("car_list.txt", "r") as file:
            car_lines = file.readlines()
            car_len = len(car_lines)

        show_cars()

        rental_answer = int(input("\nChoose a number above to rent: "))

        if rental_answer < 0 or int(car_len) < rental_answer:
            print('Please enter correct number: ')

        else:
            with open("car_list.txt", "r") as file:
                for count, line in enumerate(file):
                    if count == rental_answer:
                        is_rent = line
                        print(f"\nThe car you chose: {count}: {is_rent}\n")

            with open("car_list.txt", "r") as file:
                data = file.read()
                data = data.replace(
                    is_rent, f"{is_rent.strip()} OUT\n")

            with open("car_list.txt", "w") as file:
                file.write(data)

            with open("customer_history.txt", "a") as file:
                file.write(f" car:{' '.join(is_rent.split()[:3])} ")

            ask_duration(username, is_rent)

    else:
        print("Please enter correct answer.")


# -------------------------------------
# ask duration
def ask_duration(username, is_rent):
    while True:
        how_long = int(
            input("""How long would you like to rent the car?\n
                1 - days\n
                2 - hours\n
                3 - weeks\nChoose number: """))

        while how_long == 1:
            duration = int(input("Duration (1-7days): "))
            if 0 < duration <= 7:
                with open("customer_history.txt", "a") as file:
                    file.write(f"duration:{duration}day ")
                price_d(duration, is_rent)
                user_menu(username)
                break
            else:
                print("We accept from 1 day up to 7 days.")

        while how_long == 2:
            duration = int(input("Duration (1-23h): "))
            if 0 < duration <= 24:
                with open("customer_history.txt", "a") as file:
                    file.write(f"duration:{duration}h ")
                price_h(duration, is_rent)
                user_menu(username)
                break
            else:
                print("We accept from 1 up to 23 hours.")

        while how_long == 3:
            duration = int(
                input("Duration (1-4weeks): "))
            if 0 < duration <= 4:
                with open("customer_history.txt", "a") as file:
                    file.write(f"duration:{duration}week ")
                    price_w(duration, is_rent)
                user_menu(username)
                break
            else:
                print("We accept from 1 up to 4 weeks.")

        break


# -------------------------------------
# Payment
def pay(price):
    while True:
        pay_method = int(
            input("How would you like to pay?: \n1- Cash \n2 - Credit Card\n"))

        if pay_method == 1:
            while True:
                amount = int(input("Enter the amount of money you pay: "))
                while amount >= price:
                    with open("customer_history.txt", "a") as file:
                        file.write(f"method:cash paid:${amount} ")
                    print("Payment proceeded. Thank you!")
                    return False
                else:
                    print("Please enter correct amount of money.")
            break

        elif pay_method == 2:
            while True:
                card_name = str(input("Please enter your card holder name: "))
                card_num = int(input("Enter card number: "))

                while len(str(card_num)) == 7:
                    with open("customer_history.txt", "a") as file:
                        file.write(
                            f"method:card card-info:{card_name} {card_num} ")
                    print("Payment proceeded. Thank you!")
                    return False
                else:
                    print("Please enter correct information.")
            break
        break
    else:
        print("Please enter correct answer.")


def price_h(duration, is_rent):
    base = int(is_rent.split()[-3])
    fee_h = base * duration
    print(f"\nAmount you pay: ${fee_h}\n")
    pay(fee_h)
    with open("customer_history.txt", "a") as file:
        file.write(f"fee:${fee_h}\n")


def price_d(duration, is_rent):
    base = int(is_rent.split()[-2])
    fee_d = base * duration
    print(f"\nAmount you pay: {fee_d}\n")
    pay(fee_d)
    with open("customer_history.txt", "a") as file:
        file.write(f"fee:${fee_d}\n")


def price_w(duration, is_rent):
    base = int(is_rent.split()[-1])
    fee_w = base * duration
    print(f"\nAmount you pay: ${fee_w}\n")
    pay(fee_w)
    with open("customer_history.txt", "a") as file:
        file.write(f"fee:${fee_w}\n")


# -------------------------------------
# Return a car
def return_car(username):
    to_return = []

    print("The car you rent:\n")
    with open("customer_history.txt", "r") as file:
        for line in file:
            if username in line:
                if not "RETURNED" in line:
                    print(line)
                    to_return.append(line)

    while not len(to_return) == 0:
        return_id = input("Enter ID of the car you'd like to return: ")

        if return_id:
            with open("customer_history.txt", "r") as file:
                lines = []
                for line in file:
                    if return_id in line:
                        returned_car = line.strip() + " RETURNED\n"
                        lines.append(returned_car)
                    else:
                        lines.append(line)

            with open("customer_history.txt", "w") as file:
                for line in lines:
                    file.write(line)

            with open("car_list.txt", "r") as file:
                lines = []
                for line in file:
                    if return_id in line:
                        removed_out = line.replace("OUT", "")
                        lines.append(removed_out)
                    else:
                        lines.append(line)

            with open("car_list.txt", "w") as file:
                for line in lines:
                    file.write(line)

        print("Returned.\nThank you for choosing us!")
        user_menu(username)
        break

    else:
        print("You have nothing to return.\n")
        user_menu(username)


# -------------------------------------
# add a car
def add_car():
    print("Enter information to add a new car:")
    new_brand = input("Car brand: ")
    new_model = input("Car model: ")
    new_num_plate = input("Number plate: ")
    new_passenger = input("Number of passenger: ")
    new_hourly_cost = input("Hourly cost: ")
    new_daily_cost = input("Daily cost: ")
    new_weekly_cost = input("Weekly cost: ")

    with open("car_list.txt", "a+") as file:
        data = file.readlines()
        car_id = new_model[0] + str(len(data))
        new_car = f"\n{car_id} {new_brand} {new_model} {new_num_plate} {new_passenger} {new_hourly_cost} {new_daily_cost} {new_weekly_cost}"
        file.write(str(new_car))
        print(f"Successfully added a new car: {new_car}\n")

    admin_menu()


# -------------------------------------
# Modify Car Details
def edit_car():
    check_lines = []
    lines = []
    not_delete = []

    while True:
        answer1 = int(input(
            "Which would you like to do?\n1 - Modify Car Infomation\n2 - Delete A Car From The List\n"))

        with open("car_list.txt", "r") as file:
            for count, line in enumerate(file):
                line = line.split()
                print(
                    f"{count} - Car ID:{line[0]} Car Brand:{line[1]} Car Model:{line[2]} Number:{line[3]} Hourly Price:${line[4]} Daily Price:${line[5]} Weekly Price:${line[6]}")
                check_lines.append(line)

        while True:
            edit_num = int(input("Choose a number above: "))

            if edit_num <= len(check_lines):
                with open("car_list.txt", "r") as file:
                    for count, line in enumerate(file):
                        if edit_num == count:
                            this_car = line
                            line = line.split()
                            print(
                                f"\nThe car you chose: \n{count} - Car ID:{line[0]} Car Brand:{line[1]} Car Model:{line[2]} Number:{line[3]} Hourly Price:${line[4]} Daily Price:${line[5]} Weekly Price:${line[6]}")

                if answer1 == 1:
                    while True:
                        info = input("Choose info to modify: ")

                        if info in this_car:
                            modify_to = input("Modify to: ")

                            with open("car_list.txt", "r") as file:
                                for count, line in enumerate(file):
                                    if count == edit_num:
                                        new_line = line.replace(
                                            info, modify_to)
                                        lines.append(new_line)
                                    else:
                                        lines.append(line)

                            with open("car_list.txt", "w") as file:
                                for line in lines:
                                    file.write(line)

                            print("Successfully modified information.")
                            admin_menu()
                            break

                        else:
                            print("Please enter existing category.")
                    break

                elif answer1 == 2:
                    print("The car will be permanently deleted. Is it okay?")
                    answer2 = int(input("1 - No\n2 - Yes\n"))

                    if answer2 == 1:
                        admin_menu()

                    elif answer2 == 2:
                        with open("car_list.txt", "r") as file:
                            for count, line in enumerate(file):
                                if count != edit_num:
                                    not_delete.append(line)

                        with open("car_list.txt", "w") as file:
                            for line in not_delete:
                                file.write(line)

                        print("Succcessfully deleted.")
                        admin_menu()

                    else:
                        print("Please enter a correct number")
                        break

                else:
                    print("Please enter a correct number")
                    break

            else:
                print("Please enter a correct number")
                break


# -------------------------------------
# Search Specific record of Specific Car Booking & Customer Payment
def search_booking():
    while True:
        keyword = input(
            "\nEnter keyword to search specific booking and/or payment history: ")

        with open("customer_history.txt", "r") as file:
            for line in file:
                for word in line.split():
                    if keyword in word:
                        print(line)

        answer = int(
            input("\nDo you want to back to the menu page?:\n1 - Yes\n2 - No "))

        if answer == 1:
            admin_menu()


# -------------------------------------
if __name__ == "__main__":
    home()
