from plugins.MyPlugin import MyPlugin
from body import Body
from pyop import pyopenpose as op
from actives import Actives


class HandPlugin(MyPlugin):
    def __init__(self):
        pass

    def make_body_from_points(self, datum: op.Datum):
        points = datum.poseKeypoints
        if points is not None:
            if len(points) != 1:
                pass
                # self.logger.warning(f"too many people: {len(points)}")
            self.update_label(Body(points[0]))

    @staticmethod
    def update_label(body: Body):
        Actives.AC.update(body)

    def run(self):
        self.ui.cap_thread.register(self.make_body_from_points)
