class atm:
    def __init__(self, cardno, pin):
        self.cardno = cardno
        self.pin = pin
        self.amount = 50000
    
    def checkBalance(self):
        print("Your balance is : ", self.amount)
    
    def withdrawal(self,amountt):
        self.amount = self.amount - amountt
        print("U have withdrawn : "+ str(amountt)+ " ur remaining balance : "+ str(self.amount))
    
def main():
    cardno = input("Insert ur card number : ")
    pin = input("Enter ur pin number : ")
    newUser = atm(cardno, pin)
    print("Choose your activity : 1.balance enquiry, 2.withdrawal")
    activity = int(input("Enter activity number : "))
    if (activity == 1):
        newUser.checkBalance()
    elif (activity == 2):
        amount = int(input("Enter amount : "))
        newUser.withdrawal(amount)
    else:
        print("Enter a valid number : ")

main()