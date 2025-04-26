class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    

    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height
    
    def set_width(self, height):
        self.__height = height

    
    def area(self):
        area = self.__height * self.__width
        return area
    
    def Perimetr(self):
        Perimetr = (self.__height + self.__width)*2
        return Perimetr
    
    def print_detalis(self):
        # area = area()
        # Perimetr = Perimetr()
        print("Width: ", self.__width, "Height: ", self.__height)

rect1 = Rectangle(2,5)
rect1.print_detalis()
