
table = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    for i in range(len(weights)):
        table[weights[i]] = i
    print(table)
    for i in range(len(weights)):
        dif = limit - weights[i]
        if dif in table:
            return(max(i,table[dif]), min(i,table[dif]))
    
    return None

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21
get_indices_of_item_weights(weights,length,limit)