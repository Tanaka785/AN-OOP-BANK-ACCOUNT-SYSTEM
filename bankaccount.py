import csv
import sys
import re

class Account:
    def __init__(self):
        self.balance = 0
        self.signing_in_or_up_options = {
            1: "Sing Up",
            2: "Sign In",
            3: "Exit",
        }


    def sign_up_or_sign_in(self):
        while True:
            self.print_signing_in_or_up_options()
            signing_option = int(self.get_signing_in_or_up_option())
            if (signing_option) == 1:
                self.sign_up()
            elif (signing_option) == 2:
                self.sign_in()
            else:
                self.quit_program()


    def print_signing_in_or_up_options(self):
        print()
        print("Account Options:", "\n")
        for option in (self.signing_in_or_up_options):
            print(f"{option}. {self.signing_in_or_up_options[option]}")
        print()


    def get_signing_in_or_up_option(self):
        while True:
            signing_option = input("CHOOSE OPTION: ").strip()
            if (self.validate_signing_in_or_up_option(signing_option)):
                return (signing_option)
    

    def validate_signing_in_or_up_option(self, signing_option):
        if (signing_option):
            try:
                signing_option = int(signing_option)
            except ValueError:
                print("Please Enter An Integer Value For The Option!")
                self.sign_up_or_sign_in()
            else:
                if (signing_option) in (self.signing_in_or_up_options):
                    return True
                else:
                    print("Please Choose An Option that Is Among The Provided Options!")
                    self.sign_up_or_sign_in()
        else:
            self.print_null_error()
            self.sign_up_or_sign_in()


    def sign_up(self):
        user_fullname = self.get_user_fullname()
        user_id_number = self.get_user_id_number()

    
    def get_user_fullname(self):
        while True:
            user_fullname = input("Full Name: ").strip()
            if self.validate_user_fullname(user_fullname):
                return (user_fullname)
            
    
    def validate_user_fullname(self, user_fullname):
        if user_fullname:
            ...
        else:
            self.print_null_error()

            
    def get_user_id_number(self):
        while True:
            user_id_number = input("ID Number: ").strip()
            if self.validate_user_id_number(user_id_number):
                return user_id_number


    def validate_user_id_number(self, user_id_number):
        if user_id_number:
            if re.search(r"^(\d{2})-(\d{7})([A-Z]{1})(\d{2})$", user_id_number):
                return True 
            else:
                print("Please Enter A Valid Id-Number!")
                return False 
        else:
            self.print_null_error()


    def print_null_error(self):
        print("Come on now 😌. Please Enter Something")

        
    def sign_in(self):
        ...

    def quit_program(self):
        sys.exit("Goodbye👋")


class Savings_Account(Account):
    def __init__(self):
        super().__init__()


class Checkings_Account(Account):
    def __init__(self):
        super().__init__()


class Credit_Account(Account):
    ...


account = Account()
account.sign_up_or_sign_in()