#Author is Paul Mwaura
"""
This is the basic M-Pesa Menu logic with console interface.
The code can be improved by use of functions to make it much more smaller but I guess
I had the 'motivation' to type all these if statements.
Feel free to improve the code anyway.
"""
import time
option = int(input("Enter\n 1 for Send Money\n 2 for Withdraw Cash\n 3 for Buy Airtime\
\n 4 for Loans and Savings\n 5 for Lipa na Mpesa\n 6 for My Account\n >> "))
if option == 1:
    print("---Send money---")
    option = int(input("Enter\n 1 for Search sim contacts\n 2 for Enter phone no.\n >> "))
    if option == 1:
        names =["Paul", "Vince", "Sam", "Ken", "Collins"]
        name = input("Enter Name : ")
        if name in names:
            amount = int(input("Enter Amount : "))
            if amount <= 70000:
                pin = int(input("Enter M-Pesa PIN : "))
                if pin == 1234:
                    balance = 10001
                    if amount <=balance:
                        print("Sending ", amount ," to ", name)
                        time.sleep(3)
                        print("")
                        print("SENT")
                    else:
                        print("You don't have enough balance in your M-Pesa Acount.")
                else:
                    print("Invalid M-Pesa PIN!")
            else:
                print("Amount exceeds allowed M-Pesa sending limit")
        else:
            print("Name not in Contact list!")
    elif option == 2:
        number = int(input("---Enter Phone No. "))
        if number == number:
            amount = int(input("Enter Amount : "))
            if amount <= 70000:
                pin = int(input("Enter M-Pesa PIN : "))
                if pin == 1234:
                    balance = 10001
                    print("")
                    print("Sending...")
                    print("")
                    if amount <= balance:
                        print("Sending ", amount)
                        time.sleep(2)
                        print("")
                        print("SENT", amount)
                    else:
                        print("You don't have enough balance in your M-Pesa Acount.")
                else:
                    print("Invalid M-Pesa PIN!")
            else:
                print("Amount exceeds allowed M-Pesa sending limit")
        else:
            print("Number not in contact list!")
    else:
        print("Option Not Available!")
if option == 2:
    print("---Withdraw Cash---")
    option = int(input("Enter\n 1 for From Agent\n 2 for From ATM \n >> "))
    if option == 1:
        print("---FromAgent---")
        number = int(input("Enter Agent No. : "))
        amount = int(input("Enter Amount : "))
        if amount <= 70000:
            pin = int(input("Enter M-Pesa PIN : "))
            if pin == 1234:
                balance = 10001
                if amount < balance:
                    print("Sending.... ")
                    time.sleep(5)
                    print("")
                    print("SENT ", amount)
                else:
                    print("You don't have enough balance in your M-Pesa Acount.")
            else:
                print("Invalid M-Pesa PIN!")
        else:
            print("Amount exceeds allowed M-Pesa sending limit")
    elif option == 2:
        print("---From ATM---")
        option = int(input("EnterAgent No. "))
        amount = int(input("Enter Amount : "))
        if amount <= 70000:
            pin = int(input("Enter M-Pesa PIN : "))
            if pin == 1234:
                balance = 10000
                print("Sending.... ")
                if amount < balance:
                    time.sleep(5)
                    print("")
                    print("SENT ", amount)
                else:
                    print("You don't have enough balance in your M-Pesa Acount.")
            else:
                print("Invalid M-Pesa PIN!")
        else:
            print("Amount exceeds allowed M-Pesa sending limit")
    else:
        print("Option not Available!")
