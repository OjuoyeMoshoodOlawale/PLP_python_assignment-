# import example
# import math as m
# print(example.sum(2,5))
# print(m.pi)

import numpy as np
import pandas as pd
# a=np.array([[1,2,3], [4,5,6]])
# b=np.array([[0,2,3], [4,5,6]])
# # print(a+b)
# # print(a*b)
# # print(a[0][1])
# a=np.array([a for a in range(10)])
# a_reshape=a.reshape((2,5))
# print(a_reshape)

# data=pd.read_csv('sample_data.csv')

# print(data['CustomerName'])
import matplotlib.pyplot as plt
x=[0,30,45,60,90]
y=[ np.sin(a) for a in x]
plt.boxplot(x,y)
plt.xlabel("MY X AXIS")
plt.ylabel("MY YAXIS")
plt.title("Hello world")
plt.show()