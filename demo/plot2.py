# encoding=utf8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.5', '0.6', '0.7', '0.8', '0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0']
x = range(len(names))
y = [0.46161382,
y1=[5.371270834,
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
plt.xlim(-1, 3)  # 限定横轴的范围
plt.ylim(0, 6)  # 限定纵轴的范围
plt.plot(x, y, marker='o', color='r', mec='r', mfc='w',label=u'无OTN交换的传统场景')
plt.plot(x, y1, marker='^', ms=5,label=u'OTN交换场景')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"总流量(Tbps)") #X轴标签
plt.ylabel("CEPG(Mbps/CU/GHz)") #Y轴标签

plt.show()