#! /home/user/anaconda2/envs/bioinf/bin/python

#This script was made in Python 3.7.2
acountbal = 50000
print('%s' % "Welcome to Festus Enterpise Bank".center(60))
print('%s' %"We are commited to serve you".center(60))
choice = input("Please enter 'b' to check balance, 'w' to withdraw, or 'd' to deposit: ")
while choice != 'q':
    if choice.lower() in ('w','b','d'):
        
        if choice.lower() == 'd':
            print("How much do you want to deposit?")
            deposit = float(input("Enter amount to deposit: "))
            print ("You have deposited %d into your account." %deposit)
            acountbal= acountbal + deposit
            print("Your new account balance is: %d." %acountbal)
            choice = input("Enter b for balance, w to withdraw, d for deposit or q to quit: ")
            print(choice.lower())
        if choice.lower() == 'b':
            print("Your balance is: %d" % acountbal)
            print("Do you want to do another transaction?")
            choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
            print(choice.lower())
        else:
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= acountbal:
                print("Here is your: %.2f" % withdraw)
                acountbal = acountbal - withdraw
                print("Your new account balance is: %d." %acountbal)
                print("Do you want to do another transaction?")
                choice = input("Enter b for balance, w to withdraw, d for deposit or q to quit: ")
                #choice = 'q'
            else:
                print("You have insufficient funds, your account balance is: %.2f" % acountbal)
        
            
            
    else:
        print("Wrong choice!")
        choice = input("Please enter 'b' to check balance 'w' to withdraw or 'd' to deposit: ")

#CK: Good