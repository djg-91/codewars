'''
https://www.codewars.com/kata/52597aa56021e91c93000cb0

    Write an algorithm that takes an array and moves all of the zeros to the end, 
    preserving the order of the other elements.

    moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
'''


def move_zeros(array):
    return [a for a in array if a is not 0 and str(a) != '0.0'] + [a for a in array if a is 0 or str(a) == '0.0' ] 