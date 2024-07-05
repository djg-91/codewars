'''
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

    This time we want to write calculations using functions and get the results. Let's have a look at some examples:

        seven(times(five())); // must return 35
        four(plus(nine())); // must return 13
        eight(minus(three())); // must return 5
        six(dividedBy(two())); // must return 3
        
    Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:
'''


def zero(a=None): 
    if not a:
        return '0'
    else:
        return int(eval( '0' + a))
def one(a=None): 
    if not a:
        return '1'
    else:
        return int(eval( '1' + a))
def two(a=None): 
    if not a:
        return '2'
    else:
        return int(eval( '2' + a))
def three(a=None): 
    if not a:
        return '3'
    else:
        return int(eval( '3' + a))
def four(a=None): 
    if not a:
        return '4'
    else:
        return int(eval( '4' + a))
def five(a=None): 
    if not a:
        return '5'
    else:
        return int(eval( '5' + a))
def six(a=None): 
    if not a:
        return '6'
    else:
        return int(eval( '6' + a))
def seven(a=None): 
    if not a:
        return '7'
    else:
        return int(eval( '7' + a))
def eight(a=None): 
    if not a:
        return '8'
    else:
        return int(eval( '8' + a))
def nine(a=None): 
    if not a:
        return '9'
    else:
        return int(eval( '9' + a))

def plus(a): return ' + ' + str(a)
def minus(a): return ' - ' + str(a)
def times(a): return ' * ' + str(a)
def divided_by(a): return ' / ' + str(a)