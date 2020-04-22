#Hash Table
import random

class hashtable:

    def __init__(self, tablesize):

        self.table = [0 for i in range (tablesize)]
        self.collusion = 0


    def hash_function(self, x):

        return x % len(self.table)


    def insert(self, x):

        if (self.table[self.hash_function(x)] == 1):
            self.collusion += 1
            return True

        else:
            self.table[self.hash_function(x)] = 1
            return False


def test(size, numOfInsert):

    h = hashtable(size)
    for i in range (numOfInsert):
        number = random.randint(0,10000)
        h.insert(number)
    return h.collusion


print(test(203,50))
