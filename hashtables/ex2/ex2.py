#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

table = {}
def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None] * length
    table = {}
    for t in tickets:
        table[t.source] = t.destination
    next = table["NONE"]

    for i in range(0, length):
        route[i] = next
        next = table[next]

    # Your code here

    return route


