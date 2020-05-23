import mysql.connector
from mysql.connector import Error
from device import Device
from cycleIrrigation import CycleIrrigation

class DbConnection:
    def __init__(self):
        self.connection = self.create_connection("localhost", "pi", "Orangev8z", "homestead")
        self.equalizeDevicesWithDb()

    def equalizeDevicesWithDb(self):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM cycleIrrigation")
        irrigationResult = mycursor.fetchall()

        for item in irrigationResult:
            onTimeSeconds = item[4] * 3600 + item[5] * 60 + item[6]
            offTimeSeconds = item[7] * 3600 + item[8] * 60 + item[9]
            blackoutStarttime = f"0000-00-00T{item[10]}:00"
            blackoutStoptime = f"0000-00-00T{item[11]}:00"
            Device.deviceList.append(CycleIrrigation(item[0],item[1],item[2],item[12],onTimeSeconds,offTimeSeconds,
                                    blackoutStarttime, blackoutStoptime))

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
