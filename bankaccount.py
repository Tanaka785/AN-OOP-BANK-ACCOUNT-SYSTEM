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
        self.bank_accounts = {
            1: "Savings Account",
            2: "Checkings Account",
            3: "Credit Account",
            4: "Quit",
        }
        self.system_options = {
            1: "Deposit Money",
            2: "Withdraw Money",
            3: "Check Account Balances",
            4: "Transfer Money between Accounts",
            5: "Generate Account statements",
        }


    def sign_up_or_sign_in(self):
        self.print_options(self.signing_in_or_up_options)
        signing_option = int(self.get_option())
        if (signing_option) == 1:
            self.sign_up()
        elif (signing_option) == 2:
            self.sign_in()
        else:
            self.quit_program()


    def print_options(self, options):
        print()
        for option in (options):
            print(f"{option}. {options[option]}")
        print()


    def get_option(self):
        while True:
            signing_option = input("CHOOSE OPTION: ").strip()
            if (self.validate_chosen_option(signing_option, self.signing_in_or_up_options)):
                return (signing_option)
    

    def validate(self, signing_option, options):
        if (signing_option):
            try:
                signing_option = int(signing_option)
            except ValueError:
                print("Please Enter An Integer Value For The Option!")
                return False 
            else:
                if (signing_option) in (options):
                    return True
                else:
                    print("Please Choose An Option that Is Among The Provided Options!")
                    return False 
        else:
            self.print_null_value_error()
            return False 


    def validate_chosen_option(self, signing_option, options):
        if self.validate(signing_option, options):
            return True
        else:
            self.sign_up_or_sign_in()


    def sign_up(self):
        user_fullname = self.get_user_fullname()
        user_phone_number = self.get_user_phone_number("Phone Number")
        user_id_number = self.get_user_id_number("Id Number")
        account_to_create = self.get_account_to_create()
        self.save_sign_up_details(
            user_fullname,
            user_phone_number,
            user_id_number,
            account_to_create,
        )
        print(f"You have successfully created a {account_to_create} \n")
        print("->Your Phone Number Is Your Account Number")
        print(f"->Your Id-Number Is Your Password \n")
        self.inside_system_options()


    def get_user_fullname(self):
        while True:
            user_fullname = input("Full Name: ").strip()
            if self.validate_user_fullname(user_fullname):
                return (user_fullname.title())
            
    
    def validate_user_fullname(self, user_fullname):
        if user_fullname:
            if re.search(r"^([A-Za-z]+)(\s[A-Za-z]+)+$", user_fullname):
                return True
            else:
                print("Please Enter Your Fullname!")
                return False
        else:
            self.print_null_value_error()


    def get_user_phone_number(self, phone_number_or_account_number):
        while True:
            user_phone_number = input(f"{phone_number_or_account_number}: ")
            if self.validate_user_phone_number(user_phone_number, phone_number_or_account_number):
                return (user_phone_number)
        

    def validate_user_phone_number(self, user_phone_number, phone_number_or_account_number):
        if user_phone_number:
            if re.search(r"^(\d{10})$", user_phone_number):
                return True
            else:
                print(f"Please Enter A Valid {phone_number_or_account_number}!")
                return False 
        else:
            self.print_null_value_error()

            
    def get_user_id_number(self, id_number_or_password):
        while True:
            user_id_number = input(f"{id_number_or_password}: ").strip()
            if self.validate_user_id_number(user_id_number, id_number_or_password):
                return (user_id_number.upper())


    def validate_user_id_number(self, user_id_number, id_number_or_password):
        if user_id_number:
            if re.search(r"^(\d{2})-(\d{7})([A-Za-z]{1})(\d{2})$", user_id_number):
                return True 
            else:
                print(f"Please Enter A Valid {id_number_or_password}!")
                return False 
        else:
            self.print_null_value_error()


    def get_account_to_create(self):
        while True:
            self.print_options(self.bank_accounts)
            account_to_create:int = input("Which Account Do You Want To Create: ")
            if self.validate_account_to_create(account_to_create, self.bank_accounts):
                account_to_create = int(account_to_create)
                return (self.bank_accounts[account_to_create])
        

    def validate_account_to_create(self, account_to_create, options):
        if self.validate(account_to_create, options):
            return True
        else:
            self.get_account_to_create()


    def save_sign_up_details(self, fullname, phone_number, id_number, account_name):
        with open("bank_accounts_details.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "Full Name",
                "Phone Number",
                "Id Number",
                "Account Name"
                ])
            writer.writerow({
                "Full Name": fullname, 
                "Phone Number": phone_number,
                "Id Number": id_number,
                "Account Name": account_name,
            })
        with open("bank_accounts.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Account Number", "Password"])
            writer.writerow({
                "Account Number": phone_number,
                "Password": id_number,
            })


    def print_null_value_error(self):
        print("Come on now 😌. Please Enter Something")

        
    def sign_in(self):
       account_number = self.get_user_phone_number("Account Number")
       password = self.get_user_id_number("Password")
       account_details = self.get_account_details()
       if self.compare_sign_in_details(account_number, password, account_details):
           print("Sign In Successful🤩")
           self.inside_system_options()
       else:
           print("Account Details Provided Are Invalid! Try Again...")
           self.sign_in()


    def compare_sign_in_details(self, account_number, password, account_details):
        for account in account_details:
            if (account["Account Number"] == account_number and account["Password"] == password):
                return True
            else:
                return False
            

    def get_account_details(self):
        account_details = list()
        with open("bank_accounts.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                account_details.append({"Account Number": row["Account Number"], "Password": row["Password"]})
        return (account_details)

    def inside_system_options(self):
        self.print_options(self.system_options)
        system_option = int(self.get_option())
        if (system_option) == 1:
            self.deposit_money()
        elif (system_option) == 2:
            self.withdraw_money()
        elif (system_option) == 3:
            self.check_account_balances()
        elif (system_option) == 4:
            self.transfer_money_between_accounts()
        elif (system_option) == 5:
            self.generate_account_statements()
        else:
            self.quit_program()


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