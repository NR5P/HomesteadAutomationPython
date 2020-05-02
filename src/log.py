logFile = None
import datetime
currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class Log:
    @staticmethod
    def irrigationHigh():
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        global logFile
        logFile.write("irrigation time HIGH" + currentTime + "\n")

    @staticmethod
    def irrigationLow():
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        global logFile
        logFile.write("irrigation time LOW" + currentTime + "\n")

    @staticmethod
    def cycleIrrigationHigh():
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        global logFile
        logFile.write("cycle time HIGH" + currentTime + "\n")

    @staticmethod
    def cycleIrrigationLow():
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        global logFile
        logFile.write("cycle time LOW" + currentTime + "\n")

    @staticmethod
    def close():
        global logFile
        logFile.close()

    @staticmethod
    def initialize():
        global logFile
        logFile = open('log.txt', 'a')