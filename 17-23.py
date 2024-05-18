## Just for practice
def withdrawMoney(totalMoney):
    withdrawMoneyValue = int(input("Enter withdraw value: "))
    totalMoney = totalMoney - withdrawMoneyValue
    print("Your new balance is now: " + str(totalMoney))
    return totalMoney

def checkBalance(totalMoney):
    print("Your total balance is " + str(totalMoney))

def addMoney(totalMoney):
    amount = int(input("Enter add money amount: "))
    totalMoney += amount
    return totalMoney

def transferBalance(totalMoney):
    amount = int(input("Enter transfer amount: "))
    if(amount > totalMoney):
        print("Insufficiant balance")
        return totalMoney
    else:
      totalMoney +- amount
      return totalMoney

totalMoney = 1000

while True:
    print("ATM machine")
    print("______________________________________________________________________-")
    print("1. To withdraw money \n2. To check balance \n3. To add money \n4. To transfer balance \n5. Exit")
    print("______________________________________________________________________\n\n")

    value = int(input("Enter your option"))
    if value == 1:
        totalMoney = withdrawMoney(totalMoney)
    elif value == 2:
        checkBalance(totalMoney)
    elif value == 3:
        totalMoney = addMoney(totalMoney)
    elif value == 4: 
        totalMoney= transferBalance(totalMoney)
    else:
        break

    print("\n\nContinue again? y/n ")
    if input() != "y":
        break

