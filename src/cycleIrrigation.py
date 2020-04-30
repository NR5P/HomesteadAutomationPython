import datetime, json
#import RPi.GPIO as GPIO TODO: add back when on pi
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
        self.triggerTime = None

        if self not in Device.deviceList:
            Device.deviceList.append(self)
    
    def run(self):
        if not self.isBlackedOut():
            if self.triggerTime == None:
                self.triggerTime = datetime.now()

            if self.state == True:
                if datetime.now() > self.triggerTime + self.cycleOnTime:
                    self.state = False
                    self.triggerTime = datetime.now()
                    #GPIO.output(self.pin, GPIO.LOW) TODO: add back when on pi
            elif self.state == False:
                if datetime.now() > self.triggerTime + self.cycleOffTime:
                    self.state = True
                    self.triggerTime = datetime.now()
                    #GPIO.output(self.pin, GPIO.HIGH) TODO: add back when on pi
        else:
            self.state = False
            #GPIO.output(self.pin, GPIO.LOW) TODO: add back when on pi

    def isBlackedOut(self):
        if self.blackoutStartTime < self.blackoutStopTime:
            if datetime.now().time() > self.blackoutStartTime and datetime.now().time() < self.blackoutStopTime:
                return True
        else:
            if datetime.now().time() > self.blackoutStartTime or datetime.now().time() < self.blackoutStopTime:
                return True

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
