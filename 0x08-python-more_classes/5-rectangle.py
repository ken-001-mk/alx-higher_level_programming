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

        def area(self):
            """return the area of the rectangle"""
            self.__width * self.__height

        def perimeter(self):
            """return perimeter of the rectangle"""
            if self.__width == 0 0r self.__height == 0:
                return 0
            return (self.__width * 2) + (self.__height * 2)

        def __str__(self):
            """returns printable string representation of the rectangle"""
            string = ""
            if self.__width != 0 and self.__height != 0:
                string += "\n".join("#" * self.__width
                                    for j in range(self.__height))
                return string

        def __repr__(self):
            """return a string representation of rectangle for reproduction"""
            return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

        def __del__(self):
            """prints a string when an instance has been deleted"""
            print("Bye rectangle...")
