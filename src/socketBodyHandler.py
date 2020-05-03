import json

class SocketBodyHandler:
    def __init__(self,jsonText):
        self.socketDataDict = json.loads(jsonText)

    def getPurpose(self):
        if socketDataDict["purpose"] == "checkDB":
            #TODO: check the database and add, remove, or modify
            print("checking the db")
        elif socketDataDict["purpose"] == "test":
            #TODO: test all the valves one by one
            pass