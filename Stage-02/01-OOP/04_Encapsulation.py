class BankAccount :
    def __init__(self , name , balance):
        self.owner =  name
        self.__balance =  balance
    def get_balance(self):
        print(f"Balance : ${self.__balance}")
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount to deposit")
        else :
            self.__balance += amount
            print(f"Deposit successfully!! Balance : ${self.__balance}")
    def withdraw(self,amount):
        if amount <= 0 or amount > self.__balance:
            print("Invalid amount to withdraw")
        else :
            self.__balance -= amount
            print(f"Withdraw successfully!! Balance : ${self.__balance}")

consumer = BankAccount("kesha",50000)
print(consumer.owner)
# print(consumer.__balance)  ==> throws error
consumer.get_balance()
consumer.deposit(10000)
consumer.deposit(0)
consumer.withdraw(100000)
consumer.withdraw(15000)
