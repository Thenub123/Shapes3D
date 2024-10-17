from Shapes3D import Shapes3D
from cone import Cone
from dodecahedron import Dodecahedron
import os

clear = lambda: os.system('cls')

cone = Cone(1, 1, 6)
dodecahedron = Dodecahedron(1, 1)

class Menu():
    def __init__(self):
        self.menu()

    def menu(self):
        print("""         _______  ________        ________  __    __       __         _______    _______   ________  
        /" __   )|"      "\      /"       )/" |  | "\     /""\       |   __ "\  /"     "| /"       ) 
        (__/ _) ./(.  ___  :)    (:   \___/(:  (__)  :)   /    \      (. |__) :)(: ______)(:   \___/  
            /  // |: \   ) ||     \___  \   \/      \/   /' /\  \     |:  ____/  \/    |   \___  \    
        __ \_  \ (| (___\ ||      __/   \  //  __   \  //  __'  \    (|  /      // ___)_   __/   \   
        (: \__) :\|:       :)     /" \   :)(:  (  )  :)/   /  \   \  /|__/ \    (:      "| /" \   :)  
        \_______)(________/     (_______/  \__|  |__/(___/    \___)(_______)    \_______)(_______/   
                                                                                                    
              
        1. Cone Properties
        2. Dohdecahedron Properties
        3. Rounding Settings
              
        
        (The 3D rendering module I used was not compatible with any other GUI interface I tried using... so I'm unfortunately stuck with this)
              
        """)

        try:
            selection = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.menu()

        if selection == 1:
            clear()
            self.cone_menu()
        elif selection == 2:
            clear()
            self.d_menu()
        elif selection == 3:
            clear()
            self.rounding_properties()
        else:
            clear()
            print("----[Not a valid selection]----")
            self.menu()
            
    def rounding_properties(self):
        try:
            rounding = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.rounding_properties()

        if rounding < 0:
            clear()
            print("----[Cannot be less than 0]----")
            self.rounding_properties()

        cone.rounding = rounding
        dodecahedron.rounding = rounding
        self.menu()


    def cone_menu(self):
        print(f""" ---------[Cone Properties]---------
        
        The type of this shape is a {cone.get_type()} and the colour is {cone.get_colour()}
        
        1. Set Dimensions (Current dimensions are: Radius: {cone.get_dimensions()[0]}, Height: {cone.get_dimensions()[1]}, Number of Points: {cone.get_dimensions()[2]})
        2. Set Colour
        3. Get Verticies
        4. Get Surface Area/ Volume/ Circumference
        5. Render in 3D space
        6. Back

        """)

        try:
            selection = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.cone_menu()

        if selection == 1:
            clear()
            self.cone_set_dimensions()
        elif selection == 2:
            clear()
            self.set_color_cone()
        elif selection == 3:
            clear()
            self.cone_get_verticies()
        elif selection == 4:
            clear()
            self.cone_get_svc()
        elif selection == 5:
            cone.display()
            clear()
            self.cone_menu()
        elif selection == 6:
            clear()
            self.menu()
        else:
            clear()
            print("----[Not a valid selection]----")
            self.cone_menu()
    
    def cone_set_dimensions(self):
        try:
            radius = int(input("Radius: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.cone_set_dimensions()

        try:
            height = int(input("Height: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.cone_set_dimensions()

        try:
            num_points = int(input("Number of points: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.cone_set_dimensions()

        print(f"{radius}, {height}, {num_points}")

        if radius <= 0 or height <= 0 or num_points <= 0:
            clear()
            print("----[You cannot have negative numbers]----")
            self.cone_set_dimensions()
        
        cone.set_dimensions(radius, height, num_points)
        clear()
        self.cone_menu()
    
    def set_color_cone(self):
        print(f""" ---------[Cone Color]---------
        
        The current colour is {cone.get_colour()}
        
        You can choose from: black, red, orange, yellow, green, blue, purple

        """)

        color = input("Color: ")

        valid_colors = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']

        if color.lower() not in valid_colors:
            clear()
            print("""----[Not a valid color]----
                  """)
            self.set_color_cone()
        
        cone.set_colour(color)
        clear()
        self.cone_menu()

    def cone_get_verticies(self):
        print(f""" ---------[All current verticies]---------
        
        There are {cone.get_dimensions()[2]} points
        
        The verticies are {cone.get_verticies()}

        1. Back

        """)

        try:
            selection = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.cone_get_verticies()

        if selection == 1:
            clear()
            self.cone_menu()
        else:
            clear()
            print("----[Not a valid selection]----")
            self.cone_get_verticies()

    def cone_get_svc(self):
        print(f""" ---------[Surface area/ Volume/ Circumference]---------
        
        The surface area is {cone.surface_area()}
        
        The volume is {cone.volume()}

        The circumference of the circle is {cone.get_circumference()}

        1. Back

        """)

        try:
            selection = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.cone_get_svc()

        if selection == 1:
            clear()
            self.cone_menu()
        else:
            clear()
            print("----[Not a valid selection]----")
            self.cone_get_svc()

    def d_menu(self):
        print(f""" ---------[Dodecahedron Properties]---------
        
        The type of this shape is a {dodecahedron.get_type()} and the colour is {dodecahedron.get_colour()}
        
        1. Set Dimensions (Current dimensions are: a: {dodecahedron.get_dimensions()[0]}, b: {dodecahedron.get_dimensions()[1]})
        2. Set Colour
        3. Get Verticies
        4. Get Surface Area/ Volume
        5. Render in 3D space
        6. Back

        """)

        try:
            selection = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.d_menu()

        if selection == 1:
            clear()
            self.d_set_dimensions()
        elif selection == 2:
            clear()
            self.set_color_d()
        elif selection == 3:
            clear()
            self.d_get_verticies()
        elif selection == 4:
            clear()
            self.d_get_svc()
        elif selection == 5:
            dodecahedron.display()
            clear()
            self.d_menu()
        elif selection == 6:
            clear()
            self.menu()
        else:
            clear()
            print("----[Not a valid selection]----")
            self.d_menu()

    def d_set_dimensions(self):
        try:
            a = int(input("a: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.d_set_dimensions()

        try:
            b = int(input("b: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.d_set_dimensions()
        
        dodecahedron.set_dimensions(a, b)
        clear()
        self.d_menu()

    def set_color_d(self):
        print(f""" ---------[Dodecahedron Color]---------
        
        The current colour is {dodecahedron.get_colour()}
        
        You can choose from: black, red, orange, yellow, green, blue, purple

        """)

        color = input("Color: ")

        valid_colors = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']

        if color.lower() not in valid_colors:
            clear()
            print("""----[Not a valid color]----
                  """)
            self.set_color_d()
        
        dodecahedron.set_colour(color)
        clear()
        self.d_menu()

    def d_get_verticies(self):
        print(f""" ---------[All current verticies]---------
        
        There are 20 points
        
        The verticies are {dodecahedron.get_verticies()}

        1. Back

        """)

        try:
            selection = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.d_get_verticies()

        if selection == 1:
            clear()
            self.d_menu()
        else:
            clear()
            print("----[Not a valid selection]----")
            self.d_get_verticies()

    def d_get_svc(self):
        print(f""" ---------[Surface area/ Volume]---------
        
        The surface area is {dodecahedron.surface_area()}
        
        The volume is {dodecahedron.volume()}

        1. Back

        """)

        try:
            selection = int(input("Selection: "))
        except:
            clear()
            print("----[Not a valid selection]----")
            self.d_get_svc()

        if selection == 1:
            clear()
            self.d_menu()
        else:
            clear()
            print("----[Not a valid selection]----")
            self.d_get_svc()

Menu()