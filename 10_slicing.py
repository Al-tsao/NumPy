#維度: 資料的層次
#形狀: 同時表達資料的層次，和每個層次的資料數量

#載入模組
import numpy as np

#建立陣列
data = np.arange(10)
data2 = data.reshape(2, 5)

#slicing
data[0:2]
data2[0:2, 1]
data2[0:2, ...] #...表示全都要