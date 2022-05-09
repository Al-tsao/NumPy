#載入模組
import numpy as np

#載入資料
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
])

#stacking
result1 = np.vstack(arr, 2) #根據第一個維度切割
result2 = np.hstack(arr, 2) #根據第二個維度切割
