import os
import glob
import re
import time
import datetime
import pymysql


def initialize_device():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    devices_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(devices_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    return device_file


def read_file(device_file):
    with open(device_file, 'r') as f:
        content = f.readlines()

    return content


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
            # print(content[1])

    return t


def write_to_db_proto(timestamp, temperature):
    connection = pymysql.connect(user='admin', password='password', database='aquarium_monitor', host='localhost')
    cursor = connection.cursor()

    ts = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    message = "INSERT INTO temperature (timestamp, value) VALUES ('{}', {});".format(ts, temperature)

    print(message)
    ret = cursor.execute(message)
    connection.commit()
    connection.close()


def main():
    device_file = initialize_device()

    while True:
        content = read_file(device_file)
        temp = parse_temperature(content)
        write_to_db_proto(time.time(), temp)

        time.sleep(30)


if __name__ == '__main__':
    main()
