#!/usr/bin/python3

"""Define a rectangle"""


class Rectangle:
    """representation of rectangle"""

    def __init__(self, width=0, height=0):
        """initializing the rectangle by
        setting object of width and height"""

        self.width = width
        self.height = height

        @property
        def width(self):
            """getter for private instance for attribute width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter for private instance attribute for width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
                self.__width = value

        @property
        def height(self):
            """getter for private instance attribute for height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for private instance attribute for height"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
                self.__height = value
