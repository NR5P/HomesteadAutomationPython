import datetime

class Device:
    """
    Device the parent class that all other devices inherit from
        Atributes:
            id = unique database id of the device
            name = unique user defined name of a device
            notes = user defined notes of the device 
            pin = gpio pin number used for the device
            state = current state (on or off)
            deviceList = list of all devices that are of Device type
    """
    deviceList = []
    outputPinDict = {
        5:False,
        6:False,
        12:False,
        13:False,
        16:False,
        18:False,
        20:False,
        21:False,
        22:False,
        23:False,
        24:False,
        25:False,
        26:False,
        27:False,
    }
    allOn = True

    def __init__(self, id, name, notes, pin):
        self.id = id
        self.name = name
        self.notes = notes
        self.pin = pin
        self.state = False
        self.on = True
    
    def setPin(self, newPin):
        for i in Device.deviceList:
            if i.pin == newPin:
                return False
        self.pin = newPin
        return True
    
    def setName(self, newName):
        for i in Device.deviceList:
            if i.name == newName:
                return False
        self.name = newName
        return True

    def turnOff(self):
        self.on = False

    def gpioOn(self):
        self.state = True
        GPIO.output(self.pin, GPIO.HIGH)

    def gpioOff(self):
        self.state = False
        GPIO.output(self.pin, GPIO.LOW)
    
    @staticmethod
    def convertToDatetimeTimedeltaDict(timesToConvert):
        """
            takes a dict of times to irrigate (key) and length of time to irrigate (value). 
            converts the time to irrigate from 8601 and converts it to a datetime and takes the
            seconds (value) and converts to a time delta. then returns the dict of k, v (datetime, timedelta)
        """
        newIrrigationDict = {}
        for k, v in timesToConvert.items():
            newIrrigationDict[datetime.datetime.strptime(k,"%Y-%m-%dT%H:%M:%S")] = datetime.timedelta(seconds=v)
        return newIrrigationDict

    @staticmethod
    def isAllOn():
        return Device.allOn
    
    @staticmethod
    def turnAllOff():
        for device in Device.deviceList:
            device.turnOff()

    @staticmethod
    def turnMainStateOn():
        Device.allOn = True 


        
        