elif option == 3:
    print("---Buy Airtime---")
    option = int(input("Enter\n 1 for My Phone\n 2 for Other Phone\n >> "))
    if option == 1:
        amount = int(input("Enter Amount : "))
        if amount < 70001:
            pin = int(input("Enter M-Pesa PIN : "))
            if pin == 1234:
                print("Sending.... ")
                balance = 10001
                if amount < balance:
                    time.sleep(5)
                    print("")
                    print("SENT ", amount)
                else:
                    print("You don't have enough balance in your M-Pesa Acount.")
            else:
                print("Invalid M-Pesa PIN!")
        else:
            print("Amount exceeds allowed M-Pesa sending limit")
    elif option == 2:
        number = int(input("---Enter Phone No. "))
        if number == number:
            amount = int(input("Enter Amount : "))
            if amount <= 70000:
                pin = int(input("Enter M-Pesa PIN : "))
                if pin == 1234:
                    balance = 10001
                    print("")
                    print("Sending...")
                    print("")
                    if amount <= balance:
                        print("Sending ", amount)
                        time.sleep(2)
                        print("")
                        print("SENT", amount)
                    else:
                        print("You don't have enough balance in your M-Pesa Acount.")
                else:
                    print("Invalid M-Pesa PIN!")
            else:
                print("Amount exceeds allowed M-Pesa sending limit")
        else:
            print("Number not in contact list!")
    else:
        print("Option Not Available!")
