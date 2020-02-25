class Cage:
    """This class describe one cell"""
    temperature = None
    material = None
    mass = None
    upd_q = None
    saved_q = None
    dx = 10 ** (-3)
    S = 10 ** (-6)
    t_0 = 10 ** (-2)

    def interaction(self, *cell_list):
        for i in range(len(cell_list)):
            self.upd_q += 0.5 * (self.material.conductivity + cell_list[i].material.conductivity) * (
                    self.temperature - cell_list[i].temperature) / Cage.dx * Cage.t_0 * Cage.S
            if round(self.temperature, 0) == self.material.trans_temperature and self.material != cell_list[i].material:
                self.saved_q += abs(self.upd_q) * 10
                self.upd_q = 0
            if self.saved_q >= self.material.fusion * self.mass:
                self.material = cell_list[i].material
                self.saved_q = 0

    def change_temp(self):
        self.temperature -= self.upd_q / (self.material.capacity * self.mass)
        self.upd_q = 0

    def __init__(self, temperature=None, material=None):
        self.temperature = temperature
        self.material = material
        self.mass = material.density * Cage.S * Cage.dx
        self.upd_q = 0
        self.saved_q = 0
