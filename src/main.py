from cycleIrrigation import CycleIrrigation
from irrigation import Irrigation
from device import Device
import RPi.GPIO as GPIO

def main():
    #TODO: grab date from the database to get settings on startup

    setupBoard()

    CycleIrrigation(3, "by barn","random notes", 7, 10, 600, "2020-03-09T19:44:18+0000", "2020-03-09T06:44:18+0000")
    Irrigation(3, "barn irrigation", "random notes", 11, [1, 4, 5],{"2020-03-08T01:54:57+0000":3600,"2020-04-08T01:52:51+0000":10})
    Device.turnMainStateOn()
    while True: 
        if Device.isAllOn():
            for device in Device.deviceList:
                device.run()
        else:
            Device.turnAllOff()
    cleanup()

def setupBoard():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    main()

