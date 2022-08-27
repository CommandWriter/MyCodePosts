print("Welcome to the Bill and Tip Calculator")
Billed = input ("What is your total bill amount?: $")
Customer = input ("Total no.of.people in your group? ")
Tip = int(input ("Please input, tip in percentage.\n The popular options are 12, 15, 20 :"))
tip_percentage = Tip / 100
Billed_Amount = float(Billed)
Group = int(Customer)
Tip_Amount = Billed_Amount * tip_percentage
Total_bill = Billed_Amount + Tip_Amount
Split_amount = Total_bill / Group
print (f"Your bill is {Billed_Amount} USD, with a inclusion tip of {Tip_Amount} USD, your updated bill is {Total_bill}, the split is {Split_amount} USD.")