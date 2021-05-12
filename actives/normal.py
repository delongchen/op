from body import Body
from pose import PoseCoach
from .active import Active


class NormalActive(Active):
    NAME = "normal"

    def __init__(self, win, button):
        super().__init__(win, button)
        self.c1 = PoseCoach((30, 180))
        self.c2 = PoseCoach((30, 180), False)

    def update(self, body: Body):
        plu = self.win
        self.c1.update(body, plu)
        self.c2.update(body, plu)


class OtherActive(Active):
    NAME = "other"

    def __init__(self, win, button):
        super(OtherActive, self).__init__(win, button)
        self.c = PoseCoach((40, 170))

    def update(self, body: Body):
        self.c.update(body, self.win)
