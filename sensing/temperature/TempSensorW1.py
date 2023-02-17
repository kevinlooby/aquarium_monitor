import glob
import os
import re


class TempSensorW1:
    devices_dir = '/sys/bus/w1/devices/'

    def __init__(self, device_name):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        # device_folder = glob.glob(self.devices_dir + '28*')[0]
        device_folder = self.devices_dir + device_name
        self.device_file = device_folder + '/w1_slave'

    def read_value(self):
        content = self.read_file()
        temp = self.parse_temperature(content)
        return temp

    @staticmethod
    def parse_temperature(content):
        pattern = re.compile('t=')

        if 'YES' not in content[0]:
            t = -1
        else:
            try:
                text = pattern.split(content[1])[1]
                t = float(text) / 1000
            except TypeError:
                t = -1

        return t

    def read_file(self):
        with open(self.device_file, 'r') as f:
            content = f.readlines()

        return content
