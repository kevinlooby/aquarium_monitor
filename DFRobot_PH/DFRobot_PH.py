'''!
  @file DFRobot_PH.py
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author [Jiawei Zhang](jiawei.zhang@dfrobot.com)
  @version  V1.0
  @date  2018-11-06
  @url https://github.com/DFRobot/DFRobot_PH
'''

import time
import sys


class DFRobot_PH:
    def __init__(self):
        self._temperature = 25.0
        self._acidVoltage = 2032.44
        self._neutral_voltage = 1500.0

    def begin(self):
        '''!
          @brief   Initialization The Analog pH Sensor.
        '''

        try:
            with open('phdata.txt', 'r') as f:
                neutralVoltageLine = f.readline()
                neutralVoltageLine = neutralVoltageLine.strip('neutralVoltage=')
                self._neutralVoltage = float(neutralVoltageLine)
                acidVoltageLine = f.readline()
                acidVoltageLine = acidVoltageLine.strip('acidVoltage=')
                self._acidVoltage = float(acidVoltageLine)
        except FileNotFoundError:
            print("phdata.txt ERROR ! Running DFRobot_PH_Reset")
            # sys.exit(1)
            self.reset()

    def read_PH(self, voltage, temperature):
        '''!
          @brief   Convert voltage to PH with temperature compensation.
          @note voltage to pH value, with temperature compensation
          @param voltage       Voltage value
          @param temperature   Ambient temperature
          @return  The PH value
        '''
        slope = (7.0 - 4.0) / ((self._neutralVoltage - 1500.0) / 3.0 - (self._acidVoltage - 1500.0) / 3.0)
        intercept = 7.0 - slope * (self._neutralVoltage - 1500.0) / 3.0
        _phValue = slope * (voltage - 1500.0) / 3.0 + intercept
        round(_phValue, 2)
        return _phValue

    @staticmethod
    def calibration(voltage):
        '''!
          @brief   Calibrate the calibration data.
          @param voltage       Voltage value
        '''
        if 1322 < voltage < 1678:
            print(">>>Buffer Solution:7.0")
            f = open('phdata.txt', 'r+')
            flist = f.readlines()
            flist[0] = 'neutralVoltage=' + str(voltage) + '\n'
            f = open('phdata.txt', 'w+')
            f.writelines(flist)
            f.close()
            print(">>>PH:7.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
            time.sleep(5.0)
        elif 1854 < voltage < 2210:
            print(">>>Buffer Solution:4.0")
            f = open('phdata.txt', 'r+')
            flist = f.readlines()
            flist[1] = 'acidVoltage=' + str(voltage) + '\n'
            f = open('phdata.txt', 'w+')
            f.writelines(flist)
            f.close()
            print(">>>PH:4.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
            time.sleep(5.0)
        else:
            print(">>>Buffer Solution Error Try Again<<<")

    @staticmethod
    def reset():
        '''
          @brief   Reset the calibration data to default value.
        '''

        _acidVoltage = 2032.44
        _neutralVoltage = 1500.0
        try:
            f = open('phdata.txt', 'r+')
            flist = f.readlines()
            flist[0] = 'neutralVoltage=' + str(_neutralVoltage) + '\n'
            flist[1] = 'acidVoltage=' + str(_acidVoltage) + '\n'
            f = open('phdata.txt', 'w+')
            f.writelines(flist)
            f.close()
            print(">>>Reset to default parameters<<<")
        except:
            f = open('phdata.txt', 'w')
            # flist=f.readlines()
            flist = 'neutralVoltage=' + str(_neutralVoltage) + '\n'
            flist += 'acidVoltage=' + str(_acidVoltage) + '\n'
            # f=open('data.txt','w+')
            f.writelines(flist)
            f.close()
            print(">>>Reset to default parameters<<<")
