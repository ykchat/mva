# coding: UTF-8

import numpy as np

def stat(data):

    mean = data.mean(axis=1)[:, np.newaxis]       # 平均
    std = data.std(axis=1, ddof=1)[:, np.newaxis] # 標準偏差

    result = (data - mean) / std # データの標準化

    return result

if __name__ == '__main__':

    heights = (151, 164, 146, 158)
    weights = (48, 53, 45, 61)

    data = np.array([heights, weights])

    print stat(data)
