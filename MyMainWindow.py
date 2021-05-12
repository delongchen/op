from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from CapThread import CapThread
from out import WinStdOut, LabelOut
from MyLogger import Logger
from cap import CapCache
from openpose import OpenPose
from actives import Actives


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.label_tip.setText('''
        <div style="text-align: center">
            <h1 style="color: red">hello</h1>
            <h1 style="color: white">world</h1>
        </div>
        ''')
        Actives.load(self)

    def __enter__(self):
        self.stdout = WinStdOut(self.plainTextEdit)
        self.setup_cap_thread(self)
        self.setup_logger(self)

        self.button_q.clicked.connect(lambda _: self.close())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        CapCache.release()
        OpenPose.release()

    @staticmethod
    def setup_cap_thread(win):
        win.cap_thread = CapThread()

        def on_cap_thread_datum(datum):
            for ob in win.cap_thread.obs:
                ob(datum)

        win.cap_thread.datum.connect(on_cap_thread_datum)

    @staticmethod
    def setup_logger(win):
        win.logger = Logger(win.stdout)
        win.label_out = (LabelOut(win.label_left), LabelOut(win.label_right))
        win.a = (win.lcd_left_angel, win.lcd_right_angel)
        win.n = (win.lcd_left_count, win.lcd_right_count)
