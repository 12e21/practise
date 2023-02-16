class Box:
    name ="box_01"
    __length=1
    __width=2
    __height=3
    def __init__(self,lenth,width,height):
        self.__length=lenth
        self.__width=width
        self.__height=height
    def __calculate_volumn(self):
        return (self.__length*self.__width*self.__height)
    def get_volumn(self):
        return self.__calculate_volumn()
    def __add__(self, other):
        return Box(self.__length+other.__length,
                   self.__width+other.__width,self.__height+other.__height)

class Food_box(Box):
    load_food="bread"