from out import WinStdOut
import time


time_fmt = "[%Y-%m-%d %H:%M:%S]"


class Logger:
    def __init__(self, out: WinStdOut):
        self._stdout = out

    def log(self, text, color):
        now = time.strftime(time_fmt, time.localtime())
        t = f'''
            <div style="color: {color}">
                <h3>{now}</h3>
                <h3>{text}</h3>
            </div>
        '''
        self._stdout.println(t)

    def info(self, text):
        self.log(text, "white")

    def warning(self, text):
        self.log(text, "#DAA520")

    def error(self, text):
        self.log(text, "red")
