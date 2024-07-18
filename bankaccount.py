class Account:
    def __init__(self):
        self.balance = 0


class Savings_Account(Account):
    def __init__(self):
        super().__init__()


class Checkings_Account(Account):
    def __init__(self):
        super().__init__()


class Credit_Account(Account):
    ...