elif option == 4:
    print("Loans and Savings.")
    option = int(input("Enter\n 1 for M-Shwari\n >> "))
    if option == 1:
        print("---M-Shwari---")
        option = int(input("Enter\n 1 for Send to M-Shwari\n 2 for Withdraw from M-Shwari\
        \n 3 for Lock Savings Account\n 4 Loan\n 5 Check Balance\n 6 for Mini Statement\n >> "))
        if option == 1:
            print("---Send to M-Shwari---")
            amount = int(input("Enter Amount : "))
            if amount <= 70000:
                pin = int(input("Enter M-Pesa PIN : "))
                if pin == 1234:
                    balance = 10001
                    print("")
                    print("Sending...")
                    print("")
                    if amount <= balance:
                        print("Sending ", amount)
                        time.sleep(2)
                        print("")
                        print("SENT", amount)
                    else:
                        print("You don't have enough balance in your M-Pesa Acount.")
                else:
                    print("Invalid M-Pesa PIN!")
            else:
                print("Amount exceeds allowed M-Pesa sending limit")
        elif option == 2:
            print("---Withdraw from M-Shwari---")
            amount = int(input("Enter Amount : "))
            if amount <= 70000:
                pin = int(input("Enter M-Pesa PIN : "))
                if pin == 1234:
                    balance = 10001
                    print("")
                    print("Sending...")
                    print("")
                    if amount <= balance:
                        print("Sending ", amount)
                        time.sleep(2)
                        print("")
                        print("SENT", amount)
                    else:
                        print("You don't have enough balance in your M-Pesa Acount.")
                else:
                    print("Invalid M-Pesa PIN!")
            else:
                print("Amount exceeds allowed M-Pesa sending limit")
        elif option == 3:
            print("---Lock Savings Account---")
            option = int(input("Enter\n 1 From M-Pesa\n 2 From M-Shwari\n >>"))
            if option == 1:
                amount = int(input("Enter Target Amount : "))
                if amount <= 70000:
                    pin = int(input("Enter M-Pesa PIN : "))
                    if pin == 1234:
                        balance = 10001
                        print("")
                        print("Sending...")
                        print("")
                        if amount <= balance:
                            print("Sending ", amount)
                            time.sleep(2)
                            print("")
                            print("SENT", amount)
                        else:
                            print("You don't have enough balance in your M-Pesa Acount.")
                    else:
                        print("Invalid M-Pesa PIN!")
                else:
                    print("Amount exceeds allowed M-Pesa sending limit")
            elif option == 2:
                amount = int(input("Enter Target Amount : "))
                if amount <= 70000:
                    pin = int(input("Enter M-Pesa PIN : "))
                    if pin == 1234:
                        balance = 10001
                        print("")
                        print("Sending...")
                        print("")
                        if amount <= balance:
                            print("Sending ", amount)
                            time.sleep(2)
                            print("")
                            print("SENT", amount)
                        else:
                            print("You don't have enough balance in your M-Pesa Acount.")
                    else:
                        print("Invalid M-Pesa PIN!")
                else:
                    print("Amount exceeds allowed M-Pesa sending limit")
            else:
                print("Option NOT Available!")
        elif option == 4:
            print("---Loan---")
            option = int(input("Enter\n 1 for Request Loan\n 2 for Pay Loan\
            3 for  Check Loan Limit\n >>"))
            if option == 1:
                print("Request Loan")
                amount = int(input("Enter Amount : "))
                if amount <= 70000:
                    pin = int(input("Enter M-Pesa PIN : "))
                    if pin == 1234:
                        balance = 10001
                        print("")
                        print("Sending...")
                        print("")
                        if amount <= balance:
                            print("Sending ", amount)
                            time.sleep(2)
                            print("")
                            print("SENT", amount)
                        else:
                            print("You don't have enough balance in your M-Pesa Acount.")
                    else:
                        print("Invalid M-Pesa PIN!")
                else:
                    print("Amount exceeds allowed M-Pesa sending limit")
            elif option == 2:
                print("Pay Loan")
                option == int(input("Enter\n 1 for From M-Pesa\n 2 for From KCB M-Pesa\n >>"))
                if option == 1:
                    amount = int(input("Enter Amount : "))
                    if amount <= 70000:
                        pin = int(input("Enter M-Pesa PIN : "))
                        if pin == 1234:
                            balance = 10001
                            print("")
                            print("Sending...")
                            print("")
                            if amount <= balance:
                                print("Sending ", amount)
                                time.sleep(2)
                                print("")
                                print("SENT", amount)
                            else:
                                print("You don't have enough balance in your M-Pesa Acount.")
                        else:
                            print("Invalid M-Pesa PIN!")
                    else:
                        print("Amount exceeds allowed M-Pesa sending limit")
                elif option == 2:
                    amount = int(input("Enter Amount : "))
                    if amount <= 70000:
                        pin = int(input("Enter M-Pesa PIN : "))
                        if pin == 1234:
                            balance = 10001
                            print("")
                            print("Sending...")
                            print("")
                            if amount <= balance:
                                print("Sending ", amount)
                                time.sleep(2)
                                print("")
                                print("SENT", amount)
                            else:
                                print("You don't have enough balance in your M-Pesa Acount.")
                        else:
                            print("Invalid M-Pesa PIN!")
                    else:
                        print("Amount exceeds allowed M-Pesa sending limit")
                else:
                    print("Option NOT Available!")
            else:
                print("Option NOT Available!")
        elif option == 5:
            print("---Check Balance---")
            pin = int(input("Enter M-Pesa PIN : "))
            if pin == 1234:
                balance = 10001
                print("")
                print("Sending...")
                print("Your Balance is : ", balance)
            else:
                print("Invalid M-Pesa PIN!")
        elif option == 6:
            print("---Mini Statement---")
            option = int(input("Enter\n 1 for Loan\n 2 for Deposit Account\n >>"))
            if option == 1:
                amount = int(input("Enter Amount : "))
                if amount <= 70000:
                    pin = int(input("Enter M-Pesa PIN : "))
                    if pin == 1234:
                        balance = 10001
                        print("")
                        print("Sending...")
                        print("")
                        if amount <= balance:
                            print("Sending ", amount)
                            time.sleep(2)
                            print("")
                            print("SENT", amount)
                        else:
                            print("You don't have enough balance in your M-Pesa Acount.")
                    else:
                        print("Invalid M-Pesa PIN!")
                else:
                    print("Amount exceeds allowed M-Pesa sending limit")
            elif option == 2:
                amount = int(input("Enter Amount : "))
                if amount <= 70000:
                    pin = int(input("Enter M-Pesa PIN : "))
                    if pin == 1234:
                        balance = 10001
                        print("")
                        print("Sending...")
                        print("")
                        if amount <= balance:
                            print("Sending ", amount)
                            time.sleep(2)
                            print("")
                            print("SENT", amount)
                        else:
                            print("You don't have enough balance in your M-Pesa Acount.")
                    else:
                        print("Invalid M-Pesa PIN!")
                else:
                    print("Amount exceeds allowed M-Pesa sending limit")
            else:
                print("Option NOT Available!")
        else:
            print("Option Not Available!")
    else:
        print("Option Not Available!")
