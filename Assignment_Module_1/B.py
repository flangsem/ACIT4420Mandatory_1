class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount>0:
            self.balance += amount
        else:
            print(f"Cannot deposit: {amount} to {self.account_holder} as it is not possible do deposit 0 or a negative ammount")   
        return
    
    def withdraw(self, amount):
        if self.balance >= amount & amount > 0:
            self.balance -= amount
            return
        elif amount < 0:
            return print("Cannot withdraw an ammount of 0 or lower, use a positive number to withdraw from account")
    
        else:
            return print("Unsuficcient funds")
        return
    
    def account_info(self):
        return(f"Account holder: {self.account_holder} \nAccount Balance: ${self.balance:.2f}")

class SavingsAccount(BankAccount):
    interest_rate = 0.02
    def __init__(self, account_holder:str, balance: float):
        super().__init__(account_holder, balance)
        return
    
    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)
        return

class CheckingAccount(BankAccount):
    transaction_fee = 1
    def __init__(self, account_holder:str, balance: float, ):
        super().__init__(account_holder,balance)
    
    def withdraw(self, amount):
        if self.balance >= (amount + self.transaction_fee):
            self.balance -= (amount + self.transaction_fee)
        else:
            return print("Unsuficcient funds")
        return
    


fredriks = CheckingAccount("Fredrik", 100)
print(f"created account, name should be Fredrik, ammount should be 100: Result: {fredriks.account_info()}")

fredriks.withdraw(10)
print(f"Ammount should be 89. Result: {fredriks.account_info()}")
fredriks.withdraw(90)
print(f"Ammount should be 89. Result:{fredriks.account_info()}")

frodes = SavingsAccount("Frode", 200)
print(print(f"created account, name should be Frode, ammount should be 200: Result: {frodes.account_info()}"))
frodes.apply_interest()
print(f"Ammount should be 204. Result: {frodes.account_info()}")
frodes.withdraw(20)
print(f"Ammount should be 184. Result: {frodes.account_info()}")

adas = BankAccount("ada", -100)
print(f"created account, name should be ada, ammount should be -100: Result: {adas.account_info()}")
adas.deposit(-1001)
print(f"Ammount should be -100. Result: {adas.account_info()}")
adas.withdraw(-100)
print(f"Ammount should be -100. Result: {adas.account_info()}")
adas.deposit(10)
print(f"Ammount should be -90. Result: {adas.account_info()}")
