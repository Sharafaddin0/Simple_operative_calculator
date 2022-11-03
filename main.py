# Greetings to the calculator with basic operations
print("Welcome to the basic calculator!")

from art import logo
print(logo)

# Functions of 4 fundamental operations
def add(n1, n2):
  return n1 + n2

def subt(n1, n2):
  return n1 / n2

def mult(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

# Create the list of operations with keys and values
operations = {
  "+": add,
  "-": subt,
  "*": mult,
  "/": div
}

# Define a new function and this function takes no inputs
def function():
  num1 = float(input("Enter the first number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True  #Flag setted here
  
  # Add while loop 
  while should_continue:
    num2 = float(input("Enter the second number: "))
    operations_symbol = input("Choose the operation to start: ")
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)  
    print(f"{num1} {operations_symbol} {num2} = {answer}")

    # Ask the user if he/she wants to continue or restart the program
    choice = input("Type 'yes' to continue. Type 'no' to start calculator again.")
    if choice == "yes":
      num1 = answer
    else:
      should_continue = False
      # Instead of exiting the while loop, we call a calculator() function. It is going to take us all the way back to start recalculation.
      function()

function()