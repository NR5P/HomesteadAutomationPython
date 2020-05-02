import datetime, json
import RPi.GPIO as GPIO
from device import Device
from log import Log

class Irrigation(Device):
    """
    this device type is for normal garden type irrigation
    Attributes:
        daysOfWeekToIrrigate = list of numbers for days of week
        irrigationTimes = dict of key vals keys are datetime and values are timedeltas, 
        keys for times to irrigate and time deltas for the irrigation length
    """
    def __init__(self, id, name, notes, pin, daysOfWeekToIrrigate, irrigationTimes):
        super().__init__(id, name, notes, pin)
        self.daysOfWeekToIrrigate = daysOfWeekToIrrigate
        self.irrigationTimes = Device.convertToDatetimeTimedeltaDict(irrigationTimes)

        if self not in Device.deviceList:
            Device.deviceList.append(self)

    def run(self):
        if self.isDayToIrrigate() and self.on == True:
            for irrigationTime, irrigationDuration in self.irrigationTimes.items():
                timeToStop = irrigationTime + irrigationDuration
                if timeToStop > irrigationTime:
                    if datetime.datetime.now() > irrigationTime and datetime.datetime.now() < timeToStop:
                        if self.state == False:
                            self.gpioOn()
                            Log.irrigationHigh()
                    else:
                        if self.state == True:
                            self.gpioOff()
                            Log.irrigationLow()
                else:
                    if datetime.datetime.now() > irrigationTime or datetime.datetime.now() < timeToStop:
                        if self.state == False:
                            self.gpioOn()
                            Log.irrigationHigh()
                    else:
                        if self.state == True:
                            self.gpioOff()
                            Log.irrigationLow()
        else:
            if self.state == True:
                self.gpioOff()
                Log.irrigationLow()



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
    
    def isDayToIrrigate(self):
        if datetime.datetime.today().weekday() in self.daysOfWeekToIrrigate:
            return True
        else:
            return False