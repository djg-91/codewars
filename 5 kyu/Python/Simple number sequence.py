'''
https://www.codewars.com/kata/5a28cf591f7f7019a80000de

    In this Kata, you will be given a string of numbers in sequence and your task will be to return the missing number. 
    If there is no number missing or there is an error in the sequence, return -1.

    For example:

        missing("123567") = 4 
        missing("899091939495") = 92
        missing("9899101102") = 100
        missing("599600601602") = -1 -- no number missing
        missing("8990919395") = -1 -- error in sequence. Both 92 and 94 missing.

    The sequence will always be in ascending order.
'''


def missing(s):

    for i in range(len(s) // 2):

        missing_number = 0
        missing_times = 0
    
        start = s[0:i+1]

        s_test = s[len(start):]

        next = int(start) + 1
        next_2 = next + 1

        while len(s_test) > 0:
            if s_test.startswith(str(next)):
                s_test = s_test[len(str(next)):]
                next += 1
                next_2 = next + 1
            elif s_test.startswith(str(next_2)):
                missing_number = next
                missing_times += 1
                s_test = s_test[len(str(next_2)):]
                next = next_2 + 1
            else:
                break
                
        if len(s_test) == 0:
            return -1 if missing_number == 0 or missing_times > 1 else missing_number
    
    return -1