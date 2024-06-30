    
from pywinusb import hid
import time

class PIC18f:
    def __init__(self, VID = 0x04D8, PID=0x003f):

        filter = hid.HidDeviceFilter(vender_id = VID, product_id = PID)
        self.devices = filter.get_devices()
        self.device = self.devices[0]
        self.device.open()


    def write(self, args):

        out_report = self.device.find_output_reports()
        out_report[0].set_raw_data(args)
        out_report[0].send()
        time.sleep(1)

    def read_handler(self, data):
        print("Raw data: {0}".format(data))
        print("done")