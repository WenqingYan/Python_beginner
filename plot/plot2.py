# encoding=utf8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.5', '0.6', '0.7', '0.8', '0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0']
x = range(len(names))
y = [0.46161382,0.480247792,0.486472073,0.45161464,0.408150619,0.427443807,0.433896705,0.433611781,0.449145743,0.464539383,0.476122568,0.498943214,0.504586897,0.521240553,0.527291193,0.540019693]
y1=[5.371270834,4.115894817,2.28525522,1.525767156,1.187868206,0.905134133,0.816260115,0.752084025,0.685764457,0.672649892,0.670491196,0.631792719,0.595587239,0.58908598,0.587860977,0.583491753]
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
