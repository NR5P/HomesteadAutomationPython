import datetime, json

from device import Device

class Irrigation(Device):
    """
    this device type is for normal garden type irrigation
    Attributes:
        daysOfWeekToIrrigate = list of numbers for days of week
        irrigationTimes = dict of key vals keys are datetime and values are timedeltas, 
        keys for times to irrigate and time deltas for the irrigation
    """
    def __init__(self, id, name, notes, pin, daysOfWeekToIrrigate, irrigationTimes):
        super().__init__(id, name, notes, pin)
        self.daysOfWeekToIrrigate = daysOfWeekToIrrigate
        self.irrigationTimes = Device.convertToDatetimeTimedeltaDict(irrigationTimes)

        if self not in Device.deviceList:
            Device.deviceList.append(self)

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
    
    def to_json(self):
        tempDict = {}
        for k, v in self.__dict__.items():
            if isinstance(v,bool):
                tempDict[k] = str(v).lower()
            elif isinstance(v,dict):
                tempDict[k] = Irrigation.jsonConverter(v)
            elif isinstance(v,datetime.datetime):
                tempDict[k] = v.isoformat()
            else:
                tempDict[k] = v
        return json.dumps(tempDict)
    
    @staticmethod
    def jsonConverter(j):
        tempDict = {}
        for k, v in j.items():
            tempDict[k.isoformat()] = v.total_seconds()
        return tempDict
    
    def isDayToIrrigate(self, day):
        if day in daysOfWeekToIrrigate:
            return True