#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:12:49 2020

@author: elliebear
"""





class Person():
    def __init__(self, name, birthyear, birthmonth, birthdate):
        import datetime
        self.name = name
        self.birth_day = datetime.datetime(birthyear, birthmonth, birthdate)
        
    # Define greeting function
    def greeting(self):
        return f'Hello {self.name}.'
    import datetime
    
    
    
    # Define function that returns number of seconds on Earht
    def seconds(self):
        import datetime
        current_time = datetime.datetime.now()
        current_year = current_time.year
        
        time = (current_year - self.birth_day) * 60 * 60 * 24 * 365.25
        return f'{self.name} have spent {time} seconds on Earth'
        
ellie = Person('Ellie', 2006, 8, 26)
print(ellie.seconds())





