#Homework 3 胡塾绪 2014301020108
##摘要
本文介绍了一种用python实现字符水平移动的方法以及设计了一个旋转的stick.
##正文
###1.水平移动
上次作业中已经拼写了自己的名字，为实现水平移动，作者利用了清屏和暂停命令。

清屏：

import os

i = os.system('cls')

暂停:

time.sleep()

括号中是让程序暂停的秒数.
用手动增加空格的方法使字符向右移动一次，在未移动和移动后的字符中间插入如上两个命令就可实现水平移动。重复上述操作，就可实现连续的移动。
[代码在此](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-3/%E6%B0%B4%E5%B9%B3%E7%A7%BB%E5%8A%A8.py)

执行效果如下：

