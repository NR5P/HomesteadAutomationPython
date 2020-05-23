from cycleIrrigation import CycleIrrigation
from irrigation import Irrigation
from device import Device
from log import Log
from socketcom import SocketCom
from dbConnection import DbConnection
import time, threading
import RPi.GPIO as GPIO


def main():
    #TODO: grab date from the database to get settings on startup
    global logFile

    Log.initialize()
    setupBoard()
    time.sleep(5)

    db = DbConnection()

    #CycleIrrigation(3, "by barn","random notes", 12, 5, 10, "2020-03-09T19:44:18", "2020-03-09T06:44:18") #TODO: test data
    #Irrigation(3, "barn irrigation", "random notes", 16, [1, 4, 5],{"2020-03-08T01:54:57":3600,"2020-04-08T01:52:51":10}) #TODO: test data
    Device.turnMainStateOn()

    socket = SocketCom()
    thread = threading.Thread(target=socket.start)
    thread.start()

    while True: 
        if Device.isAllOn():
            for device in Device.deviceList:
                device.run()
        else:
            Device.turnAllOff()
    cleanup()
    Log.close()

def setupBoard():
    GPIO.setmode(GPIO.BCM)
    for pin in Device.outputPinDict.keys():
        GPIO.setup(pin,GPIO.OUT) 
        GPIO.output(pin, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    main()

