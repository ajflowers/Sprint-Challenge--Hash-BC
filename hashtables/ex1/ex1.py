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

    for i in range(len(weights)):
        # print(i)
        hash_table_insert(ht, weights[i], i)
        #insert weight as key, weight's index as value

    for i in range(len(weights)):
        weight = weights[i]
        target = limit - weight
        index = hash_table_retrieve(ht, target)

        if index is not None:
            return(index, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
