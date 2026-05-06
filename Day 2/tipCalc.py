def main():
    totalBill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    tipAsPercent = tip / 100
    totalTip = totalBill * tipAsPercent
    totalBillWithTip = totalBill + totalTip
    billPerPerson = totalBillWithTip / people
    finalAmount = round(billPerPerson, 2)
    print(f"Each person should pay: ${finalAmount}")

if __name__ == "__main__":
    main()