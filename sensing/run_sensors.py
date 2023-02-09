from sensing.ph.PHSensorI2C import PHSensorI2C
from sensing.temperature.TempSensorW1 import TempSensorW1
from SensorRepository import SensorRepository
from datetime import datetime
from backend import resources
import time
import os


def main():
    # Initialize mySQL DB connection
    config_path = os.path.join(os.path.dirname(resources.__file__), "db_config.yml")
    repo = SensorRepository(config_path)

    # Initialize sensors
    ph_sensor = PHSensorI2C()
    temp_sensor = TempSensorW1()

    # Sample sensors
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        temperature = temp_sensor.read_value()
        ph = ph_sensor.read_value(temperature)

        repo.insert_value(timestamp, temperature, repo.db_tables['temperature'])
        repo.insert_value(timestamp, ph, repo.db_tables['ph'])

        time.sleep(30)


if __name__ == '__main__':
    main()
