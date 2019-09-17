##Command Line Checkbook Application
name= input( "Welcome, may i get your name? ")
print('Hello ' + str(name))
print('\n                                   ')
print ("What can I do for you today? ")
print('\n')
print("1. Current Balance")
print("2. Deposit")
print("3. Withdrawl")
print("4. End Session")

choice= int(input("please enter a number "))
if choice > 4 or < 1:
  print("Invalid Entry")
######move on to options
