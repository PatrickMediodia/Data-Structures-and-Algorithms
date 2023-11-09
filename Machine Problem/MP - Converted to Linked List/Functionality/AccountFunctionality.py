import sys
import getpass
sys.path.append("..")

from Models import Recipe as recipe, Account as account
from Functionality import Validation as valid


def login(accountCatalog):
    running = True
    while running:
        username = input("Enter username : ")
        password = getpass.getpass('Enter password : ')

        current = accountCatalog.getHead()
        while current != None:
            if current.username == username and current.password == password:
                running = False
                break
            current = current.right
        else:
            print('\nWRONG CREDENTIALS\n')
    
    return current


def new_account(accountCatalog):
    running = True
    isUsed = False

    while running:
        username = valid.getValidInputLegnth(3, "username")
        password = valid.getValidPassword("password")

        current = accountCatalog.getHead()
        while current != None:
            if current.username.lower() == username.lower():
                print("\nUsername already exists, Please choose another \n")
                isUsed = True
            current = current.right
        if not isUsed:
            running = False
        
    print("\nAccount has been created\n")
    accountCatalog.insert(account.Account(username, password,[]))


def account_settings(logged_in, accountCatalog):
    choice = input("\nAccount Options\n"
                  +"\n[1] Change password"
                  +"\n[2] Delete Account"
                  +"\n[X] Back to Main Menu"
                  +"\n\nEnter your choice : ")
    
    if choice == "1":
        change_password(logged_in, accountCatalog)

    elif choice == "2":
        if delete_account(logged_in, accountCatalog):
            return True
        return False

    elif choice.upper() == "X":
        return
    else:
        print("\nInvalid Input\n")


def change_password(logged_in, accountCatalog):
    while True:
        old_password = getpass.getpass("Enter old password : ")
        if old_password == logged_in.password:
            break
        print("\nPassword entered does not match current password\n")

    new_password = valid.getValidPassword("new password")
    logged_in.password = new_password

    print(f'\nPassword of your account with username {logged_in.username} has been changed\n')


def delete_account(logged_in, accountCatalog):
    choice = input("\nDelete Account\n"
                  +"\nAre you sure you want to delete your account?"
                  +"\nOnce you have deleted it you cannot get it back."
                  +"\n\nDelete your account [Y/N] : ")

    if choice.upper() == "Y":
        accountCatalog.delete(logged_in)    
        print('\nAccount has been deleted\n')
        return True

    elif choice.upper() == "N":
        print('\nDeletion was aborted\n')
        return False

    else:
        print("\nInvalid Input\n")



    
