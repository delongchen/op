from numpy import ndarray
from util import get_angel_of


class BodyPointMap:
    Neck = 1
    RShoulder = 2
    RElbow = 3
    RWrist = 4
    LShoulder = 5
    LElbow = 6
    LWrist = 7


class Hand:
    def __init__(self, shoulder: ndarray, elbow: ndarray, wrist: ndarray):
        self.shoulder = shoulder
        self.elbow = elbow
        self.wrist = wrist

    def get_angel(self):
        return get_angel_of(self.shoulder, self.elbow, self.wrist)


class Body:
    def __init__(self, key_points: ndarray):
        self.neck = key_points[BodyPointMap.Neck]
        self.r_shoulder = key_points[BodyPointMap.RShoulder]
        self.r_elbow = key_points[BodyPointMap.RElbow]
        self.r_wrist = key_points[BodyPointMap.RWrist]
        self.l_shoulder = key_points[BodyPointMap.LShoulder]
        self.l_elbow = key_points[BodyPointMap.LElbow]
        self.l_wrist = key_points[BodyPointMap.LWrist]

        self.l_hand = Hand(
            self.l_shoulder,
            self.l_elbow,
            self.l_wrist
        )

        self.r_hand = Hand(
            self.r_shoulder,
            self.r_elbow,
            self.r_wrist
        )
