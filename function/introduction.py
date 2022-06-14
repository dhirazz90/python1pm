# function is a block

"""
def name():
    print("dhiraj patel")
name()
"""

"""
def abc(x,y):
  
    print(x + y)
x = int(input("enter value of x"))
y = int(input("enter value of y"))

abc(x,y)

"""

"""
def add(x,y,z):

    if x > y and x > z:
       return f"greatest number is: {x}"
    elif y > x and y > z:
        return f"greatest number is: {y}"
    else:
        return f"greastes number is: {z}"
x = int(input("enter value of x"))
y = int(input("enter value of y"))
z = int(input("enter value of z"))
print(add(x,y,z))

"""


def take_vaule():
    
    p = int(input("enter pricipal: "))
    t = int(input("enter time: "))
    r = int(input("enter rate: "))
    return [p,t,r]

def calculator():
    smp = take_vaule()
    p = smp[0]
    t = smp[1]
    r = smp[2]
    return (p*t*r)/100

def display():
    print (f"your SI is: {calculator()}")
pass