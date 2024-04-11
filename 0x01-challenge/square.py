#!/usr/bin/python3
"""
A module for a class square
"""


class Square():
    """
    A class for a square
    """    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """
        A method for a class square
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """
        A method for a class square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        A method for a class square
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
