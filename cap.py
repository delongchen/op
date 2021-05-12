import cv2
import time

cap_status = {
    'closed': False
}


class CapEvent:
    ACTION = 'cap_action'
    INFO = 'cap_info'

    def __init__(self, t, text):
        self.t = t
        self.text = text
        self.start_time = None
        self.end_time = None

    def finish(self, text):
        self.end_time = time.time()
        self.text = text
        return self

    def get_spend_time(self):
        return (int(self.end_time * 1000) - int(self.start_time * 1000)) / 1000

    @classmethod
    def action(cls, text):
        result = cls(cls.ACTION, text)
        result.start_time = time.time()
        return result

    @classmethod
    def info(cls, text):
        return cls(cls.INFO, text)


def set_cap(flag: bool):
    cap_status['closed'] = flag


def close_cap():
    set_cap(True)


def open_cap():
    set_cap(False)


class CapCache:
    cap = None

    @classmethod
    def release(cls):
        if cls.cap is not None:
            cls.cap.release()


def get_cap():
    if CapCache.cap is not None:
        return CapCache.cap
    CapCache.cap = cv2.VideoCapture(0)
    return CapCache.cap


def cap_loop(cap):
    while not cap_status['closed']:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        ret, img = cap.read()
        yield img

    cap.release()
