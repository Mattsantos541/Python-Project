def current_balance():
  with open ("Master_account.txt" ,"r") as MA:
    transactions = MA.readlines()
    amount = 0
    for line in transactions:
      amount+= line
    print("Your balance is ${0.2f}.".format.amount)

def deposit():
  deposit_amount= input("How much do you want to deposit? ")
    
  with open ("Master_account.txt", 'a') as MA:
    MA.write('\n')
    MA.write(deposit_amount)

def Withdrawl():
  withdrawl_amount= input("How much do you want to withdrawl? ")
  with open ("Master_account.txt", 'a') as MA:
    MA.write('\n')
    MA.write(withdrawl_amount)

def user_input():
  choice=input("please enter a number ")

##Command Line Checkbook Application
customer= input( "Welcome, may i get your name? ")
print('Hello ' + str(customer))
print('\n                                   ')
print ("What can I do for you today? ")
print('\n')
print("1. Current Balance")
print("2. Deposit")
print("3. Withdrawl")
print("4. End Session")

user_input()

choice = input("Please enter a numbert ")
#if choice > 4 or < 1:
  #print("Invalid Entry")
######move on to options
if choice== "1":
  current_balance()
elif choice== "2":
  deposit()
elif choice== "3":
  Withdrawl()
elif choice==:
  print("Thank You, Have a nice day")
else:
  print("Invalid entry, please enter another number")


