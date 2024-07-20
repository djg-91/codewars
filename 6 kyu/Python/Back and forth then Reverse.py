'''
https://www.codewars.com/kata/60cc93db4ab0ae0026761232

    Task
        A list S will be given. You need to generate a list T from it by following the given process:

        Remove the first and last element from the list S and add them to the list T.
        Reverse the list S
        Repeat the process until list S gets emptied.
        The above process results in the depletion of the list S. Your task is to generate list T without mutating the input List S.

    Example
        S = [1,2,3,4,5,6]
        T = []

        S = [2,3,4,5] => [5,4,3,2]
        T = [1,6]

        S = [4,3] => [3,4]
        T = [1,6,5,2]

        S = []
        T = [1,6,5,2,3,4]
        return T
    
    Note
        Size of S goes up to 10^6
        Keep the efficiency of your code in mind.
        Do not mutate the Input.
'''


from collections import deque


def arrange(s):
    S = deque(s)
    T = []
    reverse = False
    
    while S:
        T.append(S.popleft() if not reverse else S.pop())
        if S:
            T.append(S.pop() if not reverse else S.popleft())
        reverse = not reverse
    
    return T