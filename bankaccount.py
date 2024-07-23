import csv
import sys
import re

class Account:
    def __init__(self):
        self.balance = 0
        self.signing_in_or_up_options = {
            1: "Create Bank Account",
            2: "Access Account",
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
            6: "Quit",
        }


    def sign_up_or_sign_in(self):
        self.print_options(self.signing_in_or_up_options)
        signing_option = int(self.get_option(self.signing_in_or_up_options))
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


    def get_option(self, options):
        while True:
            signing_option = input("CHOOSE OPTION: ").strip()
            if (self.validate_option(signing_option, options)):
                return (signing_option)
            else:
                self.print_options(options)


    def validate_option(self, provided_option, options):
        if (provided_option):
            try:
                provided_option = int(provided_option)
            except ValueError:
                print("Please Enter An Integer Value For The Option!")
                return False 
            else:
                if (provided_option) in (options):
                    return True
                else:
                    print("Please Choose An Option that Is Among The Provided Options!")
                    return False 
        else:
            self.print_null_value_error()
            return False 


    def sign_up(self):
        user_fullname = self.get_user_fullname()
        user_phone_number = self.get_user_phone_number("Phone Number")
        user_id_number = self.get_user_id_number("Id Number")
        account_option = self.get_account()
        if (account_option.lower()) == "quit":
            self.quit_program()
        else:
            self.save_sign_up_details(
                user_fullname,
                user_phone_number,
                user_id_number,
                account_option,
            )
            print(f"You have successfully created a {account_option} \n")
            print("->Your Phone Number Is Your Account Number")
            print(f"->Your Id-Number Is Your Password \n")
            self.sign_up_or_sign_in()
            

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


    def get_account(self):
        while True:
            self.print_options(self.bank_accounts)
            account_option:int = input("Choose Account: ")
            if self.validate_option(account_option, self.bank_accounts):
                account_option = int(account_option)
                return (self.bank_accounts[account_option])
        

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
           self.particular_account()
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


    def particular_account(self):
        account_option:int = self.get_account()
        if (account_option) == 1:
            savings = Savings_Account()
        elif (account_option) == 2:
            checkings.account_options()
        elif (account_option) == 3:
            credit.account_options()
            

    def quit_program(self):
        sys.exit("Goodbye👋")


class Savings_Account(Account):
    def __init__(self):
        super().__init__()
        self.inside_account_options = {
            1: "Deposit Money",
            2: "Withdraw Money",
            3: "Transfer Funds",
            4: "Check Balance",
            5: "View Interest Earned",
            6: "Generate Statement",
            7: "Set Savings Goals",
            8: "Set Up Alerts",
            9: "Update Account Information",
            10: "Quit",
            }
        self.account_options()


    def account_options(self):
        ...


class Checkings_Account(Account):
    def __init__(self):
        super().__init__()
        self.inside_account_options = {
            1: "Deposit Funds",
            2: "Withdraw Funds", 
            3: "Pay Bills", 
            4: "Withdraw Funds", 
            5: "Transfer Funds",
            6: "Check Balance", 
            7: "Set Up Direct Deposit",
            8: "Update Account Information",
            9: "Use My Debit Card",
            10: "Quit",

        }


    def account_options(self):
        account_option = self.get_account()


class Credit_Account(Account):
   def __init__(self):
        super().__init__()
        self.inside_account_options = {
            1: "Make Payment",
            2: "Check balance",
            3: "Check Credit Limit",
            4: "Request Credit Limit Increase",
            5: "Generate Account Statement",
        }
   

   def account_options(self):
        ...


account = Account()
account.sign_up_or_sign_in()
savings = Savings_Account()
credit = Credit_Account()
checkings = Checkings_Account()
