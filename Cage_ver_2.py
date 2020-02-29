class Cage:
    """This class describe one cell"""
    temperature = None
    material = None
    mass = None
    upd_q = None  # q that cell get from other cells
    saved_q = None  # q that goes to change material
    fraction = 0  # parameter that is used for change effective_mass
    checker = True  # exit criterion
    # const
    dx = 10 ** (-3)
    S = 10 ** (-6)
    t_0 = 10 ** (-3)
    V = S * dx

    def interaction(self, *cell_list):
        for i in range(len(cell_list)):

            self.upd_q += 0.5 * (self.material.conductivity + cell_list[i].material.conductivity) * (
                    self.temperature - cell_list[i].temperature) / Cage.dx * Cage.t_0 * Cage.S  # q that taken from cell

            if self.saved_q >= self.material.fusion * self.mass * (
                    1 - self.fraction):  # check if saved_q >= lambda * effective_mass
                self.checker = False  # exit if False
                self.fraction = 0  # change to initial
                self.material = cell_list[i].material  # change material
                self.saved_q = 0  # change to initial
                self.V = self.mass / self.material.density  # Mass conservation law
            if round(self.temperature,
                     1) == self.material.trans_temperature and self.checker:  # check criterion and temp to enter
                self.saved_q += abs(self.upd_q) * 10
                self.fraction = self.saved_q / (self.material.fusion * self.mass * (1 - self.fraction))
                self.upd_q = 0

    def change_temp(self):
        self.temperature -= self.upd_q / (self.material.capacity * self.mass)
        self.upd_q = 0

    def __init__(self, temperature=None, material=None):
        self.temperature = temperature
        self.material = material
        self.mass = material.density * Cage.S * Cage.dx
        self.upd_q = 0
        self.saved_q = 0
