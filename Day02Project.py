print("Welcome to the Tip Calculator!!\n")

userQty=int(input("Enter total no. of people to split the bill with: \n"))
totalBill=float(input("Enter the total bill amount: $\n"))
tipValue1=float(input("Select a tip percentage: \n"))

tipPercent=tipValue1/100
tipValue2=totalBill*tipPercent
tipValue3=totalBill+tipValue2
tipSplit=tipValue3/userQty
finalTip=round(tipSplit,2)
print(f"Your total payable amount per person for {userQty} is {finalTip}")
