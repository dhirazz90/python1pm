"""
i = 0
while i < 10:
    i += 1
    if i == 2 or i == 5 or i == 8:
        continue
    print(i)
"""


#def dell():
#    pass

#def toshiba():
# pass

"""
def check(fun):
    def inf(x , y):
        if y >= 100 or x >= 100:
            return" maxium value has been entered"
        else:
            return fun(x , y)
    return inf


@check
def add(x,y):
    return x + y

print(add(10, 10))
"""

import calendar
print(calendar.calendar(2020))