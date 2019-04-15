
#使用python脚本的方式将.ui转化为.py文件

import os
import os.path

#UI文件所在的路径
dir='./'

#列出目录下的所有UI文件
def listUIFile():
    list=[]
    files=os.listdir(dir)
    for filename in files:
        if os.path.splitext(filename)[1]==".ui":
            list.append(filename)

    return list

#把扩展名为.ui的文件改为扩展名为.py的文件
def transPyFile(filename):
    return os.path.splitext(filename)[0]+'.py'

#调用系统命令把UI文件转换为python文件
def runMain():
    list=listUIFile()
    for uifile in list:
        pyfile=transPyFile(uifile)
        cmd ='pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)
        os.system(cmd)

#程序的主入口
if __name__=='__main__':
    runMain()