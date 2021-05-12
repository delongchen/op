from PyQt5.QtWidgets import QPlainTextEdit, QLabel


class WinStdOut:
    def __init__(self, out: QPlainTextEdit):
        self.out = out

    def println(self, text):
        self.out.appendHtml(text)

    def println_wrapper(self, text):
        return lambda _: self.println(text)


class LabelOut:
    def __init__(self, label: QLabel):
        self._label = label

    def log(self, text, color):
        t = f'''
            <div style="color: {color}">
                <h1>{text}</h1>
            </div>
        '''
        self._label.setText(t)

    def info(self, text):
        self.log(text, 'white')

    def error(self, text):
        self.log(text, 'red')
