from MyMainWindow import MyMainWindow
from MyLogger import Logger


class MyPlugin:
    _plus = dict()
    ui: MyMainWindow
    logger: Logger

    @classmethod
    def load_plugins(cls, win: MyMainWindow, plus):
        cls.ui = win
        cls.logger = cls.ui.logger
        cls.label_out = cls.ui.label_out

        for plu in plus:
            p = plu()
            cls._plus[plu.__name__] = p
            p.run()

    @classmethod
    def get_plu(cls, name):
        return cls._plus[name]

    def run(self):
        pass
