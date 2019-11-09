#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# This is the brute force approach. Starting from the top, check the values with or without items that do not exceed capacity.
def knapsack_solver(items, capacity):

    def get_Total(items):                           #get the values of all items
        return sum(item.value for item in items)       

    def get_subset(n, c):

        if n < 0 or c <= 0:                         #base case (no more items in list or no more capacity)
            return []

        if items[n].size > c:                       #if item size already exceeds capacity, skip
            return get_subset(n - 1, c)

        else:                                       
            wo_item = get_subset(n - 1, c)
            with_item = [items[n]] + get_subset(n - 1, c - items[n].size)
            
            if get_Total(with_item) > get_Total(wo_item):     #compare total values with or without item
                return with_item
            else:
                return wo_item
   
    n = len(items) - 1
    results = get_subset(n, capacity)
    value = sum(item.value for item in results)     #sum values of all items in results
    chosen = [item.index for item in results]       
    chosen.sort()                                   #order items by index
    return {'Value': value, 'Chosen': chosen}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))
        
        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')