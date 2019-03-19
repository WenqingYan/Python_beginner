# encoding=utf8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.5', '0.6', '0.7', '0.8', '0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0']
x = range(len(names))
y = [21.83468967,22.6782449,22.93430108,21.25625279,20.44286396,20.91914576,21.23495125,21.59001477,22.36346805,23.08897248,23.75214622,24.93747974,25.21955438,26.10012006,26.54489741,27.13799267]
y1=[329.4249826,252.4586697,140.2121354,92.71050662,72.19954984,59.75124684,53.56468332,49.07447623,44.70338388,43.59911693,43.42282239,40.73737397,38.33333555,37.6000134,37.36318906,37.06890861]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
plt.xlim(-1, 3)  # 限定横轴的范围
plt.ylim(0, 350)  # 限定纵轴的范围
plt.plot(x, y, marker='o', color='r', mec='r', mfc='w',label=u'无OTN交换的传统场景')
plt.plot(x, y1, marker='^', ms=5,label=u'OTN交换场景')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"总流量(Tbps)") #X轴标签
plt.ylabel("EEPG(kbps/Joule/GHz)") #Y轴标签

plt.show()
