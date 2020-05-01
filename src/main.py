from cycleIrrigation import CycleIrrigation
from irrigation import Irrigation
from device import Device

def main():
    #TODO: grab date from the database to get settings on startup
    while True: 
        if Device.isAllOn():
            for device in Device.deviceList:
                device.run()
        else:
            Device.turnAllOff()

if __name__ == "__main__":
    main()

