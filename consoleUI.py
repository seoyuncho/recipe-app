import Request
from colorama import Fore, Style

def print_mainMenu():
    s = "-" * 30
    print(Fore.CYAN + Style.BRIGHT + s)
    print("Command Menu")
    print(s)
    print(Fore.RESET + Style.RESET_ALL + "1 - List all Categories")
    print("2 - List all Meals by Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - List all Meals by Area")
    print("7 - Menu")
    print("8 - Favorite Recipes")
    print("0 - Exit")


while(True):
    print_mainMenu()
    try:
        option = int(input(Fore.CYAN + Style.BRIGHT + "Enter your choice: "))
        if option == 1:
            Request.opt1()
        elif option == 2:
            Request.opt2()
        elif option == 3:
            Request.opt3()
        elif option == 4:
            Request.opt4()
        elif option == 5:
            Request.opt5()
        elif option == 6:
            Request.opt6()
        elif option == 7:
            print_mainMenu()
        elif option == 8:
            Request.opt8()
        elif option == 0:
            break
        else:
            print("Enter between 0 to 8")
    except ValueError:
        print("Please enter a number.")
