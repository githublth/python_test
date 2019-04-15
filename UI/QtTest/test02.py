from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
import sys

app=QApplication([])
widget=QWidget()

def showMsg():
    QMessageBox.information(widget,"信息提示狂",'ok,弹出测试新')

btn=QPushButton("测试点击按钮",widget)
btn.clicked.connect(showMsg)

widget.show()
sys.exit(app.exec_())