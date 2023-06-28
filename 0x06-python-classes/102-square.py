#!/usr/bin/python3
"""task 9 : based on file 4*
Square instance can answer to comparators:
==, !=, >, >=, < and <= based on the value
of square area
"""


class Square():
    """private instance field(variable) -> __size
    # class accept optional argument size
    # alse implement exception with specific msgs
    Author : A. Hesham
    # public method area acces other method's private field
    2 extra methods to get and set __size
    """

    def __init__(self, size=0):
        """ intialize instance """
        self.__size = size

    def area(self):
        """access another public method'instance attribute
        size and calculate the area of square
        """
        return (self.__size ** 2)

    @property  # Decorator for a method to define
    def size(self):  # a getter method for a property.
        """ __size getter """
        return (self.__size)

    @size.setter  # Decorator for a method to define a setter method
    def size(self, value):  # for a (field type) property (size).
        """ __size field setter method code """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """  instance can answer to == comparator """
        if isinstance(other, Square):  # check other type is it Square
            return self.area() == other.area()
        return False

    def __gt__(self, other):  # gt -> greater than
        """  instance can answer to > comparator """
        if isinstance(other, Square):  # check other type is it Square
            return self.area() > other.area()
        return False

    def __lt__(self, other):  # lt -> less than
        """  instance can answer to < comparator """
        if isinstance(other, Square):  # check other type is it Square
            return self.area() < other.area()
        return False

    def __ne__(self, other):  # ne -> not equel
        """  instance can answer to == comparator """
        if isinstance(other, Square):  # check other type is it Square
            return self.area() != other.area()
        return False

    def __ge__(self, other):  # ge -> greater than or equal
        """  instance can answer to >= comparator """
        if isinstance(other, Square):  # check other type is it Square
            return self.area() >= other.area()
        return False

    def __le__(self, other):  # le -> less than or equal
        """  instance can answer to <= comparator """
        if isinstance(other, Square):  # check other type is it Square
            return self.area() <= other.area()
        return False
