from datetime import timedelta
from datetime import datetime
import numpy as np


def build_training_point(data, t_str, history_days=64, horizon_days=1):
    '''

    :param data:
    :param t_str:
    :param history_days:
    :param horizon_days:
    :return:
    '''

    # Cast for indexing
    t_datetime = datetime.strptime(t_str, "%Y-%m-%d 00:00:00")

    # Create training example (x,y)
    try:
        x = data.loc[t_datetime - timedelta(days=history_days - 1):t_datetime]
        y = data.loc[t_datetime + timedelta(days=1):t_datetime + timedelta(days=horizon_days)]
    except KeyError:
        raise KeyError("The date {} is not in the data".format(t_str))

    # Return
    return x, y


def create_training_points(data, history_days=64, horizon_days=32):
    '''

    :param data:
    :param history_days:
    :param horizon_days:
    :return:
    '''
    X = []
    Y = []
    for t in data.index[history_days:(len(data) - horizon_days)]:
        try:
            x, y = build_training_point(data, str(t), history_days=history_days, horizon_days=horizon_days)
            if (len(x) == history_days) & (len(y) == horizon_days):
                X.append(x)
                Y.append(y)
        except KeyError:
            continue
    X = np.stack(X)
    Y = np.stack(Y)
    return X, Y
