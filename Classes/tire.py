class Tire:
    """
    Tire represents a tire that would be used with an automobile.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type: tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction