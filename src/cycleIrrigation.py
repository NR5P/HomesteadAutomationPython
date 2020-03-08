import datetime, json

from device import Device

class CycleIrrigation(Device):
    """
    this device type is for cycle type irrigation for short bursts of irrigation. This is usually used for propagating plants
    Attributes:
        cycleOnTime = the length of time irrigation on
        cycleOffTime = the length of time irrigation is off
        blackoutStartTime = time that irrigation stops (usually in evening)
        blackoutStopTime = time irrigation starts again (usually in morning)
    """
    def __init__(self, id, name, notes, pin, cycleOnTime, cycleOffTime, blackoutStartTime, blackoutStopTime):
        super().__init__(id, name, notes, pin)
        self.cycleOnTime = Device.convertISOToTimeDelta(cycleOnTime)
        self.cycleOffTime = Device.convertISOToTimeDelta(cycleOffTime)
        self.blackoutStartTime = datetime.datetime.strptime(blackoutStartTime, "%Y-%m-%dT%H:%M:%S%z")
        self.blackoutStopTime = datetime.datetime.strptime(blackoutStopTime, "%Y-%m-%dT%H:%M:%S%z")

        if self not in Device.deviceList:
            Device.deviceList.append(self)
    
    def run(self):
        pass

