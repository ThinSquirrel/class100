class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("Your Balance is: 50000")
    
    def withdrawl(self,amount):
        newAmount = 50000-amount
        print("You Have Withdrawn: "+str(amount)+" your remaining balance is: "+str(newAmount))

def main():
    cardNumber = input("Enter Your Card Number: ")
    pinNumber = input("Enter Your Pin Number: ")
    user = Atm(cardNumber,pinNumber)
    print("Choose your activity")
    print("1. balance enquiry 2. withdraw")
    activity = int(input("enter your activity number: "))
    
    if(activity == 1):

        user.checkBalance()
    elif(activity == 2):

        amount = int(input("Enter Amount: "))
        

        user.withdrawl(amount)
    else:

        print("Enter a valid number")
    
    if(amount > 50000):
        print("Insufficent balance")

if __name__ == "__main__":
    main()