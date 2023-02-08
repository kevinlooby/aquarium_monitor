from DFRobot_PH.DFRobot_ADS1115 import ADS1115, ADS1115_REG_CONFIG_PGA_6_144V
from DFRobot_PH.DFRobot_PH import DFRobot_PH
from common.repositories.BaseRepository import BaseRepository
import os
from backend import resources
import time


class SensorRepository(BaseRepository):

    def __init__(self, config_path):
        super().__init__(config_path)
        self.load_config()
        self.db_tables = self.config['db_tables']
        self.load_db(self.config['db_configuration'])

    def store_ph(self, timestamp, ph):
        query_str = "INSERT INTO pH (timestamp, value) VALUES ({}, {});".format(int(timestamp), ph)
        self.db_insert(query_str)


def main():
    repo = SensorRepository(os.path.join(os.path.dirname(resources.__file__), "db_config.yml"))
    ads1115 = ADS1115()
    ph_sensor = DFRobot_PH()

    ph_sensor.begin()

    while True:
        temperature = 25

        ads1115.set_addr_ads1115(0x48)
        ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
        adc0 = ads1115.read_voltage(0)
        ph = ph_sensor.read_PH(adc0['r'], temperature)

        repo.store_ph(time.time(), ph)


if __name__ == '__main__':
    main()
