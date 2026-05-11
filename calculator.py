def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2
    
def multiply(num1,num2):
    return num1*num2
    
def divide(num1,num2):
    return num1/num2
        
def exponent(num1,num2):
    return num1**num2
    
def root(num1,num2):
    return num1**(1/num2)
        
def remainder(num1,num2):
    return num1%num2
while True:
    num1=int(input("Enter The first number:"))
    operator=input("Enter Operator:")
    num2=int(input("Enter The second number:"))
    
    if operator== '+':
        result=add(num1,num2)
        print('Result =',result)
    
    elif operator== '-':
        result=subtract(num1,num2)
        print('Result =',result)
        
    elif operator== '*':
        result=(multiply(num1,num2))
        print('Result =',result)
    
    elif operator== '/':
        if num2==0:
            print('Number cant be divided by zero')
        else:    
            result=divide(num1,num2)
            print('Result =',result)
    
    elif operator== '%':
        if num2==0:
            print('Number cant be divided by zero')
        else:
            result=(remainder(num1,num2))
            print('Result =',result)
    
    elif operator== '**':
        result=exponent(num1,num2)
        print('Result =',result)
    
    elif operator== '√':
        if num1<0:
            print('Imaginary Number')
        elif num2==0:
            print('Invalid root ')
        else:    
            result=root(num1,num2)
            print('Result =',result)
        
    else:
        print('Invalid operator was used: ')
    choose=input('Exit (y/n)')

    if choose== 'y':
        break
