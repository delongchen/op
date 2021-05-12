from plugins.MyPlugin import MyPlugin
from PyQt5.QtGui import QPixmap, QImage
import cv2
from cap import CapEvent
from openpose import OpenPose


class Op(MyPlugin):
    def open(self):
        self.ui.cap_thread.start()

    def handle_sig(self, ev: CapEvent):
        if ev.t == CapEvent.ACTION and ev.end_time is not None:
            self.logger.info(f"spend {ev.get_spend_time()} s")
        self.logger.info(ev.text)

    def show_img(self, img):
        show = cv2.flip(img, 1)
        show = cv2.resize(show, (1280, 960))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

        to_show = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.ui.label.setPixmap(QPixmap.fromImage(to_show))

    def run(self):
        self.ui.button_open.clicked.connect(self.open)
        self.ui.cap_thread.img.connect(self.show_img)
        self.ui.cap_thread.sigOut.connect(self.handle_sig)
        self.ui.button_op.clicked.connect(lambda _: OpenPose.get_op_instance().switch())

    def shutdown(self):
        pass
