import Materials


class Cage:
    """This class describe one cell"""
    temperature = None
    material = None
    mass = None
    upd_q = None  # q that cell get from other cells
    fraction = 0  # parameter that is used for change effective_mass
    checker_transformation = True  # exit criteria
    # const
    dx = 10 ** (-3)
    S = dx ** 2
    t_0 = 10 ** (-3)
    V = S * dx

    def interaction(self, *cell_list):
        for i in range(len(cell_list)):
            self.upd_q += 0.5 * (self.material.conductivity + cell_list[i].material.conductivity) * (
                    -self.temperature + cell_list[i].temperature) / Cage.dx * Cage.t_0 * Cage.S * (
                                      1 - self.fraction) ** (1 / 3)  # q that taken from cell

        if (self.material.name is 'Water') and self.fraction >= 0.9:  # check if saved_q >= lambda * effective_mass
            self.checker_transformation = False  # exit if False
            self.fraction = 0  # change to initial
            self.material = Materials.ice  # change material
            self.V = self.mass / self.material.density

        if (self.material.name is 'Ice') and self.fraction >= 0.9:  # check if saved_q >= lambda * effective_mass
            self.checker_transformation = False  # exit if False
            self.fraction = 0  # change to initial
            self.material = Materials.water  # change material
            self.V = self.mass / self.material.density  # Mass conservation law
        if round(self.temperature, 1) == self.material.trans_temperature and self.checker_transformation:
            self.fraction += self.upd_q / (self.material.fusion * self.mass) * 100
            self.upd_q = 0
        # if round(self.temperature, 1) > self.material.trans_temperature:
        #     self.checker_transformation = True  #  IF WE WANT TO DO 2 PHASE TRANSFORMATION
        #  DONT KNOW WORK OR NOT

    def change_temp(self):
        self.temperature += self.upd_q / (self.material.capacity * self.mass)
        self.upd_q = 0

    def __init__(self, temperature=None, material=None):
        self.temperature = temperature
        self.material = material
        self.mass = material.density * Cage.S * Cage.dx
        self.upd_q = 0
