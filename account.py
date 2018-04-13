class Account:

    def __init__(self, number, owner, balance, limit):
        print("Creating object ... {}".format(self))
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print("Balance {} of owner {}".format(self.__balance, self.__owner))

    def deposit(self, value):
        self.__balance += value

    def cash(self, value):
        if self.can_cash(value):
            self.__balance -= value
        else:
            print("Limit exceeded")

    def transfer(self, value, account):
        self.cash(value)
        account.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @property
    def owner(self):
        return self.__owner

    @limit.setter
    def limit(self, value):
        self.__limit = value

    # Private Methods

    def __can_cash(self, value):
        total_value = self.__balance + self.__limit
        if value <= total_value:
            return True
        else:
            return False
