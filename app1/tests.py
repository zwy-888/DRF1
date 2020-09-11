from django.test import TestCase

# Create your tests here.
# for i in range(6):
#     for k in range(5-i):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*", end=" ")
#     print()

# for i in range(6):
#     for k in range(5 - i):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("⭐", end=" ")
#     print()
# for i in range(5):
#     for k in range(i + 1):
#         print(" ", end=" ")
#     for m in range((9 - 3 * i) + i):
#         print("⭐", end=" ")
#     print()


# rows = 5
# # for循环打印
# for x in range(rows):
#     # if判断，筛选第一行与最后一行
#     if x == 0 or x == rows - 1:
#         print(' *' * rows)
#     # else筛选打印剩余行数
#     else:
#         print(' *' + '  ' * (rows - 2) + ' *')

import matplotlib.pyplot as plt

plt.plot([5,2,3,4], [5,4,9,16], )#x=[1,2,3,4],y=[1,4,9,16],'ro'表示红色的圆点

#axis接收的list参数表示：[xmin, xmax, ymin, ymax]

plt.axis([0, 6, 0, 20])#设置x、y轴的长度，x轴为[0,6],y轴为[0,20]

plt.show()