import random
class ATM(object):
    def __init__(CardNumber,PinNumber):
        
        self.CardNumber=CardNumber
        self.PinNumber=PinNumber

    def CashWithdrawl(self):
        print("Be ready money is coming out")

    def BalanceEnquiry(self):
        print(random.randint(1000,9000))    