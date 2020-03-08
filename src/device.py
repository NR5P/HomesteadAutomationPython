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

    def __init__(self, id, name, notes, pin):
        self.id = id
        self.name = name
        self.notes = notes
        self.pin = pin
        self.state = False
        self.createdOn = datetime.datetime.now()
    
    def setNewId(self, newId):
        for i in Device.deviceList:
            if i.id == newId:
                return False
        self.id = newId
        return True
    
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
    
    @staticmethod
    def convertDatetimeToTimeDelta(isoDateTime):
        return datetime.timedelta(hours=int(isoDateTime[11:13]),
                                  minutes=int(isoDateTime[14:16]),
                                  seconds=int(isoDateTime[17:19]))


        
        