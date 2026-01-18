
account_balance = 10000
withdrawn_amount = int(input("Ënter the amount to be withdraw : "))

if account_balance > withdrawn_amount:
    if (withdrawn_amount % 100 == 0):
        print ("amount can be withdrawn")
        x = account_balance - withdrawn_amount

        print("withdrawn_amount amount is", withdrawn_amount)
        print("remaining balance is", x)
    else:
        print ("try amount which is multiple of 100")

else:
    print ("withdrawl amount is bigger than account amount")