class Calculator:
    
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
    
    def addition(self):
        return self.a+self.b
    
    def subtraction(self):
        return self.a-self.b
    
    def multiplication(self):
        return self.a*self.b
    
    def division(self):
        if self.b != 0:
            return self.a/self.b
        else:
            return 'Division by 0  is undefined!'

a=float(input('Enter a number:'))
b=float(input('Enter next number:'))
op=input('Enter an operation (Addition, Subtraction, Multiplication, Division): ')
operation=op.lower()
cal= Calculator(a,b,operation)
if operation=='addition':
    print('Result:',cal.addition())
elif operation=='subtraction':
    print('Result:',cal.subtraction())
elif operation=='multiplication':
    print('Result:',cal.multiplication())
elif operation=='division':
    print('Result:',cal.division())
else:
    print('Please enter an operation from the above list.')


        
        
        
            
        