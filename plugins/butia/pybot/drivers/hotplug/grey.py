
RD_VERSION = 0x00
GET_VALUE = 0x01
ERROR = -1

def getVersion(dev):
    dev.send([RD_VERSION])
    raw = dev.read(3)
    return raw[1] + raw[2] * 256

def getValue(dev):
    dev.send([GET_VALUE])
    raw = dev.read(3)
    if not(raw[1] == 255):
        return (raw[1] + raw[2] * 256)
    else:
        return ERROR


