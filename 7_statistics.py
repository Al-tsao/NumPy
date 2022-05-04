#統計運算

#載入模組
import numpy as np

#建立陣列
data1 = np.array([
    [2, 1, 7],
    [3, -5, 8]
])

#運算
data1.sum() #全部加總
data1.sum(axis = 0) #加總column
data1.sum(axis = 1) #加總row
