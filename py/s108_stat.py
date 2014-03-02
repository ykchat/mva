# coding: UTF-8

import numpy as np

def stat(data):

    result = np.zeros((len(data), 3))

    result[:,0] = data.mean(axis=1)        # 平均
    result[:,1] = data.var(axis=1, ddof=1) # 分散（不偏分散）
    result[:,2] = data.std(axis=1, ddof=1) # 標準偏差

    return result

if __name__ == '__main__':

    heights = (151, 164, 146, 158)
    weights = (48, 53, 45, 61)

    data = np.array([heights, weights])

    print stat(data)
