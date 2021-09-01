from DWX_ZeroMQ_Connector_v2_0_1 import DWX_ZeroMQ_Connector
import pandas as pd
import numpy as np
import time
import sys, os
import zmq
from tensorflow import keras
from DWX_history import DWX_MT_HISTORY_IO

dir = os.path.dirname

path = dir(dir(os.path.abspath(__file__)))
sys.path.append(path)

from src.utils.mining_data_tb import final_add_features
from src.utils.models import final_preprocessing
model_path = path + os.sep + 'src' + os.sep + 'models' + os.sep + 'tuned_CNN.h5'

model = keras.models.load_model(model_path)

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
compared_prices = []
counter = 0
predictions=[]
actual_price = []
pred_dates = []
counter = 0
time.sleep(15)
if len(date) == 210:
    print('Data collected is enough to start feeding the model')
while counter < 400:

# Ojo  mirar los  contadores
    if counter == 0:
        for i in _zmq._Market_Data_DB['EURUSD_M1'].keys():
            date.append(i)
            open_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][1])
            low_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][2])
            high_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][3])
            volume.append(0)
            close_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][i][4])
            print('Started collecting first data')
            counter += 1
    else:
        time.sleep(15)
        if len(_zmq._Market_Data_DB['EURUSD_M1']) > len(date):
            if len(predictions)> 0:
                # Para que estén alineados el tiempo con la predicción
                
                date.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]])
                open_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][1])
                low_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][2])
                high_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][3])
                volume.append(0)
                close_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][4])
                actual_price.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][4])
                counter += 1
                
            else:
                date.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]])
                open_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][1])
                low_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][2])
                high_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][3])
                volume.append(0)
                close_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][4])
                counter += 1
                print(f'{len(date)}/210 of data collected to start predicting')

            if len(date) >= 210 and len(compared_prices) == 0:
                compared_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][4])


            elif len(date) >= 210 and len(compared_prices) > 0:
                pred_dates.append(list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1])
                pred_df = pd.DataFrame({'Date': date, 'Open price': open_prices, 'Low price': low_prices, 'High price': high_prices, 'volume': volume, 'Close price': close_prices})
                pred_df = final_add_features(pred_df).iloc[-10:, :]
                print('df for input:',pred_df)
                prediction_input = final_preprocessing(pred_df, 10)
                print('input shape:')
                print(prediction_input.shape)
                predictions.append(model.predict(prediction_input)[-1])
                print('prediction:', model.predict(prediction_input)[-1])
                compared_prices.append(_zmq._Market_Data_DB['EURUSD_M1'][list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]][4])
                print('prediction made with data date:', {list(_zmq._Market_Data_DB['EURUSD_M1'].keys())[-1]})
                

print('lenght pred date:', len(pred_dates))
print('length actual price:', len(compared_prices))
print('length predictions:', len(predictions))
historico = pd.DataFrame({'prediction date': pred_dates,  'close price': compared_prices[:-1], 'prediction': predictions} )
historic_path = path + os.sep + 'data' + os.sep + 'historico4.csv'
historico.to_csv(historic_path, header= True)