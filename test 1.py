#First test case


import doctest
def sub(x,y):

    '''>> sub(5,4)
1
>>> sub(0,4)
-4
>>> sub(6,6)
0
>>>'''
    return x*y

doctest.testmod()
