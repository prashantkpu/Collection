# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:44:50 2018

Developed by: Prashant Kumar Sharma
Tested by: Deepa I Belvi
"""

class Collection():
    def __init__(self):
        self.number_of_items = 0
        self.items = {}
        return
    def is_collection_empty(self):
        return self.number_of_items == 0
    def total_items(self):
        return self.number_of_items
    def is_present(self, value):
        return value in self.items
    def frequency(self, value):
        return self.items.get(value, 0)
    def add(self, value):
        if value in self.items:
            self.items[value] += 1
        else:
            self.items[value] = 1
        self.number_of_items += 1
        return
    def remove(self, value):
        if value in self.items:
            if self.items[value] == 1:
                self.items.pop(value, None)
            else:
                self.items[value] -= 1
            self.number_of_items -= 1
        return
    def most_frequent(self):
        most_occurring = []
        highest_occurrance = 0
        for key in self.items:
            if len(most_occurring) == 0 or self.items[key] > self.items[most_occurring[0]]:
                most_occurring = [key]     
            elif self.items[key] == self.items[most_occurring[0]]:
                most_occurring.append(key)
        if len(most_occurring) > 0:
            highest_occurrance = self.items[most_occurring[0]]
        return (most_occurring, highest_occurrance)
    def least_frequent(self):
        least_occurring = []
        smallest_occurrance = 0
        for key in self.items:
            if len(least_occurring) == 0 or self.items[key] < self.items[least_occurring[0]]:
                least_occurring = [key]     
            elif self.items[key] == self.items[least_occurring[0]]:
                least_occurring.append(key)
        if len(least_occurring) > 0:
            smallest_occurrance = self.items[least_occurring[0]]
        return (least_occurring, smallest_occurrance)
    def __repr__(self):
        temp_list = []
        for key in self.items:
            for i in range(self.items[key]):
                temp_list.append(key)
        return str(temp_list)
    def pretty_print(self):
        print("Items in the Collection are as follows:")
        for key in self.items:
            print("{} of {}".format(self.items[key], key))
        return 
