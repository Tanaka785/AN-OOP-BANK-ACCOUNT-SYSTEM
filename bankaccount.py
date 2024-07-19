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
            self.option = self.get_signing_in_or_up_option()
            if (self.option) == 1:
                self.sign_up()
            elif (self.option) == 2:
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
            self.option = input("CHOOSE OPTION: ").strip()
            if (self.validate_signing_in_or_up_option(self.option)):
                return (self.option)
    

    def validate_signing_in_or_up_option(self, option):
        if (self.option):
            try:
                self.option = int(self.option)
            except ValueError:
                print("Please Enter An Integer Value For The Option!")
                self.sign_up_or_sign_in()
            else:
                if (self.option) in (self.signing_in_or_up_options):
                    return True
                else:
                    print("Please Choose An Option that Is Among The Provided Options!")
                    self.sign_up_or_sign_in()
        else:
            print("Come on now 😌. Please Enter Something")
            self.sign_up_or_sign_in()


    def sign_up(self):
        user_id_number = self.get_user_id_number()


    def get_user_id_number(self):
        while True:
            user_id_number = input("ID Number: ").strip()
            if self.validate_user_id_number(user_id_number):
                return user_id_number


    def validate_user_id_number(self, user_id_number):
        if user_id_number:
            ...
        else:
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