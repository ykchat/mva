# coding: UTF-8

import numpy as np

def stat(data):

    result = np.cov(data) # 分散共分散行列

    return result

if __name__ == '__main__':

    heights = (151, 164, 146, 158)
    weights = (48, 53, 45, 61)

    data = np.array([heights, weights])

    print stat(data)
