import numpy as np
import pandas as pd



def LSTM_preprocessing(data, step, train_size):
    """This function returns the values preprocessed to train a LSTM model
    parameters:
    data: dataframe 
    step: step size for the sliding window
    train_size = percentage of the train size

    returns: x and y divided in train and test already preprocessed to use the in a LSTM model
    """
    rep_step = data.iloc[-step:, 2:]
    LSTM_df = pd.concat([data, rep_step])
    x_list = []
    y_list = []
    separator = int(train_size * len(data))
    for i in range(len(data)):
        D = i + step
        x_list.append([LSTM_df[x][i:D] for x in data.columns[2:]])
        y_list.append(LSTM_df['Close Price'][D:D+1])
    
    array_x = np.array(x_list)
    array_y = np.array(y_list)

    x_train, x_test = array_x[:separator], array_x[separator:]
    y_train, y_test = array_y[:separator], array_y[separator:]

    return x_train, x_test, y_train, y_test



def build_simple_rnn(num_units=128, embedding=8, num_dense=32,lr=0.001):
    """
    Builds and compiles a simple RNN model
    Arguments:
            num_units: Number of units of a the simple RNN layer
            embedding: Embedding length
            num_dense: Number of neurons in the dense layer followed by the RNN layer
            lr: Learning rate (uses RMSprop optimizer)
    Returns:
            A compiled Keras model.
    """
    model = Sequential()
    # Long short term memory
    model.add(LSTM(units=num_units, input_shape=(1,embedding), activation="relu"))
    model.add(Dense(num_dense, activation="relu"))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer=RMSprop(learning_rate=lr),metrics=['mse'])
    
    return model