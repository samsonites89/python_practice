class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return "ID: {0} that belongs to {1} has ${2}".format(self.__id, self.__name, self.__balance)


# code
mine = BankAccount(100, "sam", 20000)

# deposit more
mine.deposit(5000)


class MyString:
    def __init__(self, value):
        self.value = value


mStr = MyString("hello")

print(mStr)