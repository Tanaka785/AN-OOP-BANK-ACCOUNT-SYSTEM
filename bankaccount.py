import csv
import sys

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
            if (self.validate_signing_in_or_up_option(self.option)):
                if (self.option) == 1:
                    self.sing_up()
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
        self.option = input("CHOOSE OPTION: ").strip()
        return (self.option)
    

    def validate_signing_in_or_up_option(self, option):
        if (self.option):
            try:
                self.option = int(self.option)
            except ValueError:
                print("Please Enter An Integer Value For The Option!")
            else:
                if (self.option) in (self.signing_in_or_up_options):
                    return True
                else:
                    print("Please Choose An Option that Is Among The Provided Options!")
        else:
            print("Come on now 😌. Please Enter Something")
            

    def sign_up(self):
        ...

    
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