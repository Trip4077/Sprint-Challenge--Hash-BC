#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Store all the Tickets in a hashtable using source as key
    for i in range( length ):
        hash_table_insert( hashtable, tickets[i].source, tickets[i] )

    # Get the starting Ticket for route
    current_ticket = hash_table_retrieve( hashtable, 'NONE' )
    #Numer of Tickets inserted in Route
    count = 0

    # Add the current ticket's destination to route list and move to next ticket
    while current_ticket.destination != "NONE":
        route[count] = current_ticket.destination
        count += 1

        current_ticket = hash_table_retrieve( hashtable, current_ticket.destination )
    
    # Add final destination to list
    route[count] = current_ticket.destination
   
    return route
