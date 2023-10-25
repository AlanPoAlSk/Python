class BankAccount:
            
        
    
    def __init__(self,balance,interest_rate):
        self.balance= balance
        self.interest_rate = interest_rate
        
        
    def deposit(self,amount_in):
        self.balance+= amount_in
        return self
        
    
    def withdraw(self,amount_out):
        print("+++++++++++ACTION+++++++++++")
        print(f'Balance: ${self.balance}')
        print(f'Withdraw of ${amount_out} requested')
        if self.balance > amount_out :
            self.balance-= amount_out
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= (amount_out+5)
        print(f'New balance: ${self.balance}')    
        return self
        
    def account_info(self):
        print("++++++++++LIVE_INFO+++++++++++++")
        print(f'Your balance is: ${self.balance}')
        print(f'The interest rate is: ${self.interest_rate}')
        return self
        
        
    def interest_yeld(self, yeld):
        self.yeld = self.balance * self.interest_rate
        self.balance+= self.yeld
        print("+++++GOOD_NEWS!_INTERESTS_ARE_COMING+++++")
        print(f'An interest of ${self.yeld} occurred.')
        print(f'Your new Balance is: {self.balance}')
        return self
        
        
class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance=0 , interest_rate=0.03)
        
    
    def make_deposit(self,amount_in):
        self.account.balance += amount_in
        print("++++A DEPOSIT WAS MADE+++++++++++++++++")
        print(f'You have deposited: ${amount_in}')
        print(f'Your balance: ${self.account.balance}')
        return self
        
        
    def make_withdraw(self,amount_out):
        print("+++++++++++ACTION++++++++++++++++++")
        print(f'Balance: ${self.account.balance}')
        print(f'Withdraw of ${amount_out} requested')
        if self.account.balance > amount_out :
            self.account.balance-= amount_out
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.account.balance -= (amount_out+5)
        print(f'New balance: ${self.account.balance}')    
        return self
        
        
    def display_user_balance(self):
        print("++++++HERE'S YOUR BALANCE AS REQUESTED+++++++")
        print(f'Your current balance: ${self.account.balance}')
        
        
alan = User("Alan","alan.alan@alan.com")
alan.display_user_balance()

alan.make_deposit(1000).make_deposit(3500).make_withdraw(700).display_user_balance()
