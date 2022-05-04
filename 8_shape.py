#維度: 資料的層次
#形狀: 同時表達資料的層次，和每個層次的資料數量

#載入模組
import numpy as np

#建立陣列
data = np.array([
    [2, 1, 7],
    [3, -5, 8]
])

#觀察資料形狀
data.shape

#資料傳置
data.T.shape

#扁平化資料: 變成一維陣列
data.ravel()

#重塑資料形狀: 前提是資料總數量必須要一樣
print(data.reshape(2, 3, 1))
