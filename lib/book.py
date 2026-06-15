#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1


    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print(f"Turned page to {self.current_page}.")
        else:
            print("You're already at the last page!")


        

        
    
        