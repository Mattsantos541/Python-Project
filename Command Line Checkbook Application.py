##Command Line Checkbook Application
import locale
locale.setlocale( locale.LC_ALL, '' )



def current_balance():
  with open ("Master_account.txt" ,"r") as MA:
    transactions = MA.readlines()
    amount = 0
    for line in transactions:
      line = float(line)
      amount+= line
      balance = locale.currency(amount, grouping =True)
    print("This is your current balance: " + balance)
    

def deposit():
  deposit_amount= input("How much do you want to deposit? ")
    
  with open ("Master_account.txt", 'a') as MA:
    MA.write('\n')
    MA.write(deposit_amount)

def Withdrawl():
  withdrawl_amount= input("How much do you want to withdrawl? ")
  with open ("Master_account.txt", 'a') as MA:
    MA.write('\n')
    MA.write("-" + withdrawl_amount)


  


customer= input( "Welcome, may i get your name? ")
def menu():
  print('\n')
  print('Hello ' + str(customer) + "...")
  print('\n                                   ')
  print ("What can I do for you today? ")
  print('\n')
  print("1. Current Balance")
  print("2. Deposit")
  print("3. Withdrawl")
  print("4. End Session")



choice = "1"
while choice != "4":
  menu()
  print('\n')
  choice = input("enter a number ")
  if choice == "1":
    current_balance()
  elif choice == "2":
    deposit()
    current_balance()
  elif choice == "3":
    Withdrawl()
    current_balance()
  elif choice == "4":
    print('\n')
    print("Thank You, Have a nice day")
  else:
    print("Invalid entry, please enter another number")


