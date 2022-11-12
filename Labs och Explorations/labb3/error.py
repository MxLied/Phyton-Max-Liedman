###OLD
from __future__ import annotations
import matplotlib.pyplot as plt
import math

class Mother_Class_Of_Shapes:
    def __init__(self):

        self.area = 0
        self.circumference = 0
        
#######################transalte
    def transalte(self, x_offsett, y_offsett):
     if not isinstance(x_offsett, (int, float)):
        raise TypeError("you have to input a int or a float ")

     if not isinstance(y_offsett, (int, float)):
        raise TypeError("you have to input a int or a float ")
     self.center_point_x = x_offsett
     self.center_point_y = y_offsett


#### OVERLOADERS

####compares areas of shapes

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other): 
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area






##############################################################
    def print_area(self):
        return print(f"The shapes area =: {self.area}")

    def print_circumfernce(self):
        return print(f"The shapes area =: {self.cirumfernce}")


    def __repr__(self) -> str:
        return (f"This class has no function on its own, the values represent a X and a Y value in a coordinate system")
    
    def __str__(self) -> str:
        return (f"Hi user, this class has no function for you. Try: newRectangle = Rectangle(2, 2, 0, 0) or, newcircle = Circle(1,1,1)")
############################################################
#GETTER SETTER X
@property
def center_point_x(self):
    return self._center_point_x

@center_point_x.setter
def center_point_x(self, value:float | int):
    if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")

#GETTER SETTER y
@property
def center_point_y(self):
    return self._center_point_y

@center_point_y.setter
def center_point_y(self, value:float | int):
    if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")
























###############################################################################################
###############################################################################################
class Circle(Mother_Class_Of_Shapes):
    def __init__(self, radius:float, center_point_x: float, center_point_y: float):

        self.center_point_x = center_point_x
        self.center_point_y = center_point_y
        self.radius = radius


        
