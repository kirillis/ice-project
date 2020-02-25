class Mew:
    """This class describe one cell"""
    temperature = None
    material = None
    mass = None
    upd_q = None
    saved_q = None
    dx = 10 ** (-3)
    S = 10 ** (-6)
    t_0 = 10 ** (-2)

    def interaction(self, cell):
        self.upd_q = min(self.material.conductivity, cell.material.conductivity) * (
                self.temperature - cell.temperature) / Mew.dx * Mew.t_0 * Mew.S

        if abs(self.saved_q) < self.material.fusion * self.mass and round(self.temperature,
                                                                          2) == self.material.trans_temperature \
                and self.material != cell.material:
            self.saved_q += abs(self.upd_q) * 10
            self.upd_q = 0
        if self.saved_q >= self.material.fusion * self.mass:
            self.material = cell.material
            self.saved_q = 0

    def change_temp(self):
        self.temperature -= self.upd_q / (self.material.capacity * self.mass)

    def __add__(self, other):
        self.interaction(other)
        other.interaction(self)
        self.change_temp()
        other.change_temp()

    def total_change(self):
        self.change_temp()

    def __init__(self, temperature=None, material=None):
        self.temperature = temperature
        self.material = material
        self.mass = material.density * Mew.S * Mew.dx
        self.upd_q = 0
        self.saved_q = 0

    def __str__(self):
        return self.material.name


def line_interaction(*cells_list):
    n = len(cells_list[0])
    for i in range(1, n):
        _ = cells_list[0][i - 1] + cells_list[0][i]
