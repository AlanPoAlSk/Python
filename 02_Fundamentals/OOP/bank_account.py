class BankAccount:
    
    # use a classmethod to print all instances of a Bank Account's info


    # all_bank_accounts = []
    
    
    # @classmethod
    # def display_all(cls):
    #     for account in BankAccount.all_bank_accounts:
    #         BankAccount.all_bank_accounts.append()
    #         print(BankAccount.account_info())
        
        
    
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
        print("++++++++++LIVE_INFO+++++++++")
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
        
        
alan = BankAccount(1000, 0.03)
bob = BankAccount (5000, 0.03)

alan.deposit(1000).deposit(500).deposit(400).withdraw(3000).account_info()

bob.deposit(500).deposit(10000).withdraw(1000).withdraw(500).withdraw(500).withdraw(800).interest_yeld("yeld").account_info()

# print(BankAccount.account_info('self'))