from body import Body


class Active:
    NAME: str

    def __init__(self, win, button):
        self.win = win
        self.button = button

    def update(self, body: Body):
        pass
