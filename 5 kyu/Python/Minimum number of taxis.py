'''
https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d

    You work at a taxi central.
    People contact you to order a taxi. They inform you of the 
    time they want to be picked up and dropped off.

    A taxi is available to handle a new customer 1 time unit 
    after it has dropped off a previous customer.

    What is the minimum number of taxis you need to service all requests?

    Constraints:

        Let N be the number of customer requests:
        N is an integer in the range [1, 100k]
        All times will be integers in range [1, 10k]
        Let PU be the time of pickup and DO be the time of dropoff
        Then for each request: PU < DO
        The input list is NOT sorted.

    Examples:

        # Two customers, overlapping schedule. Two taxis needed.
        # First customer wants to be picked up 1 and dropped off 4.
        # Second customer wants to be picked up 2 and dropped off 6.
        requests = [(1, 4), (2, 6)]
        min_num_taxis(requests) # => 2

        # Two customers, no overlap in schedule. Only one taxi needed.
        # First customer wants to be picked up 1 and dropped off 4.
        # Second customer wants to be picked up 5 and dropped off 9.
        requests = [(1, 4), (5, 9)]
        min_num_taxis(requests) # => 1
'''


def min_num_taxis(requests):
    from heapq import heappush, heappop

    taxis = [-1]
    for start, end in sorted(requests):
        if taxis[0] < start:
            heappop(taxis)
        heappush(taxis, end)
    return len(taxis)