import matplotlib.pyplot as plt
import numpy as np 

from math import sin, pi


def true_function (x):
    y = np.sin(np.pi * x * 0.8) * 10
    return y


#print(true_function(0))

#print(true_function(1))


# xを定義 ----------
x = np.linspace(-2, 2, 100)                   # (B) xを100個準備

# グラフ描画 ----------
plt.plot(x, true_function(x), "black")              # (C) fのグラフ

plt.legend(loc="upper left")                         # (E) 凡例表示
plt.title("    y = sin(pi * x * 0.8) * 10")             # (F) タイトル
plt.xlabel("x")                                      # (G) xラベル
plt.ylabel("y")                                      # (H) yラベル
plt.xlim(-1, 1)                                      # (I) x軸の範囲
plt.grid()                                           # (K) グリッド
plt.show()


