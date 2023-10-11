from Processor import Processor
from MessageType import MessageType

p = Processor(MessageType.messageType, MessageType.numMessageType)
p.processWords()
print(p.record)
