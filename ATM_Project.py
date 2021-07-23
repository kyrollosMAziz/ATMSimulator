from datetime import date

theCurrentDate = date.today()

class User : #User class is used to identify user attributes
    name = ""
    password = 0
    moneyInTheAccount=0
    maxMoney = False #Maximum amount of money to withdraw per day is withdrawn or not

    def __init__(self,name,password,moneyInTheAccount):
        self.name = name
        self.password = password
        self.moneyInTheAccount = moneyInTheAccount

class PapersAmount : #Class is used to store paper value and amount
    numberOfPapers = 0
    value=0
    def __init__(self,numberOfPapers,value):
        self.numberOfPapers = numberOfPapers
        self.value = value

def Login(User= User,counter = 0): #Login function is used to save current user data in memory
    username = input("Enter Username : ")
    password = int(input("Enter your password : "))
    if username!= User.name or password!= User.password :
        print("you entered incorrect Username or password! ")
        if counter<2:
            Login(User,counter+1)
        else:
            print("Please head to bank to get your card back")
            StartScreen()
    else:
        print("\n ************************","Welcome ", User.name,"************************ \n")
def Withdraw() :
    currentAmount = int(input("Enter the amount of money you want : "))
    tdate = date.today()
    CurrentDate= theCurrentDate
    if CurrentDate != tdate:
        user.maxMoney = False
        CurrentDate = todaysDate
    if user.maxMoney == True: #if user already withdraw the allowed amount of money per day
        print("you have already withdrawn all the available money for you in a day")
        StartScreen()
    if currentAmount > user.moneyInTheAccount:
        print("amount of money entered is not available in your bank account")
        Withdraw()
    if currentAmount >= 8000:#maximum amount of money availble to withdraw in a day
            currentAmount = 8000
            user.maxMoney = True
    nextAmount = currentAmount
    values = [200, 100, 50, 20, 10, 5]
    i = 0
    user.moneyInTheAccount -= currentAmount
    ATMOutcome = []
    while i <=len(values)-1:
        if moneyAmount[i] < currentAmount :
            continue
        value = values[i]
        currentAmount = nextAmount
        if nextAmount >=  value:
            numberOfPapers =int(currentAmount/value)
            nextAmount = currentAmount-int(numberOfPapers)*value
            paperValueAndNumer = PapersAmount(numberOfPapers,value)
            ATMOutcome.append(paperValueAndNumer)
            i+=1
        else:
            i+=1
    print("Output is : \n")
    x = 0
    for obj in ATMOutcome:
        print(obj.numberOfPapers, " of ", obj.value, sep=' ')
        moneyAmount[x] -= obj.numberOfPapers
        x+=1
    print("Have a good day!")
    print("")
    print("Your current balance is : " + str(user.moneyInTheAccount))
    print("")
    print(moneyAmount)

    StartScreen()

def Deposit() :
    depositMoney = int(input("Enter amount of money you wish to deposit : "))
    user.moneyInTheAccount += depositMoney
    print("You have : ",user.moneyInTheAccount,"  in your bank account")
    print("Have a good day")
    StartScreen()
def StartScreen() :
    print("1-Withdraw \n", "2-Deposite")
    processIndex = int(input("Enter the index of the process you wish to do : "))
    processOfChoice = {1: Withdraw, 2: Deposit} #Process Dictionary
    if (processIndex) in processOfChoice:
        processOfChoice[processIndex]()
    else:
        print("Invalid choice")
        StartScreen()


#Database Simulation================================================================================================================
user = User("mariam",12345,300000)

#Current number of papers of each value in the ATM machine = fifty thousand each
numberOfTwoHnds = 50000
numberOfOneHnds = 50000
numberOfFifties = 50000
numberOfTwenties = 50000
numberOfTens = 50000
numberOfFives = 50000

moneyAmount = [numberOfTwoHnds , numberOfOneHnds , numberOfFifties ,numberOfFifties, numberOfTwenties , numberOfTens , numberOfFives]

Login(user,0)
StartScreen()

theCurrentDate = date.today()

ATMOutcome = []
