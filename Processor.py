from MessageType import MessageType


class Processor:
    def __init__(self, messageType=None, numMessageType=0):
        self.messageType = messageType
        self.numMessageType = numMessageType
        self.record = dict()
        for key in messageType:
            self.record[key] = list()

    def processWords(self):
        while True:
            s = input()
            if s == "end":
                break
            print(self.messageType[int(s)])
            self.record[int(s)].append(self.messageType[int(s)].processWords())


if __name__ == '__main__':
    processor = Processor(MessageType.messageType, MessageType.numMessageType)
    processor.processWords()
    print(processor.record)
