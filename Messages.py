class WheelVelocity:

    def __init__(self, velocities):
        self.data = velocities

    def calculateAverageVelocity(self):
        return (self.data[0] + self.data[1]) / 2

    @staticmethod
    def processWords():
        a = int(input())
        b = int(input())
        return WheelVelocity((a, b))


class VisionTarget:

    def __init__(self, targets):
        self.data = targets

    @staticmethod
    def processWords():
        numTarget = int(input())
        targets = list()
        for i in range(numTarget):
            a = int(input())
            b = int(input())
            targets.append((a, b))
        return VisionTarget(targets)


if __name__ == '__main__':
    vt = VisionTarget.processWords()
    print(vt.data)
    wv = WheelVelocity.processWords()
    print(wv.calculateAverageVelocity())
