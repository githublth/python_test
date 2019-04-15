# 逻辑文件，调用界面文件


import sys
from PyQt5 import QtWidgets
from  PyQt5.QtWidgets import QMessageBox
from DataAnalysis import ReadTxt


class MyWindow(QtWidgets.QMainWindow, ReadTxt.Ui_MainWindow):

    #实现逻辑部分

    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.action()  # 存放所有的信号槽

    def action(self):
        # 定义按下按钮执行的方法
        self.pushButton.clicked.connect(self.showMsg)
        self.pushButton.clicked.connect(self.buttonClicked)


    def showMsg(self):
        if self.lineEdit.text()=='':
            QMessageBox.information(QtWidgets.QWidget(), "信息提示框", "路径不正确")
        else:
            self.path=self.lineEdit.text()
            QMessageBox.information(QtWidgets.QWidget(), "信息提示框", "成功生成.mat")

    def buttonClicked(self):


        # -*- coding:utf-8 -*-
        # 文本目的：处理从codesys采集的txt文档



        import numpy as np
        from scipy import io

        import matplotlib.pyplot as plt

        import linecache  # 该模块允许从任何文件里得到任何的行

        line_3 = linecache.getline(self.path, 3)  # 读取文件的第3行
        Variable_Name = line_3.split()[1:]  # 去除第一列的时间列
        Variable_Name = [x.replace('[', '').replace(']', '') for x in Variable_Name]  # 去除变量名中的[和]字符

        data = np.genfromtxt(self.path, delimiter=' ', skip_header=3, encoding='UTF-8')  # genfromtxt是一个强大的函数

        names = locals()  # 利用locals()函数动态生成变量名
        for i in range(len(Variable_Name)):  # 读取txt中的数据并赋值给变量
            names[Variable_Name[i]] = data[:, i + 1]
            names[Variable_Name[i]] = names[Variable_Name[i]][~np.isnan(names[Variable_Name[i]])]  # 消去nan值

        # 保存为.mat数据
        dict_data = {}
        for i in np.arange(len(Variable_Name)):
            dict_data[Variable_Name[i]] = eval(Variable_Name[i])

        io.savemat('data.mat', dict_data)  # 保存数据为.mat,从而和matlab交互数据

        # 画图
        # 'b':蓝色  ‘g’：绿色 ‘r’：红色  ‘c’：青色 ‘m’：洋红 ‘k’：黑色 ‘w’：白色
        plt.figure()
        for i in np.arange(len(Variable_Name)):
            if i < 6:
                plt.subplot(2, 3, i + 1)
                plt.plot(eval(Variable_Name[i]))

                # matplotlib.rcParams['font.family'] = 'SimHei'  # 支持中文显示
                plt.xlabel("time(ms)")
                plt.ylabel(Variable_Name[i])
                plt.show()


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myWin=MyWindow()
    myWin.show()
    sys.exit(app.exec_())



