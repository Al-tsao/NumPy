#載入模組
import numpy as np

#載入資料
arr1 = np.array([
    [3, 4]
])

arr2 = np.arrat([
    [5, 6]
])

#stacking
result1 = np.vstack((arr1, arr2)) #合併第一個維度
result2 = np.hstack((arr1, arr2)) #合併第二個維度