######GETTER SETTER radius
    
    @property
    def radius(self) -> (int | float):
        """radius"""
        return self._radius
         
    @radius.setter
    def radius(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")
        self._radius = value
        self.calc_area()
        self.calc_circumference()

            
        
 ####################################################################               
        
    def calc_area(self):
        print("calling calc area")
        self.area = math.pi * (self.radius**2)
    
    
    def calc_circumference(self):
        print("calling calc circum")
        self.circumference = (math.pi*2) * (self.radius)


    def plot(self, color = 'k'):
        """plots circle"""
        circle_plot_object = plt.Circle((self.center_point_x, self.center_point_y), self.radius, color = color, alpha=0.7)
        
        fig = plt.gcf()
        ax = fig.gca()

        ax.add_patch(circle_plot_object)
        return ax
    
    def point_plot(self, point_x_positioner, point_y_positioner):
        """"plots a point and calculates distance"""
        single_plot_point = plt.plot(point_x_positioner,point_y_positioner,'bo') 

        ## Calculates ecludian
        dista = math.dist((self.center_point_x, self.center_point_y), (point_x_positioner, point_y_positioner))
        
        if (dista < self.radius):
            print(f"The distance from the center of circle is :{dista} uints, the point is inside of the circle")
        else: 
            print(f"The distance from the center of circle is :{dista} units")
    
    def is_unit_circle(self):
        return (self.center_point_y | self.center_point_x == 0) and (self.radius == 1) ##bool
        
            
###################################################################


######################################################
######################################## Reper and Str
    def __repr__(self):
        return (self.center_point_x,self.center_point_y, self.radius) 

    def __str__(self) -> str:
        return (f"Circle X-position is: {self.center_point_x} Y-position is: {self.center_point_y}  the radius {self.radius} the area {self.area} the circumference {self.circumference}")


##############################################################################################################################################################################################
################################################### RECTANGLE ###########################################################################################################################################

class Rectangle(Mother_Class_Of_Shapes): 
    """Creates rectangle, plots rectangle calculates area, calculates circumference"""
    def __init__(self, height:float, width:float ,center_point_x: float, center_point_y: float):

        self.center_point_x = center_point_x
        self.center_point_y = center_point_y
        self.height = height
        self.width = width

    #GETTER SETTER width
    #GETTER SETTER width
    @property
    def width(self) -> (int | float):
        """Width of rectangle"""
        return self._width

    @width.setter
    def width(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")
        self._width = value
        self.calc_area()
        self.calc_circumference()
            

    #GETTER SETTER height
    @property
    def height(self) -> (int | float):
        """Width of rectangle"""
        return self._height

    @height.setter
    def height(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")
        self._height = value
        self.calc_area()
        self.calc_circumference()

    

    def calc_area(self):
        print("calling calc area")
        self.area = self.height*self.width
    
    def calc_circumference(self):
        print("calling calc circum")
        self.circumference = self.height*2+self.width*2   

 ##  ####################################################################### Check if it is a square 

    def is_square(self):
        return self.width == self.height

    def Sqaure_checker(self):
        if self.width == self.height:
            print("It is a perceft square")
        else: 
            print("It is a rectangle but not a square")
        
########################################################### ## creates rectangle in matplotlib
##########################################################  ### colour = coloring of rectangle as example, newRectangle.plot('b') defualt colour is black 
    def plot(self, colour = 'k'):
        """plots circle"""

        cornor_of_x = self.center_point_x -(self.width/2)
        cornor_of_y = self.center_point_y -(self.height/2)
    
        x_list = [cornor_of_x, cornor_of_x, self.width + cornor_of_x, self.width + cornor_of_x, cornor_of_x]
        
        y_list = [cornor_of_y, cornor_of_y + self.height, cornor_of_y + self.height, cornor_of_y, cornor_of_y]

        plt.plot(x_list, y_list, c = colour, alpha = 0.7)

# ## ## looks if two rectangles are the same size
#     def __eq__(self, value): ##  Code heavily inspierd by Daniel Nillson: exercise 12 fractions
#         if (self.width == value.width) and (self.height == value.height):
#             return print("The two rectangles are the SAME size")
#         else: return print ("The two rectangles are NOT the same size")

###############################################################################################################
##############################################################################################

    def point_plot(self, point_x_positioner, point_y_positioner):

        ## plotter
        single_plot_point = plt.plot(point_x_positioner,point_y_positioner,'bo') 
        
        ##  Andreas Svensson hjälpte mig ↓↓↓↓
        ### 
        if  (self.center_point_x - self.width/2  <= point_x_positioner <= self.center_point_x + self.width/2 and 
             self.center_point_y - self.height/2  <= point_y_positioner <= self.center_point_y + self.height/2 ):
            print("punkten är inom rektangeln")

############################################################################
#------------------------------------------------------------------------REPER----STR
    def __repr__(self):
        return (self.width, self.height), (self.center_point_x),(self.center_point_y)

    def __str__(self) -> str: ##
        return f"width is: {self.width} and height is: {self.height}, X-position is: {self.center_point_x} Y-position is: {self.center_point_y} the area {self.area} the circumference {self.circumference}"













#################################################################

        
cirkel1 = Circle(1,0,0) # Enhetscirkel
cirkel2 = Circle(10,2,1)
print(cirkel1)
print(cirkel2)

cirkel1.print_area()
cirkel2.print_area()

print(cirkel1 == cirkel2)
print(cirkel1 != cirkel2)
print(cirkel1 < cirkel2)
print(cirkel1 > cirkel2)
print(cirkel1 >= cirkel2)
print(cirkel1 <= cirkel2)

###########################################################################################




rectangle1 = Rectangle(1,1,0,0) # Enhetscirkel
rectangle2 = Rectangle(10,10,0,0)
print(rectangle1)
print(rectangle2)

rectangle1.print_area()
rectangle2.print_area()

print(rectangle1 == rectangle2)
print(rectangle1 != rectangle2)
print(rectangle1 < rectangle2)
print(rectangle1 > rectangle2)
print(rectangle1 >= rectangle2)
print(rectangle1 <= rectangle2)