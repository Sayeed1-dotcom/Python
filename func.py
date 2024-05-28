#user defined function
#add two numbers functions

def sum(a,b):
    print(a + b)

sum(4,5)

#if we want to fix one number (like b=2)
def sum(a,b=2):
    print(a + b)

sum(4) #here b=2 will take automatically



#multiplication of two numbers functions

def M(a,b=3):
    print(a * b)

M(3,5)
M(7) # here b=3 will take automatically