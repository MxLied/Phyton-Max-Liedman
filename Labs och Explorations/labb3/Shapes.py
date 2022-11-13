""""
Koden är rätt drastiskt förändrad. Med ökad och nya funkonaliteter. Area och omkretes defineras i moder klassen.
Jämnföresler fungerar som det ska, 
gjort kod mer logisk och lättläst 


"""




from __future__ import annotations
import matplotlib.pyplot as plt
import math

class Mother_Class_Of_Shapes:
    def __init__(self):
        
        self.area = 0
        self.circumference = 0
        
#------------transaltion method------------#
    def transalte(self, x_offsett, y_offsett):
     if not isinstance(x_offsett, (int, float)):
        raise TypeError("you have to input a int or a float ")

     if not isinstance(y_offsett, (int, float)):
        raise TypeError("you have to input a int or a float ")
     self.center_point_x = x_offsett
     self.center_point_y = y_offsett


#### OVERLOADERS

#--------compares areas of shapes--------#

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
        return print(f"The shapes area = {self.area}")

    def print_circumference(self):
        return print(f"The shapes area = {self.circumference}")


    def __repr__(self) -> str:
        return (f"This class has no function on its own, the values represent a X and a Y value in a coordinate system")
    
    def __str__(self) -> str:
        return (f"Hi user, this class has no function for you. Try: newRectangle = Rectangle(2, 2, 0, 0) or, newcircle = Circle(1,1,1)")

############################################################
#-----------------property OF X-----------------#
@property
def center_point_x(self):
    return self._center_point_x

@center_point_x.setter
def center_point_x(self, value:float | int):
    if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")

#-----------------property OF y-----------------#
@property
def center_point_y(self):
    return self._center_point_y

@center_point_y.setter
def center_point_y(self, value:float | int):
    if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")



##---------------------CIRCLE CLASS STARTS HERE---------------------#


###############################################################################################
class Circle(Mother_Class_Of_Shapes):
    def __init__(self, radius:float, center_point_x: float, center_point_y: float):

        self.center_point_x = center_point_x
        self.center_point_y = center_point_y
        self.radius = radius


        
#-----------------GETTER SETTER radius-----------------#
    
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
        #######------ calculations for area and circumference----######
    def calc_area(self):
        self.area = math.pi * (self.radius**2)
    
    
    def calc_circumference(self):
        self.circumference = (math.pi*2) * (self.radius)

#---------------------plots circle-------------------#
    def plot(self, color = 'k'):
        """plots circle"""
        circle_plot_object = plt.Circle((self.center_point_x, self.center_point_y), self.radius, color = color, alpha=0.7)
        
        fig = plt.gcf()
        ax = fig.gca()

        ax.add_patch(circle_plot_object)
        return ax

#----------------------plots a point and calculates the distance from circle center------------------------#    
    def point_plot(self, point_x_positioner, point_y_positioner):
        """"plots a point and calculates distance"""
        single_plot_point = plt.plot(point_x_positioner,point_y_positioner,'bo') 

        ## Calculates ecludian
        dista = math.dist((self.center_point_x, self.center_point_y), (point_x_positioner, point_y_positioner))
        
        if (dista < self.radius):
            print(f"The distance from the center of circle is :{dista} uints, the point is inside of the circle")
        else: 
            print(f"The distance from the center of circle is :{dista} units")

#---------------------looks if circle is a unit circle, returns True or False-------------------------#    
    def is_unit_circle(self):
        return (self.center_point_y | self.center_point_x == 0) and (self.radius == 1) ##bool
        
            


#---------------------------#
#------ Reper and Str ------#

    def __repr__(self):
        return  (f"X-position: {self.center_point_x} Y-position: {self.center_point_y} Radius: {self.radius} Area {self.area} Circumference {self.circumference}")

    def __str__(self) -> str:
        return (f"Circle X-position is: {self.center_point_x} Y-position is: {self.center_point_y}  the radius {self.radius} the area {self.area} the circumference {self.circumference}")


##############################################################################################################################################################################################


#----------------------------------------RECTANGLE CLASS STARTS HERE ----------------------------------------#

class Rectangle(Mother_Class_Of_Shapes): 
    """Creates rectangle, plots rectangle calculates area, calculates circumference"""
    def __init__(self, height:float, width:float ,center_point_x: float, center_point_y: float):

        self.center_point_x = center_point_x
        self.center_point_y = center_point_y
        
    #user might want to change widh and also have correct calculations on area and circumference if printed
    #solution: width and height a defualt value of 0 so it "update" the area and circumference
        # not sure why this is working, 
        self._height = 0
        self._width = 0

        self.height = height
        self.width = width


#--------------#Getter Setter Width#--------------#
    @property
    def width(self) -> (int | float):
        """Width of rectangle"""
        return self._width

    @width.setter
    def width(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")
        self._width = value
        #check if height is set
        self.calc_area() 
        self.calc_circumference()
            

#--------------#Getter Setter Height#--------------#
    @property
    def height(self) -> (int | float):
        """Width of rectangle"""
        return self._height 

    @height.setter
    def height(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be a number, not {type(value)}")
        self._height = value
         #check if width is set
        self.calc_area()
        self.calc_circumference()

    
#-------------------Calculates circumference and area --------------------#
    def calc_area(self):
        self.area = self.height*self.width
    
    def calc_circumference(self):
        self.circumference = self.height*2+self.width*2   

#-------------------Check if it is a square --------------------#

    def is_square(self):
        return self.width == self.height

    def Sqaure_checker(self):
        if self.width == self.height:
            print("It is a perceft square")
        else: 
            print("It is a rectangle but not a square")
        
#------------------- plots rectangle ----------------------------- #

    def plot(self, colour = 'k'):
        """plots circle"""

        cornor_of_x = self.center_point_x -(self.width/2)
        cornor_of_y = self.center_point_y -(self.height/2)
    
        x_list = [cornor_of_x, cornor_of_x, self.width + cornor_of_x, self.width + cornor_of_x, cornor_of_x]
        
        y_list = [cornor_of_y, cornor_of_y + self.height, cornor_of_y + self.height, cornor_of_y, cornor_of_y]

        plt.plot(x_list, y_list, c = colour, alpha = 0.7)


#---------------------plots a point, and cheks if point is inside a square--------------------#
    def point_plot(self, point_x_positioner, point_y_positioner):

        ## plotter
        plt.plot(point_x_positioner,point_y_positioner,'bo') 
        
        ##  Andreas Svensson hjälpte mig ↓↓↓↓
        ### 
        
        if  (self.center_point_x - self.width/2  <= point_x_positioner <= self.center_point_x + self.width/2 and 
             self.center_point_y - self.height/2  <= point_y_positioner <= self.center_point_y + self.height/2 ):
            print("punkten är inom rektangeln")


#--------------------------------     #REPER----STR#    -----------------------------------------------------------------------
    def __repr__(self):
        return f"width: {self.width}, height: {self.height}, X-position: {self.center_point_x}, Y-position:, {self.center_point_y}, Area: {self.area}, Circumference: {self.circumference}"

    def __str__(self) -> str: ##
        return f"width is: {self.width} and height is: {self.height}, X-position is: {self.center_point_x} Y-position is: {self.center_point_y} the area: {self.area} the circumference: {self.circumference}"