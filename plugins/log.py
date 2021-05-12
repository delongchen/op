from plugins.MyPlugin import MyPlugin


class Logger(MyPlugin):
    def __init__(self):
        self.out = self.ui.plainTextEdit

    def log(self, text):
        self.out.appendPlainText(text)

    def log_wrapper(self, text):
        return lambda _: self.log(text)

    def run(self):
        self.ui.button_op.clicked.connect(self.log_wrapper("test"))
