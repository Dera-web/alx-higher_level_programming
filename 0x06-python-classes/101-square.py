#!/usr/bin/python3
"""task 8: based on 6-square.py, add method
for print class that acts like my_print
"""


class Square():
    """private instance field(variable) -> __size
    # class accept optional argument size
    # alse implement exception with specific msgs
    Author : A. Hesham
    # public method area acces other method's private field
    2 extra methods to get and set __size
    method to print square if __size > 0
    """

    def __init__(self, size=0, position=(0, 0)):
        """ intialize instance """
        self.__size = size
        self.__position = position

    def area(self):
        """access another public method'instance attribute
        size and calculate the area of square
        """
        return (self.__size ** 2)

    @property  # Decorator for a method to define
    def size(self):  # a getter method for a property.
        """ __size getter """
        return (self.__size)

    @size.setter  # Decorator for a method to define  a setter method
    def size(self, value):  # for a (field type) property (size).
        """ __size setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ position field getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """
        for idx, val in enumerate(value):
            msg = "position must be a tuple of 2 positive integers"
            if (type(val) != int or val < 0 or idx > 1 or
                    type(value) != tuple or len(value) != 2):
                raise TypeError(msg)
                return
        self.__position = value

    def my_print(self):
        """ print square using #'s in stdout
        and won't print anything if size = 0
        position = (x, y)
        self.__position[0] = shift in x axis
        self.__position[1] = shift in y axis
        """
        if self.__size > 0:
            for spc in range(self.__position[1]):
                print("")
            for Vunit in range(self.__size):
                for spc in range(self.__position[0]):
                    print(" ", end="")
                for Hunit in range(self.__size):
                    print("#", end="")
                print("\n", end="")
        else:  # size == 0 then print new line
            print("")

    def __str__(self):
        """ handle print(square class)
        like my_print method
        print square using #'s in stdout
        and won't print anything if size = 0
        position = (x, y)
        self.__position[0] = shift in x axis
        self.__position[1] = shift in y axis
        """
        if self.__size > 0:
            for spc in range(self.__position[1]):
                print("")
            for Vunit in range(self.__size):
                for spc in range(self.__position[0]):
                    print(" ", end="")
                for Hunit in range(self.__size):
                    print("#", end="")
                print("\n", end="")
        else:  # size == 0 then print new line
            print("")
        return ("")  # must return string type
