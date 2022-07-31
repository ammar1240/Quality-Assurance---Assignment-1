#fifth test case

import doctest
def kmToMiles(x):

    '''>> kmToMiles(5)
3.10686
>>> kmToMiles(90)
55.92339
>>> kmToMiles(35)
21.747985
>>>'''
    return x*0.621371

doctest.testmod()
