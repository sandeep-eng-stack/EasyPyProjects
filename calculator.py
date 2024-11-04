#Define functitons for each arithmetic operation
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("error")
    else:    
        return a/b
#Define the symbols and keywords in a dictionary
operations_dict={
    '+':add,
    '-':sub,
    '*':mult,
    '/':div
}
def calculator():
    print("Available operations: '+','-','*','/'")
    #Ask for the first number
    number_1=float(input("Enter the first number:"))
    continue_flag=True
    while continue_flag:
        operator=input("Enter the operation:")
        if operator not in operations_dict:
            print("Recheck the operator")
            print("Choose any of the available opeators")
            break
        #Ask for the second number
        number_2=float(input("Enter the next number:"))
        function=operations_dict[operator]
        result=function(number_1,number_2)
        print(f"{number_1}{operator}{number_2}={result}")
        proceed=input("enter 'yes' to continue or 'no' to end the calculation:")
        if proceed=='yes':
            continue_flag=True
            number_1=result
        elif proceed=='no':
            continue_flag=False
            print("BYE")
        else:
            continue_flag=False
            print("Recheck the input again")
calculator()