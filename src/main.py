from cycleIrrigation import CycleIrrigation
from irrigation import Irrigation
from device import Device
import RPi.GPIO as GPIO
from log import Log
import time


def main():
    #TODO: grab date from the database to get settings on startup
    global logFile

    Log.initialize()
    setupBoard()
    time.sleep(5)

    CycleIrrigation(3, "by barn","random notes", 12, 5, 10, "2020-03-09T19:44:18", "2020-03-09T06:44:18")
    Irrigation(3, "barn irrigation", "random notes", 16, [1, 4, 5],{"2020-03-08T01:54:57":3600,"2020-04-08T01:52:51":10})
    Device.turnMainStateOn()
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
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    main()

