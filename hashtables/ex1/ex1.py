#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    # Pair not possible
    if length == 1: return None
    # Pair only
    if length == 2 and weights[0] + weights[1] == limit: return ( 1, 0 )

    # insert weights into hash table
    for i in range( length ):
        hash_table_insert( ht, i, weights[ i ] )

    # make copy of limit to prevent mutation
    # index of next value
    # number of loops, used as index of current value
    wlimit = limit
    i = 1
    loops = 0

    # while matching pair not found
    while wlimit != 0:
        # iterate loop once end is reached
        if i == length-1:
            loops += 1
            i = loops

        # Get values from hast table
        current_val = hash_table_retrieve( ht, loops )
        next_val = hash_table_retrieve( ht, i )
        
        # if wlimit is found return tuple
        if wlimit - current_val - next_val == 0:
            print( 'In Condition', (i, loops) )
            return ( i, loops )


        # iterate next value
        i += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# print( get_indices_of_item_weights( [ 4, 6, 10, 15, 16 ], 5, 21 ) )