from Shapes3D import Shapes3D
import math
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

class Cone(Shapes3D):
    def __init__(self, r, h, num_points):
        super().__init__('cone', 'red', 1)
        self.verticies_coordinates = []
        self.r = r
        self.h = h
        self.num_points = num_points

    def volume(self):
        volume = math.pi * (self.r ^ 2) * (self.h / 3)
        return round(volume, self.rounding)
    
    def surface_area(self):
        l = math.sqrt((self.r ^ 2) + (self.h ^ 2))
        surface_area = (math.pi * (self.r^2)) + (math.pi * self.r * l)
        return round(surface_area, self.rounding)

    def get_type(self) :
        return self.type
    
    def get_dimensions(self):
        return [self.r, self.h, self.num_points]
    
    def set_dimensions(self, new_r, new_h, new_num_points):
        self.r = new_r
        self.h = new_h
        self.num_points = new_num_points
    
    def get_colour(self):
        return self.colour
    
    def set_colour(self, new_colour):
        self.colour = new_colour
    
    def get_verticies(self):
        for point in range(1, self.num_points):
            numsides = 360/self.num_points
            coordinate = [round(self.r * math.cos(math.radians(point * numsides)), self.rounding), round(self.r * math.sin(math.radians(point * numsides)), self.rounding), 0]
            self.verticies_coordinates.append(coordinate)
        
        self.verticies_coordinates.append([0, 0, self.h])

        return self.verticies_coordinates

    
    def get_circumference(self):
        return round(2 * math.pi * self.r, self.rounding)
    
    def display(self):
        fig = plt.figure() 
        ax = fig.add_subplot(111, projection='3d') 
        
        z = np.linspace(0, self.h, self.num_points) 
        theta = np.linspace(0, 2 * np.pi, self.num_points) 
        theta_grid, z_grid = np.meshgrid(theta, z) 
        x_grid = self.r * (1 - z_grid / self.h) * np.cos(theta_grid) 
        y_grid = self.r * (1 - z_grid / self.h) * np.sin(theta_grid) 
        
        ax.plot_surface(x_grid, y_grid, z_grid, color=self.colour, alpha=0.7)

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title('3D Cone')
        
        ax.set_aspect('equal')
        plt.show()