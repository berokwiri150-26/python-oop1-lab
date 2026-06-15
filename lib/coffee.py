#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size 
        self.price = price
        self.tips = 0

    def tip(self, amount):
        self.tips += amount
        print(f"Added a tip of {amount}. Total tips:{self.tips}.")