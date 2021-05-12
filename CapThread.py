from PyQt5.QtCore import QThread, pyqtSignal
from cap import cap_loop, get_cap, CapEvent
from openpose import OpenPose
import pyop.pyopenpose as op
import numpy as np


class CapThread(QThread):
    sigOut = pyqtSignal(CapEvent)
    datum = pyqtSignal(op.Datum)
    img = pyqtSignal(np.ndarray)

    def __init__(self):
        super(CapThread, self).__init__()
        self.obs = list()

    def emit(self, sig):
        self.sigOut.emit(sig)

    def register(self, ob):
        self.obs.append(ob)

    def run(self) -> None:
        self.emit(CapEvent.info('openpose starting'))
        OP = OpenPose.get_op_instance()
        OP.start()
        self.emit(CapEvent.info('openpose on'))

        open_cap_action = CapEvent.action("camera starting")
        self.emit(open_cap_action)
        cap = get_cap()
        self.emit(open_cap_action.finish("camera on"))

        for img in cap_loop(cap):
            if OP.running:
                datum = OP.feed(img)
                self.datum.emit(datum)
                self.img.emit(datum.cvOutputData)
            else:
                self.img.emit(img)
