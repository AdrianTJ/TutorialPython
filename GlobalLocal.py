x = 6 # NOT a global variable

def example():
    z = 5 # This is okay because z is defined inside the function. 
    print(z)

# example()

def example2():
    global x # This makes x global. 
    print(x)
    x+=5
    print(x)

# example2()

def example3(): # To get around global variables
    globx = x
    print(globx)
    globx+=5
    print(globx)
    return(globx)

x = example3()

print(x)