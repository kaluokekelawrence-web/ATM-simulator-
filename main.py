Acc_balance = 50000
correct_pin = 7300
max_attempts = 3
attempts = 0
options = ["1=> check balance",
           "2=> Deposit",
           "3=> Withdraw",
           "4=> Exit"]
exit_program = False 
while attempts < max_attempts and not exit_program:
    try:
        PIN = input("Enter PIN (or type exit):").lower()
        if PIN == "exit":
            print("Thank you for using our service , see you soon")
            break
        PIN = int(PIN)
        if PIN != correct_pin:
            print("INVALID PIN, try again")
            attempts += 1
        elif PIN == correct_pin:
            while True:
                print("ACCESS GRANTED")
                print(options[0])
                print(options[1])
                print(options[2])
                print(options[3])
                try:
                    opt = int(input("Pick an option:"))
                    if opt == 1:
                        print("Your available balance is " + str(Acc_balance))
                    elif opt == 2:
                        print("Go to the counter in the bank to deposit cash,thanks")
                    elif opt == 3:
                        wd_amount = int(input("how much do u want to withdraw?:"))
                        if wd_amount > Acc_balance:
                            print("insufficient balance")
                        else:
                            Acc_balance -= wd_amount
                            print(str(wd_amount) + " has been successfully withdrawn")
                            print("Thank you for coming")
                    elif opt == 4:
                        try:
                            cross_checking = input(" Are you sure you want to exit?(yes or no)").lower()
                        except ValueError:
                            print("type yes or no")
                        if  cross_checking == "yes":
                            print("Thank you for coming, hope to see you soon")
                            exit_program = True
                            break
                        elif cross_checking == "no":
                            print("continue")
                        else:
                            print("type either yes or no")
                except ValueError:
                    print("wrong input ,input numbers between 1 to 4")
    except ValueError:
        print("WRONG INPUT,try again")
if attempts >= max_attempts:
    print("ACCOUNT LOCKED,too many trials")
    