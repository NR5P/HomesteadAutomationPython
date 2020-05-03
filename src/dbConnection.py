import pymongo
from pymongo import MongoClient
from device import Device

class DbConnection:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost/homestead")
        print("mongodb connected from python")
        self.db = client["homestead"]
        
        self.irrigationCollection = db["irrigationschemas"]
        self.cycleIrrigationCollection = db["cycleirrigationschemas"]

        self.equalizeDevicesWithDb()

    def equalizeDevicesWithDb(self):
        pass

    def checkAgainstIrrigation(self):
        for dbDevice in irrigationCollection.find():
            for device in Device.deviceList:


    def checkAgainstCycleIrrigation(self):
        pass