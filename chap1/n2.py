#import matplotlib.pyplot as plt
import numpy as np 
import random 
import pandas as pd
import numpy as np

from math import sin, pi



def true_function (x):
    y = np.sin(np.pi * x * 0.8) * 10
    return y




observation_P_list = []  # 空の観測地点リストを用意
true_value_list = []  # 空の真値リストを用意

random.seed(0)
for i in range(20):
    x = random.uniform(-1, 1)  # -1 <= x <= 1の範囲で乱数を生成
    observation_P_list.append(x)
    true_value_list.append(true_function(x))
    
observation_P_list = np.array(observation_P_list)
true_value_list = np.array(true_value_list)
    
    


"""

#print(observation_P_list)
#print(true_value_list)

[ 0.6888437   0.51590881 -0.15885684 -0.4821665   0.02254944 -0.19013173
  0.56759718 -0.39337455 -0.04680609  0.16676408  0.81622577  0.00937371
 -0.43632431  0.51160841  0.23673799 -0.49898732  0.81949251  0.96557095
  0.62043447  0.8043319 ]
[ 9.87154416  9.62648605 -3.88728157 -9.36255748  0.56642599 -4.59873863
  9.89611262 -8.35288924 -1.17365411  4.06960288  8.8671641   0.23556528
 -8.89661173  9.59666108  5.6049838  -9.50266942  8.82890871  6.5550276
  9.9993417   9.00137951]
"""


combined_array =np.c_[observation_P_list,true_value_list]

"""
print(combined_array)
[[ 6.88843703e-01  9.87154416e+00]
 [ 5.15908806e-01  9.62648605e+00]
 [-1.58856838e-01 -3.88728157e+00]
 [-4.82166499e-01 -9.36255748e+00]
 [ 2.25494427e-02  5.66425986e-01]
 [-1.90131725e-01 -4.59873863e+00]
 [ 5.67597178e-01  9.89611262e+00]
 [-3.93374548e-01 -8.35288924e+00]
 [-4.68060917e-02 -1.17365411e+00]
 [ 1.66764079e-01  4.06960288e+00]
 [ 8.16225770e-01  8.86716410e+00]
 [ 9.37371163e-03  2.35565277e-01]
 [-4.36324311e-01 -8.89661173e+00]
 [ 5.11608408e-01  9.59666108e+00]
 [ 2.36737993e-01  5.60498380e+00]
 [-4.98987317e-01 -9.50266942e+00]
 [ 8.19492512e-01  8.82890871e+00]
 [ 9.65570952e-01  6.55502760e+00]
 [ 6.20434472e-01  9.99934170e+00]
 [ 8.04331901e-01  9.00137951e+00]]

"""

# DataFrameを作成
df = pd.DataFrame(combined_array, columns=["observation_P", "true_value"])

# 結果を表示
print(df)

