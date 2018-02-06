# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

#从纵轴开始均匀分布的点，实现均匀分布用0，1，2，3...作横轴标点。然后修改label
names = ['0.5', '0.6', '0.7', '0.8', '0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0']
x = range(len(names))
y = [20.44,23.47,26.91,32.98,37.66,40.65,44.05,46.44,48.57,50.370003,52.34,52.749996,55.42,56.25,57.79,59.17]
y1=[1.77,2.71,5.56,9.2,13.0199995,16.230001,19.37,22.45,26.230001,28.529999,30.17,33.03,35.88,37.56,39.010002,40.78]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
plt.xlim(-1, 16)  # 限定横轴的范围
plt.ylim(0, 70)  # 限定纵轴的范围
plt.plot(x, y, marker='o', color='r', mec='r', mfc='w',label=u'无OTN交换的传统场景')
plt.plot(x, y1, marker='^', ms=5,label=u'OTN交换场景')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"总流量(Tbps)") #X轴标签
plt.ylabel("频谱占用率(%)") #Y轴标签

plt.show()
