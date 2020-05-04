import pymongo
from pymongo import MongoClient
from device import Device

class DbConnection:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost/homestead")
        print("mongodb connected from python")
        self.db = client["homestead"]
        
        self.irrigationCollection = db.irrigationschemas
        self.cycleIrrigationCollection = db.cycleirrigationschemas

        self.equalizeDevicesWithDb()

    def equalizeDevicesWithDb(self):
        idListOfDeviceList = []
        for dbDevice in irrigationCollection.find():
            for device in Device.deviceList:
                idListOfDeviceList.append(device.id)
                if dbDevice._id == device.id:
                    if dbDevice.type == 1:
                        #cycle irrigation
                        pass
                    elif dbDevice.type == 2:
                        #irrigation
                        pass
                else:
                    #not here so add
            #check if one needs to be deleted that has been deleted in db
