class Message:
    def __init__(self, data):
        self.data = data


class WheelVelocity(Message):

    def __init__(self, data):
        super().__init__(data)
        self.left = self.data[0]
        self.right = self.data[1]

    def calculateAverageVelocity(self):
        return (self.data[0] + self.data[1]) / 2

    @staticmethod
    def processWords():
        a = int(input())
        b = int(input())
        return WheelVelocity((a, b))


class VisionTarget(Message):

    def __init__(self, data):
        super().__init__(data)
        self.numTargets = self.data[0]
        self.targets = list()
        for i in range(self.numTargets):
            self.targets.append(self.data[i + 1])

    @staticmethod
    def processWords():
        numTarget = int(input())
        targets = list()
        targets.append(numTarget)
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
