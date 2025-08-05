class Account:
    def __init__ (self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("total balance =",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 9917237959)

while True:
    print("\n----- Menu -----")
    print("1. Credit Amount")
    print("2. Debit Amount")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to credit: "))
        acc1.credit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to debit: "))
        acc1.debit(amount)

    elif choice == '3':
        print("Current balance = Rs.", acc1.get_balance())

    elif choice == '4':
        print("Exiting... Thank you!")
        False

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")