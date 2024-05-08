'''
https://www.codewars.com/kata/51fc12de24a9d8cb0e000001

    ISBN-10 identifiers are ten digits long. The first nine characters 
    digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.

    An ISBN-10 number is valid if the sum of the digits multiplied 
    by their position modulo 11 equals zero.

    For example:

        ISBN     : 1 1 1 2 2 2 3 3 3  9
        position : 1 2 3 4 5 6 7 8 9 10
        This is a valid ISBN, because:

       (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
  
    Examples

        1112223339   -->  true
        111222333    -->  false
        1112223339X  -->  false
        1234554321   -->  true
        1234512345   -->  false
        048665088X   -->  true
        X123456788   -->  false
'''


from string import ascii_uppercase

def valid_ISBN10(isbn):
    if len(str(isbn)) != 10:
        return False
    for x in isbn[:-1]:
        if x.upper() in ascii_uppercase:
            return False

    count = 0
    print(isbn)
    for x, y in enumerate([10 if x == 'X' else x for x in isbn], 1):
        count += x * int(y)

    return count % 11 == 0