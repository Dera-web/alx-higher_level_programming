#!/usr/bin/python3
"""task 6: based on 5-square.py, add method
for private instance field "position
with getter and setters with specific conditions
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

    def my_print(self):
        """ print square using #'s in stdout
        and won't print anything if size = 0
        """
        if self.__size > 0:
            for Vunit in range(self.__size):
                if self.__position[1] == 0:
                    for spc in range(self.__position[0]):
                        print(" ", end="")
                for Hunit in range(self.__size):
                    print("#", end="")
                print("\n", end="")
        else:  # size == 0 then print new line
            print("")

    @property
    def position(self):
        """ position field getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """
        for idx, val in enumerate(value):
            if type(val) != int or val < 0 or idx > 1:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
                return
        self.__position = value
