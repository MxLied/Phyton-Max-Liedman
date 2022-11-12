from __future__ import annotations
import matplotlib.pyplot as plt
import math

class Mother_Class_Of_Shapes:
    def __init__(self, center_point_x:float, center_point_y:float):
        self.center_point_x = center_point_x
        self.center_point_y = center_point_y
        self.area = 0

#######################transalte
    def transalte(self, x_offsett, y_offsett):
     if not isinstance(x_offsett, (int, float)):
        raise TypeError("you have to input a int or a float ")

     if not isinstance(y_offsett, (int, float)):
        raise TypeError("you have to input a int or a float ")
     self.center_point_x = x_offsett
     self.center_point_y = y_offsett


#### OVERLOADERS

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __ne__(self, other): 
        return self.area != other.area





        
##############################################################
 
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



############################################################################OVERLOADERS
def __repr__(self) -> str:
        return (f"This class has no function on its own, the values represent a X and a Y value in a coordinate system")
    
def __str__(self) -> str:
        return (f"Hi user, this class has no function for you. Try: newRectangle = Rectangle(2, 2, 0, 0) or, newcircle = Circle(1,1,1)")

###############################################################################################
###############################################################################################














# CIRCLE CIRCLE CIRCLE
class Circle(Mother_Class_Of_Shapes):
    def __init__(self, radius:float, center_point_x: float, center_point_y: float):
        super().__init__(center_point_x, center_point_y)
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
        self.area = {math.pi * self.radius**2} 
 ####################################################################               

    def circle_area(self):
        """calculates area"""
        return print(f"The area is of the circle equals: {math.pi * self.radius**2}")
    
    def circle_circumference(self):
        """calculates circumference"""
        return print(f"The circumference is of the circle equals: {2 * math.pi * self.radius**2}")


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
        """checks if circle is a unit circle"""
        if ((self.center_point_y | self.center_point_x == 0) and (self.radius == 1)):
            print("Its a unit-circle")

    def __eq__(self, value): ##  Code heavily inspierd by Daniel Nillson: exercise 12 fractions
        """check if circle is the same size"""
        if (self.radius == value.radius):
            return print("The two Circles are the SAME size")
        else: return print ("The two Circles are NOT the same size")
###################################################################

######################################## Reper and Str
    def __repr__(self):
        return (self.center_point_x,self.center_point_y, self.radius) 

    def __str__(self) -> str:
        return (f"Circle X-position is: {self.center_point_x} Y-position is: {self.center_point_y}  the radius {self.radius}")


##############################################################################################################################################################################################
################################################### RECTANGLE ###########################################################################################################################################




# RECTANGLE RECTANGLE


class Rectangle(Mother_Class_Of_Shapes): 
    """Contains: area/circumference calculator, plotter: creates depending on input a rectangle or square: checks if point in square, checks if square, checks is two squares the same """
    def __init__(self, height:float, width:float ,center_point_x: float, center_point_y: float, ):
        super().__init__(center_point_x, center_point_y)
        
        self.height = height
        self.width = width
        


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
        self.height*self.width
        self.area = {self.height*self.width} 
            

    #GETTER SETTER height
    @property
    def height(self) -> (int | float):
        """Width of rectangle"""
        return self._width
         

    @height.setter
    def height(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")
        self._height = value
        self.height*self.width
        self.area = {self.height*self.width} 
    

    
 ##  ##################################################################### calculates area
    def rectangle_area(self):
        """calculates area"""
        print("The Area of the square is:")
        return self.height*self.width

 ##  ###################################################################### Calucalte circumference
    def rectangle_circumference(self):
        """calculates circumference"""
        print("The circumference is:")
        return self.height*2+self.width*2

 ##  ####################################################################### Check if it is a square 
    def Sqaure_checker(self):
        """checks if shape is a perfect square"""
        if self.width == self.height:
            return print("It is a perceft square")
        else: return print("It is a rectangle but not a square")
        
########################################################### ## creates rectangle in matplotlib
##########################################################  ### colour = coloring of rectangle as example, newRectangle.plot('b') defualt colour is black 
    def plot(self, colour = 'k'):
        """plots rectanagle"""

        cornor_of_x = self.center_point_x -(self.width/2)
        cornor_of_y = self.center_point_y -(self.height/2)
    
        x_list = [cornor_of_x, cornor_of_x, self.width + cornor_of_x, self.width + cornor_of_x, cornor_of_x]
        
        y_list = [cornor_of_y, cornor_of_y + self.height, cornor_of_y + self.height, cornor_of_y, cornor_of_y]

        plt.plot(x_list, y_list, c = colour, alpha = 0.7)

## ## looks if two rectangles are the same size
    def __eq__(self, value): ##  Code heavily inspierd by Daniel Nillson: exercise 12 fractions
        """checks if two rectangle are the same size"""
        if (self.width == value.width) and (self.height == value.height):
            return print("The two rectangles are the SAME size")
        else: return print ("The two rectangles are NOT the same size")

###############################################################################################################
##############################################################################################

    def point_plot(self, point_x_positioner, point_y_positioner):
        """checks if a point is withn the rectangle"""
            
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
        return f"width is: {self.width} and height is: {self.height}, X-position is: {self.center_point_x} Y-position is: {self.center_point_y}"