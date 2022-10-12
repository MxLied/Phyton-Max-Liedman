import matplotlib.pyplot as plt
import math

class Circle():
    def __init__(self, radius, center_point_x,  center_point_y ):
        self.radius = radius
        self.center_point_x = center_point_x
        self.center_point_y = center_point_y

    
    def circle_area(self):
        return print(math.pi * self.radius**2)
    
    def circle_circumference(self):
        return print(2 * math.pi * self.radius**2)

     ##  ## moves square in axis 
    def transalte(self, x_offsett, y_offsett):
        self.center_point_x = x_offsett
        self.center_point_y = y_offsett

    def plot(self, color = 'k'):
        print("plotter is running")
        circle_plot_object = plt.Circle((self.center_point_x, self.center_point_y), self.radius, color = color, alpha=0.7)
        
        fig = plt.gcf()
        ax = fig.gca()

        ax.add_patch(circle_plot_object)
        return ax
    
    def point_plot(self, point_x_positioner, point_y_positioner):
        ## plotter
        single_plot_point = plt.plot(point_x_positioner,point_y_positioner,'bo') 

        ## Calculates ecludian
        dista = math.dist((self.center_point_x, self.center_point_y), (point_x_positioner, point_y_positioner))
        
        if (dista < self.radius):
            print(f"The distance from the center of circle is :{dista} uints, the point is inside of the circle")
        else: 
            print(f"The distance from the center of circle is :{dista} units")
    
    def is_unit_circle(self):
        if ((self.center_point_y | self.center_point_x == 0) and (self.radius == 1)):
            print("Its a unit-circle")

    def __eq__(self, value): ##  Code heavily inspierd by Daniel Nillson: exercise 12 fractions
        if (self.radius == value.radius):
            return print("The two Circles are the SAME size")
        else: return print ("The two Circles are NOT the same size")
        

cirkel1 = Circle(1,0,0)
# cirkel2 = Circle(1,0,0)
# print(f" {cirkel1} == {cirkel2}, {cirkel1 == cirkel2}")
# cirkel2.plot("r")
cirkel1.is_unit_circle()
cirkel1.circle_area()
cirkel1.circle_circumference()



#cirkel1.plot()



plt.axis([-5, 5, -5, 5])
ax = cirkel1.plot()
cirkel1.point_plot(4.5,3)
ax.set_aspect(1)
plt.show()


# cirkel1.plot()
# plt.axis([-5, 5, -5, 5])

# plt.axis([-5, 5, -5, 5])