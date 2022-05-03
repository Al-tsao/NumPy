#矩陣運算

#載入模組
import numpy as np

#建立陣列
data1 = np.array([
    [2, 1]
])
data2 = np.array([
    [3, 2, 0],[3, 1, -1]
])

#運算
data1.dot(data2) #內積
data1@(data2) #內積
np.outer(data1, data2) #外積
