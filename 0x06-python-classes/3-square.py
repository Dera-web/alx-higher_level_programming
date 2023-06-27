#!/usr/bin/python3
"""task 3 """


class Square():
    """# task 3 , private instance field(variable)
    # class accept optional argument size
    # alse implement exception with specific msgs
    # public method area acces other method's private field
    """

    def __init__(self, size=0):
        """ intialize instance """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """access another public method'instance attribute
        size and calculate the area of square
        """
        return (self.__size ** 2)
