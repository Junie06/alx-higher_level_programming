#!/usr/bin/python3
def no_c(my_string):
    filter = [char for i in my_string if char != 'c' and x != 'C']
    return "".join(filter)
