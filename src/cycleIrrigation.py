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
        self.cycleOnTime = datetime.timedelta(seconds=cycleOnTime)
        self.cycleOffTime = datetime.timedelta(seconds=cycleOffTime)
        self.blackoutStartTime = datetime.datetime.strptime(blackoutStartTime, "%Y-%m-%dT%H:%M:%S%z")
        self.blackoutStopTime = datetime.datetime.strptime(blackoutStopTime, "%Y-%m-%dT%H:%M:%S%z")

        if self not in Device.deviceList:
            Device.deviceList.append(self)
    
    def run(self):
        pass

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
    
    def to_json(self):
        return json.dumps(self.__dict__,default=self.to_json_helper)

    def to_json_helper(self, value):
        if isinstance(value,datetime.datetime):
            return value.isoformat()
        elif isinstance(value,datetime.timedelta):
            return int(value.total_seconds())
