# This code is a calculator program. 

# Printing Menu for the user
def Menu():
    print("This calculator can do following commands:")
    print("1) Insert numbers")
    print("2) Sum")
    print("3) Division")
    print("0) Stop")
    Input = input("Select command (0-3): ")
    selection = int(Input)
    return selection
    
# Selecting numbers for the calculator
def InsertNumbers(command):
    Input = input(command)
    Number = int(Input)
    return Number

# Calculating the sum
def Sum(Num1, Num2):
    sum = Num1 + Num2
    return sum
    
# Calculating the division    
def Division(Num1, Num2):
    if (Num2 > 0):
        division = round(Num1 / Num2, 2)
        return division
    else:
        return "Can't divide with zero."

# Main program
def Main():
    Num1 = None
    Num2 = None

    while True:
        selection = Menu()
        
        if (selection == 1):
            Num1 = InsertNumbers("Give first number: ")
            Num2 = InsertNumbers("Give second number: ")
            print("You gave numbers", Num1, "and", Num2)
        elif (selection == 2):
            sum = Sum(Num1, Num2)
            print("Sum", Num1, "+" , Num2, "=", sum)
        elif (selection == 3):
            division = Division(Num1, Num2)
            print("Division", Num1, "/", Num2, "=", division)
        elif (selection == 0):
            print("Program ending.")
            break
        else:
            print("Selection unknown, try again.")
    print("Thank you.")
    return None

Main()
