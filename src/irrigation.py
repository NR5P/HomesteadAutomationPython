import datetime, json

from device import Device

class Irrigation(Device):
    """
    this device type is for normal garden type irrigation
    Attributes:
        daysOfWeekToIrrigate = list of numbers for days of week
        irrigationTimes = dict of key vals keys are datetime and values are timedeltas, 
        keys for times to irrigate and time delts for the irrigation
    """
    def __init__(self, id, name, notes, pin, daysOfWeekToIrrigate, irrigationTimes):
        super().__init__(id, name, notes, pin, daysOfWeekToIrrigate, irrigationTimes)
        self.daysOfWeekToIrrigate = daysOfWeekToIrrigate
        self.irrigationTimes = irrigationTimes

        if self not in Device.deviceList:
            Device.deviceList.append(self)

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
    
    def isDayToIrrigate(self, day):
        if day in daysOfWeekToIrrigate:
            return True