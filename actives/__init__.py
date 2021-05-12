from .normal import NormalActive, OtherActive
from .active import Active
from PyQt5.QtWidgets import QMainWindow, QPushButton

ACS = (
    NormalActive,
    OtherActive
)

AC_CACHE = dict()


class Actives:
    AC: Active
    ACN = -1
    win: QMainWindow

    @classmethod
    def load(cls, win: QMainWindow):
        cls.win = win
        container = win.ac_list
        layout = win.verticalLayoutWidget_2

        for n in range(len(ACS)):
            ac = ACS[n]
            name = ac.NAME

            button = QPushButton(layout)
            button.setObjectName(f"button_active_{name}")
            button.setText(name)
            button.clicked.connect(cls.set_active(n))
            container.addWidget(button)

            AC_CACHE[name] = ac(cls.win, button)

        cls.set_active(0)()

    @classmethod
    def set_active(cls, n):
        def ret():
            if cls.ACN == n:
                return

            now, before = ACS[n].NAME, ACS[cls.ACN].NAME
            print(now, before)
            now_ins, before_ins = AC_CACHE[now], AC_CACHE[before]

            before_ins.button.setText(before)
            now_ins.button.setText(now + ' <')

            cls.ACN = n
            cls.AC = now_ins

        return ret
