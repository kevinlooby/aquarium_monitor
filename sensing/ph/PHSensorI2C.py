from DFRobot_PH.DFRobot_ADS1115 import ADS1115, ADS1115_REG_CONFIG_PGA_6_144V
from DFRobot_PH.DFRobot_PH import DFRobot_PH


class PHSensorI2C:

    def __init__(self):
        self.ads1115 = ADS1115()

        self.ph_sensor = DFRobot_PH()
        self.ph_sensor.begin()

    def read_value(self, temperature=24.5):
        self.ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
        adc0 = self.ads1115.read_voltage(0)
        ph = self.ph_sensor.read_PH(adc0['r'], temperature)
        return ph, adc0['r']


class TempSensorI2C:

    def __init__(self):
        self.ads1115 = ADS1115()

        self.ph_sensor = DFRobot_PH()
        self.ph_sensor.begin()

    def read_value(self):
        self.ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
        adc1 = self.ads1115.read_voltage(1)
        return adc1
