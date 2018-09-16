class calculator:
    def addition(self,x,y):
        self = x+y
        print(self)
    def subtraction(self,x,y):
        self = x-y
        print(self)
    def multiplication(self,x,y):
        self = x*y
        print(self)
    def division(self,x,y):
        self = x/y
        print(self)

calculator.addition(None,3,5)    # How to call the class, class.function(vars)

'''
So apparently the first object of a class' function shoould be defined as 
'self'? The youtube video said nothing of it, but apparently it's a style 
thing that can cause errors if not done, at least in VS Code. I don't want to 
mess with default settings so I just adjusted the functions to incorporate the 
self variable.
'''