elif option == 5:
    print("---Lipa na M-Pesa---")
    option = int(input("Enter\n 1 for Pay Bill\n 2 for Buy Goods and Services\n >> "))
    if option == 1:
        print("---Pay Bill---")
        option = int(input("Enter\n 1 for Search Sim Contacts\n 2 for Enter Business No.\n >>"))
        if option == 1:
            number = int(input("---Enter Phone No. "))
            if number == number:
                amount = int(input("Enter Amount : "))
                if amount <= 70000:
                    pin = int(input("Enter M-Pesa PIN : "))
                    if pin == 1234:
                        balance = 10001
                        print("")
                        print("Sending...")
                        print("")
                        if amount <= balance:
                            print("Sending ", amount)
                            time.sleep(2)
                            print("")
                            print("SENT", amount)
                        else:
                            print("You don't have enough balance in your M-Pesa Acount.")
                    else:
                        print("Invalid M-Pesa PIN!")
                else:
                    print("Amount exceeds allowed M-Pesa sending limit")
            else:
                print("Number not in contact list!")
        elif option == 2:
            number = int(input("---Enter Business No. "))
            if number == 20500:
                amount = int(input("Enter Amount : "))
                if amount <= 70000:
                    pin = int(input("Enter M-Pesa PIN : "))
                    if pin == 1234:
                        balance = 10001
                        print("")
                        print("Sending...")
                        print("")
                        if amount <= balance:
                            print("Sending ", amount)
                            time.sleep(2)
                            print("")
                            print("SENT", amount)
                        else:
                            print("You don't have enough balance in your M-Pesa Acount.")
                    else:
                        print("Invalid M-Pesa PIN!")
                else:
                    print("Amount exceeds allowed M-Pesa sending limit")
            else:
                print("Number not does NOT Exist!")
        else:
            print("Option NOT Available!")
    elif option == 2:
        print("---Buy Goods and Services---")
        number = int(input("---Enter till No. "))
        if number == 20500:
            amount = int(input("Enter Amount : "))
            if amount <= 70000:
                pin = int(input("Enter M-Pesa PIN : "))
                if pin == 1234:
                    balance = 10001
                    print("")
                    print("Sending...")
                    print("")
                    if amount <= balance:
                        print("Sending ", amount)
                        time.sleep(2)
                        print("")
                        print("SENT", amount)
                    else:
                        print("You don't have enough balance in your M-Pesa Acount.")
                else:
                    print("Invalid M-Pesa PIN!")
            else:
                print("Amount exceeds allowed M-Pesa sending limit")
        else:
            print("Number not does NOT Exist!")
    else:
        print("Option Not Available!")
elif option == 6:
    print("---My Account---")
    option = int(input("Enter\n 1 for Mini Statement\n 2 for Check Balance\n 3 for Change PIN\
                       \n 4 Change Language\n 5 for Update Customer Menu\n>> "))
    if option == 1:
        print("---Mini Statement---")
        option = int(input("Enter\n 1 for Loan\n 2 for Deposit Account\n >>"))
        if option == 1:
            amount = int(input("Enter Amount : "))
            if amount <= 70000:
                pin = int(input("Enter M-Pesa PIN : "))
                if pin == 1234:
                    balance = 10001
                    print("")
                    print("Sending...")
                    print("")
                    if amount <= balance:
                        print("Sending ", amount)
                        time.sleep(2)
                        print("")
                        print("SENT", amount)
                    else:
                        print("You don't have enough balance in your M-Pesa Acount.")
                else:
                    print("Invalid M-Pesa PIN!")
            else:
                print("Amount exceeds allowed M-Pesa sending limit")
    elif option == 2:
        print("---Check Balance---")
        pin = int(input("Enter M-Pesa PIN : "))
        if pin == 1234:
            balance = 10001
            print("")
            print("Sending...")
            print("Your Balance is : ", balance)
        else:
            print("Invalid M-Pesa PIN!")
    elif option == 2:
        print("---Change PIN---")
        pin = int(input("Enter Old PIN : "))
        if pin == 1234:
            npin = int(input("Enter New PIN : "))
            npin2 = int(input("Enter New PIN Again : "))
            if npin == npin2:
                print("Your Pin is succesfully changed!")
    elif option == 2:
        print("---Change Language---")
    elif option == 2:
        print("---Update Customer Menu---")
    else:
        print("Option Not Available!")
else:
    print("Option Not Available!")




































