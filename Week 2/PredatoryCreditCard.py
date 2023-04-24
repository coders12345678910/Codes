from math import pow
from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self.__apr

    def get_apr(self):
        return self.__apr

    def charge(self, price):
        if price + self.balance > self.limit:
            self.balance -= 5
            return False

        else:
            self.balance += price

    def process_month(self):
        if self.calls > 10:
            for calls in range(10, self.calls+1):
                self.balance -=1

        monthly_rate = pow(1+self.apr, 1/12) -1
        compound_interest = monthly_rate * self.balance
        print(f"The interest charged monthly is", compound_interest)
