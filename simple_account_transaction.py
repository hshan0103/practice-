class BankAccount():

    def __init__(self, acc, bal):
        self.account_number = acc
        self.balance = float(bal)
        self.transaction_list = []

    def deposit_funds(self, amount):
        try:
            amount_float = float(amount)
            
            self.balance += amount_float
            self.transaction_list.append( ('Deposit', amount) )
        except:
            raise Exception('Incorrect input form.')

    def withdraw_funds(self, amount):
        try:
            amount_float = float(amount)
        except:
            raise Exception('Incorrect input form.')
            
        if (self.balance - amount_float > 0):
            self.balance -= amount_float
            self.transaction_list.append( ('Withdrawal', amount) )
        else:
            raise Exception('Insuffiecient funds.')
        
    def get_transaction_string(self):
        transaction_string = ''
        for transaction in self.transaction_list:
            transaction_string += transaction[0] + '\t' + str(transaction[1]) + '\n'
        return transaction_string

    def save_to_file(self):
        filename = str(self.account_number) + '.txt'
        file = open(filename, 'w')
        
        file.write( str(self.account_number) + '\n' )
        file.write( str(self.balance)        + '\n' )
        file.write( self.get_transaction_string())

        file.close()


