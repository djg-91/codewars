'''
https://www.codewars.com/kata/513e08acc600c94f01000001

    The rgb function is incomplete. Complete it so that passing in RGB 
    decimal values will result in a hexadecimal representation being returned. 
    Valid decimal values for RGB are 0 - 255. Any values that fall out of 
    that range must be rounded to the closest valid value.

    Note: Your answer should always be 6 characters long, the shorthand 
    with 3 will not work here.

    Examples (input --> output):

        255, 255, 255 --> "FFFFFF"
        255, 255, 300 --> "FFFFFF"
        0, 0, 0       --> "000000"
        148, 0, 211   --> "9400D3"
'''


def rgb(r, g, b):
    rgb_list = []
    for n in [r, g, b]:
        if n < 0:
            rgb_list += [0]
        elif n > 255:
            rgb_list += [255]
        else:
            rgb_list += [n]

    return ''.join([ format(a, '#04x')[2:].upper() for a in rgb_list ])