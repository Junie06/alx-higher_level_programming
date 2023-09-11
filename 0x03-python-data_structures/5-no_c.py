#!/usr/bin/python3
def no_c(my_string):
    filter = [x for i in my_string if x != 'c' and x != 'C']
    print("{}".format(my_string))
