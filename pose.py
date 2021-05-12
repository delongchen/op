from body import Body


class PoseCoach:
    def __init__(self, target: tuple, left: bool = True):
        self.left = left
        self.n = -1

        self.count = 0
        self.step = 10
        self.start = target[0]
        self.end = target[1]
        self.heap = list()
        self.increase = True

        self.targets = list(range(self.start, self.end, self.step))
        self.targets.reverse()

    def check(self):
        if len(self.targets) == 0:
            self.targets, self.heap = self.heap, self.targets
            self.increase = not self.increase
            self.count += 1

    def pop_and_push(self):
        self.heap.append(self.targets.pop())

    def get_hand(self, body: Body):
        if self.left:
            return body.l_hand
        else:
            return body.r_hand

    def show_info(self, plu):
        num = 0 if self.left else 1
        a, n, out = (plu.a[num], plu.n[num], plu.label_out[num])
        if self.n == -1:
            out.error("未检测到完整手部")
        else:
            a.display(self.n)
            n.display(self.count)
            out.info("伸手" if self.increase else "收回手")

    def update(self, body: Body, plu):
        self.n = self.get_hand(body).get_angel()
        self.check()
        peek = self.targets[-1]
        if self.increase:
            if self.n > peek:
                self.pop_and_push()
        else:
            if self.n < peek:
                self.pop_and_push()

        self.show_info(plu)
