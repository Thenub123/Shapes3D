class Shapes3D:
    def __init__(self, type, colour, rounding):
        self.type = type
        self.colour = colour
        self.rounding = rounding

    def get_type(self) :
        return self.type
    
    def get_colour(self):
        return self.colour
    
    def set_rounding(self, new_rounding):
        self.rounding = new_rounding
    
    def set_colour(self, new_colour):
        self.colour = new_colour