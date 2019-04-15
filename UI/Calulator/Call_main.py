# 逻辑文件，调用界面文件


import sys
from PyQt5 import QtWidgets

from wswp_second.UI.Calulator import UI


class MyWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):

    #计算器实现逻辑部分

    #定义5个类变量，公用变量
    lcdstring=''  #用来显示lcd上的字符
    operation=''  #定义一个操作符
    currentNum=0  #当前值
    previousNum=0 #上一个值
    result=0      #存放结果

    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.action()  # 存放所有的信号槽

    def action(self):
        # 定义按下数字执行的方法
        self.num_0.clicked.connect(self.buttonClicked)
        self.num_1.clicked.connect(self.buttonClicked)
        self.num_2.clicked.connect(self.buttonClicked)
        self.num_3.clicked.connect(self.buttonClicked)
        self.num_4.clicked.connect(self.buttonClicked)
        self.num_5.clicked.connect(self.buttonClicked)
        self.num_6.clicked.connect(self.buttonClicked)
        self.num_7.clicked.connect(self.buttonClicked)
        self.num_8.clicked.connect(self.buttonClicked)
        self.num_9.clicked.connect(self.buttonClicked)

        #定义按下操作符执行的方法
        self.add.clicked.connect(self.opClicked)
        self.sub.clicked.connect(self.opClicked)
        self.mul.clicked.connect(self.opClicked)
        self.div.clicked.connect(self.opClicked)

        # 定义按下清除键执行的方法
        self.CE.clicked.connect(self.clearClicked)

        # 定义按下等于号执行的方法
        self.equ.clicked.connect(self.equalClicked)


    def buttonClicked(self):
        if len(self.lcdstring)<=9:
            self.lcdstring=self.lcdstring+self.sender().text()
            # 新lcd的显示内容=老lcd的显示内容+按钮传过来的对象的text值
            if str(self.lcdstring)=='.':   #若第一次输入时为1个点
                self.lcdstring='0.' #把'.'替换为'0.'
                self.currentNum=float(self.lcdstring)
                # 将lcd中的数字强制转换为浮点型，方便小数计算
            else:
                self.lcd.display(self.lcdstring)
                # 将self.lcdstring值在lcd中显示出来
                self.currentNum = float(self.lcdstring)  # 无法将字符串转换为浮点型
                # 将lcd中的数字强制转换为浮点型，方便小数计算
        else:  # lcd长度大于9
            pass

    def opClicked(self):
        # 按下等号后都要,清空操作符，为后续判断是否是连续运算做准备(比如9 * 9 * 9 = 729，但若不判断是否是连续运算程序则只运算等号前一步运算即9 * 9 = 81)
        if self.operation != '':  # 操作符不是空的，证明是连续运算
            self.equalClicked()
            self.previousNum = self.currentNum  # 将当前值传送给previousNum变量
            self.currentNum = 0  # 并把当前值清零
            self.lcdstring = ''  # 按下操作符后lcd显示屏首先会被清空
            self.operation = self.sender().text()  # 操作符等于按钮传过来的对象的text值
        else:
            self.previousNum = self.currentNum  # 将当前值传送给previousNum变量
            self.currentNum = 0  # 并把当前值清零
            self.lcdstring = ''  # 按下操作符后lcd显示屏首先会被清空
            self.operation = self.sender().text()  # 操作符等于按钮传过来的对象的text值





    def clearClicked(self):
        #清除键按下去就是把所有参数清零即可
        self.lcdstring=''
        self.operation=''
        self.currentNum=0
        self.previousNum=0
        self.result=0
        self.lcd.display(0) #把lcd中的数字改为0

    def equalClicked(self):
        if self.operation == '+':  # 当操作符为加号
            self.result = self.previousNum + self.currentNum  # 结果就是上一个值加当前值
            self.lcd.display(self.result)  # 把结果显示在lcd中

        if self.operation == '-':  # 当操作符为减号
            self.result = self.previousNum - self.currentNum  # 结果就是上一个值减当前值
            self.lcd.display(self.result)  # 把结果显示在lcd中

        if self.operation == '*':  # 当操作符为乘号
            self.result = self.previousNum * self.currentNum  # 结果就是上一个值乘当前值
            self.lcd.display(self.result)  # 把结果显示在lcd中

        if self.operation == '/':  # 当操作符为除以号
            if self.currentNum == 0:
                self.lcd.display('Error')
                self.result = 0  # 出现错误后将结果清零
                self.previousNum = 0  # 上一个值清零
            else:
                self.result = self.previousNum / self.currentNum  # 结果就是上一个值除当前值
                self.lcd.display(self.result)  # 把结果显示在lcd中

        self.currentNum = self.result  # 将运算的结果result顺便保存到currentNum当前值里,为后续计算做准备.否则无法准确计算紧接着操作.
        self.lcdstring = ''  # 将lcdstring顺便清空,为后续计算做准备.否则无法准确计算紧接着操作.相当于初始化
        self.operation = ''  # 清空操作符，为后续判断是否是连续运算做准备(比如9*9*9=729，但若不判断是否是连续运算程序则只运算等号前一步运算即9*9=81)


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myWin=MyWindow()
    myWin.show()
    sys.exit(app.exec_())