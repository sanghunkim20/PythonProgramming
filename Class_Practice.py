class BankAccount:
    def __init__(self):
        self.__balance = 0

    def getBalance(self):
        return self.__balance
    
    def setBalance(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        self.__balance -= amount
        print("withdraw ", amount, "from your account.")
        print("left money: ", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("deposit ", amount, "to account")
        print("left money: ", self.__balance)

a = BankAccount()
a.deposit(100)
a.withdraw(100)

# 개채 참조 (개체 비교하기)
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    
    def show(self):
        print(self.channel, self.volume, self.on)
    
    def setChannel(self, channel):
        self.channel = channel
    
    def getChannel(self):
        return self.channel
    
def setSilentMode(t):
    t.volume = 2

myTV =Television(11, 10, True)

setSilentMode(myTV)

myTV.show()

class Person:
    def __init__(self, fname, lname) :
        self.firstName = fname
        self.lastName = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

p1 = Student("Kim", "Sanghun", 2024)
p1.welcome()