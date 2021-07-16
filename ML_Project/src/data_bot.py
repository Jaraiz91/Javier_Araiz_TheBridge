from DWX_ZeroMQ_Connector_v2_0_1 import DWX_ZeroMQ_Connector
import pandas as pd
import numpy as np
import struct
import time
import sys, os
import zmq
from DWX_history import DWX_MT_HISTORY_IO

# stablish connection with trading platform
_zmq = DWX_ZeroMQ_Connector()
_zmq._DWX_MTX_SUBSCRIBE_MARKETDATA_('EURUSD')
_zmq._DWX_MTX_SEND_TRACKRATES_REQUEST_(_instruments=[('EURUSDS_M1', 'EURUSD', 1)])

date = []
open_prices = []
low_prices = []
high_prices = []
volume = []
close_prices = []
counter = 0
while True:

    if counter == 0:
        for i in _zmq._Market_Data_DB['EURUSD_M1'].keys():
            date.append(i)
            open_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][1])
            low_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][2])
            high_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][3])
            volume.append(0)
            close_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][4])
    else:
        time.sleep(15)
        if len(_zmq._Market_Data_DB['EURUSD_M1']) > len(date):
            date.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]])
            open_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][1])
            low_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][2])
            high_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][3])
            volume.append(0)
            close_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][4])
