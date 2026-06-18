#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size 
        self.price = price
        self.tips = 0

    @property
    def size (self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("Size must be 'Small', 'Medium', or 'Large'.")

        

    def tip(self, amount):
        self.tips += amount
        print(f"Added a tip of {amount}. Total tips:{self.tips}.")