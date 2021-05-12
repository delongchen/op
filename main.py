import sys
from MyMainWindow import MyMainWindow
from PyQt5.QtWidgets import QApplication
from plugins import MyPlugin as MP
import qdarkstyle as qd

from plugins import op, hand

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qd.load_stylesheet_pyqt5())  # import style

    with MyMainWindow() as myWin:
        MP.MyPlugin.load_plugins(myWin, (
            op.Op,
            hand.HandPlugin
        ))
        myWin.show()
        sys.exit(app.exec_())
