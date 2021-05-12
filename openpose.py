import time

import pyop.pyopenpose as openpose


class OpenPose:
    OP = None

    @classmethod
    def get_op_instance(cls):
        if cls.OP is None:
            cls.OP = cls()

        return cls.OP

    @classmethod
    def release(cls):
        if cls.OP is not None:
            cls.OP.stop()

    def __init__(self):
        self.config = {
            'model_folder': './models/',
            'net_resolution': '160x80',
            'hand': False
        }
        self.datum = openpose.Datum()
        self.wrapper = openpose.WrapperPython()
        self.wrapper.configure(self.config)
        self.fps = 0
        self.running = False

    def feed(self, img):
        self.datum.cvInputData = img
        start = time.time()
        self.wrapper.emplaceAndPop(openpose.VectorDatum([self.datum]))
        end = time.time()
        self.fps = int(1 / (end - start))
        return self.datum

    def start(self):
        if not self.running:
            self.wrapper.start()
            self.running = True

    def stop(self):
        if self.running:
            self.wrapper.stop()
            self.running = False

    def switch(self):
        if self.running:
            self.stop()
        else:
            self.start()
