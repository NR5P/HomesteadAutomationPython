import mysql.connector
from mysql.connector import Error
from device import Device
from cycleIrrigation import CycleIrrigation
from irrigation import Irrigation

class DbConnection:
    def __init__(self):
        self.connection = self.create_connection("localhost", "pi", "Orangev8z", "homestead")
        self.equalizeDevicesWithDb()

    def equalizeDevicesWithDb(self):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM cycleIrrigation")
        cycleIrrigationResult = mycursor.fetchall()

        for item in cycleIrrigationResult:
            onTimeSeconds = item[4] * 3600 + item[5] * 60 + item[6]
            offTimeSeconds = item[7] * 3600 + item[8] * 60 + item[9]
            blackoutStarttime = f"1900-01-01T{item[10]}:00"
            blackoutStoptime = f"1900-01-01T{item[11]}:00"
            Device.deviceList.append(CycleIrrigation(item[0],item[1],item[2],item[12],onTimeSeconds,offTimeSeconds,
                                    blackoutStarttime, blackoutStoptime))

        mycursor.execute("SELECT irrigation.id, irrigation.pin, irrigation.name, irrigation.notes, irrigation.state, irrigation.daysToIrrigate, irrigationRunTimes.startTime, irrigationRunTimes.runTime  FROM irrigation JOIN irrigationRunTimes ON irrigation.id = irrigationRunTimes.irrigationId ORDER BY id")
        irrigationResult = mycursor.fetchall()
        irrigationObject = None
        for index, item in enumerate(irrigationResult):
            irrigationObject = Irrigation(item[0],item[2],item[3],item[1],item[5],None)
            print(item[6])
            print(item[7])
            irrigationObject.irrigationTimes[item[6]] = item[7]
            if index != 0 and CycleIrrigation.id != item[0]:
                Device.deviceList.append(irrigationObject) 
                irrigationObject = None
        if irrigationObject != None:
            Device.deviceList.append(irrigationObject) 

    def create_connection(self, host_name, user_name, user_password, database):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=database
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection
