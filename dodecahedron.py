from Shapes3D import Shapes3D
import math
import matplotlib.pyplot as plt

class Dodecahedron(Shapes3D):
    def __init__(self, a, b):
        super().__init__('dodecahedron', 'red', 1)
        self.a = a
        self.b = b

    def volume(self):
        volume = (((15 + 7 * math.sqrt(5))/4) * (self.a ^ 3), self.rounding)
        return volume
    
    def surface_area(self):
        surface_area = round((3 * math.sqrt(25 + 10 * math.sqrt(5))) * (self.a ^ 2), self.rounding)
        return surface_area

    def get_type(self) :
        return self.type
    
    def get_colour(self):
        return self.colour
    
    def set_colour(self, new_colour):
        self.colour = new_colour

    def get_dimensions(self):
        return [self.a, self.b]

    def get_verticies(self):
        
        verticies = ["(±1, ±1, ±1), (0, ±(1 + h), ±(1 − h2)), (±(1 + h), ±(1 − h2), 0) and (±(1 − h2), 0, ±(1 + h))"]

        return verticies
    
    def set_dimensions(self, new_a, new_b):
        self.a = new_a
        self.b = new_b
    
    def display(self):
        Φ = (1 + (5 ** (1 / 2))) / 2

        X_square = []
        Y_square = []

        points = [
            [Φ, Φ],
            [Φ, Φ * 2],
            [Φ * 2, Φ * 2],
            [Φ * 2, Φ],
        ]
        for pair in points:
            X_square.append(pair[0])
            Y_square.append(pair[1])
        X_square.append(points[0][0])
        Y_square.append(points[0][1])

        X_rectangle = []
        Y_rectangle = []

        height = ((Φ - 1) / 2) * self.a
        height2 = (1 / 2) * self.b

        points = [
            [Φ - height2, Φ + height],
            [Φ - height2, Φ * 2 - height],
            [Φ * 2 + height2, Φ * 2 - height],
            [Φ * 2 + height2, Φ + height]
        ]
        for pair in points:
            X_rectangle.append(pair[0])
            Y_rectangle.append(pair[1])
        X_rectangle.append(points[0][0])
        Y_rectangle.append(points[0][1])

        Z_wall = [0, 0, 0, 0, 0]

        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection="3d", proj_type="ortho")
        ax.set_box_aspect(aspect=(1, 1, 1))

        ax.plot(
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[0], X_rectangle[0], X_square[0]],
            [Y_square[0], Y_rectangle[0], Y_square[0]],
            c="k",
        )
        ax.plot(2 * [Φ * 1.5], X_rectangle[0:2], Y_rectangle[0:2], c="k")
        ax.plot(
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[1], X_rectangle[1], X_square[1]],
            [Y_square[1], Y_rectangle[1], Y_square[1]],
            c="k",
        )
        ax.plot(
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[2], X_rectangle[2], X_square[2]],
            [Y_square[2], Y_rectangle[2], Y_square[2]],
            c="k",
        )
        ax.plot(2 * [Φ * 1.5], X_rectangle[2:4], Y_rectangle[2:4], c="k")
        ax.plot(
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[3], X_rectangle[3], X_square[3]],
            [Y_square[3], Y_rectangle[3], Y_square[3]],
            c="k",
        )

        ax.plot(
            [X_square[0], X_rectangle[0], X_square[0]],
            [Y_square[0], Y_rectangle[0], Y_square[0]],
            [Φ, Φ * 1.5, Φ * 2],
            c="k",
        )
        ax.plot(X_rectangle[0:2], Y_rectangle[0:2], 2 * [Φ * 1.5], c="k")
        ax.plot(
            [X_square[1], X_rectangle[1], X_square[1]],
            [Y_square[1], Y_rectangle[1], Y_square[1]],
            [Φ, Φ * 1.5, Φ * 2],
            c="k",
        )
        ax.plot(
            [X_square[2], X_rectangle[2], X_square[2]],
            [Y_square[2], Y_rectangle[2], Y_square[2]],
            [Φ, Φ * 1.5, Φ * 2],
            c="k",
        )
        ax.plot(X_rectangle[2:4], Y_rectangle[2:4], 2 * [Φ * 1.5], c="k")
        ax.plot(
            [X_square[3], X_rectangle[3], X_square[3]],
            [Y_square[3], Y_rectangle[3], Y_square[3]],
            [Φ, Φ * 1.5, Φ * 2],
            c="k",
        )

        ax.plot(
            [Y_square[0], Y_rectangle[0], Y_square[0]],
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[0], X_rectangle[0], X_square[0]],
            c="k",
        )
        ax.plot(Y_rectangle[0:2], 2 * [Φ * 1.5], X_rectangle[0:2], c="k")
        ax.plot(
            [Y_square[1], Y_rectangle[1], Y_square[1]],
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[1], X_rectangle[1], X_square[1]],
            c="k",
        )
        ax.plot(
            [Y_square[2], Y_rectangle[2], Y_square[2]],
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[2], X_rectangle[2], X_square[2]],
            c="k",
        )
        ax.plot(Y_rectangle[2:4], 2 * [Φ * 1.5], X_rectangle[2:4], c="k")
        ax.plot(
            [Y_square[3], Y_rectangle[3], Y_square[3]],
            [Φ, Φ * 1.5, Φ * 2],
            [X_square[3], X_rectangle[3], X_square[3]],
            c="k",
        )

        ax.view_init(elev=35, azim=45)
        plt.tight_layout()
        ax.set_aspect('equal')
        plt.show()