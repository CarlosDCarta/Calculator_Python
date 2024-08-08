import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def mulitply(n1, n2):
    return(n1 * n2)

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": mulitply,
    "/": divide,
}
def calculator():
    print(logo.logo1, logo.logo2)
    num1 = float(input("What is the first number? "))
    accumulate = True
    
    while accumulate:

        for symbol in operators:
            print(symbol)
        operator_symbol = str(input("Choose Operator: "))
        num2 = float(input("What is the second number? "))

    #calculations
        for key in operators:
            if key == operator_symbol:
                answer = operators[key](num1, num2)
                print(f"{num1} {operator_symbol} {num2} = {answer}")
    # checking to start over or not
        choice = str(input(f"Type 'y' if you want to continue with {answer}. Type 'n' if you would like to start over")).lower()
        if choice == "n":
            accumulate = False
            print("\n" * 100)
            calculator()
        else:
            num1 = answer

calculator()
