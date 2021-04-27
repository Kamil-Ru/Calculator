
import art


# Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def mltiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
'+' : add,
'-' : substract,
'*' : mltiply,
'/' : divide
}

def calculator():
    print(art.logo)
    
    num1 = float(input("What's the frist number?\n"))

    for keys in operations:
        print(keys)

    while True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?\n"))     
        
        calculation_funtion = operations[operation_symbol]
        answer = calculation_funtion(num1,num2)    
            
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.\n") == 'y':
            num1 = answer    
        elif input(f"Star new calculating?\nType 'y' to continue, or type 'n' to exit.\n") == 'y':
            calculator()
        else:
            break
        
calculator()
    
        