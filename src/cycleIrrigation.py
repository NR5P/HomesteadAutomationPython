import datetime, json
import RPi.GPIO as GPIO
from device import Device
from log import Log

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
        self.blackoutStartTime = datetime.datetime.strptime(blackoutStartTime, "%Y-%m-%dT%H:%M:%S")
        self.blackoutStopTime = datetime.datetime.strptime(blackoutStopTime, "%Y-%m-%dT%H:%M:%S")
        self.triggerTime = None

        if self not in Device.deviceList:
            Device.deviceList.append(self)
    
    def run(self):
        if not self.isBlackedOut() and self.on == True:
            if self.triggerTime == None:
                self.triggerTime = datetime.datetime.now()

            if self.state == True:
                if datetime.datetime.now() > self.triggerTime + self.cycleOnTime:
                    if self.state == True:
                        self.state = False
                        self.triggerTime = datetime.datetime.now()
                        GPIO.output(self.pin, GPIO.LOW)
                        Log.cycleIrrigationLow()
            elif self.state == False:
                if datetime.datetime.now() > self.triggerTime + self.cycleOffTime:
                    if self.state == False:
                        self.state = True
                        self.triggerTime = datetime.datetime.now()
                        GPIO.output(self.pin, GPIO.HIGH)
                        Log.cycleIrrigationHigh()
        else:
            if self.state == True:
                self.state = False
                GPIO.output(self.pin, GPIO.LOW)
                Log.cycleIrrigationLow()

    def isBlackedOut(self):
        if self.blackoutStartTime < self.blackoutStopTime:
            if datetime.datetime.now().time() > self.blackoutStartTime.time() and datetime.datetime.now().time() < self.blackoutStopTime.time():
                return True
                print("not blacked out")
        else:
            if datetime.datetime.now().time() > self.blackoutStartTime.time() or datetime.datetime.now().time() < self.blackoutStopTime.time():
                return True
                print("blacked out")

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
