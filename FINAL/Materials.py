class Material:
    """This class describe cell Material"""
    name = None
    capacity = None
    conductivity = None
    fusion = None
    density = None
    trans_temperature = None

    def __init__(self, name, capacity, conductivity, fusion, density, trans_temperature):
        self.name = name
        self.capacity = capacity  # удельная теплоёмкость
        self.conductivity = conductivity  # удельная проводимость
        self.fusion = fusion  # удельная теплота плавления/кристализации
        self.density = density  # плотность
        self.trans_temperature = trans_temperature


water = Material('Water', 4200, 0.556, -3.4 * 10 ** 5, 1000, 0)
ice = Material('Ice', 2100, 2.330, 3.4 * 10 ** 5, 900, 0)
air = Material('Air', float('inf'), 0.02, 100, 1.5, 100)
