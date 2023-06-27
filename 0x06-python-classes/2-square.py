#!/usr/bin/python3
""" task 2 """


class Square():
    """ task 2 , private nstance attribut + class accept arguments
    # define extra method to reassign values to size
    # but alse implement exception with specific msgs
    """

    def __init__(self, size=0):
        # intialize new sqr
        # A.Hesham
        # size must be of type int also > 0
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
