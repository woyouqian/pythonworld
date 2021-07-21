import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from gongshi import Ui_Form


class Widget(QWidget, Ui_Form):

    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.gethelp)

    def gethelp(self):
        info = '''a、b、h、r分别为长宽高半径取值；
        工具实现对应项的面积体积计算，
        默认为平行四边形；当选中圆柱体，
        并输入b为 cone时，可计算圆锥体体积！'''
        QMessageBox.information(self, 'help', info)

    def choose(self):
        if self.radioButton.isChecked() == True:
            return self.radioButton.text()
        elif self.radioButton_2.isChecked() == True:
            return self.radioButton_2.text()
        elif self.radioButton_3.isChecked() == True:
            return self.radioButton_3.text()
        elif self.radioButton_4.isChecked():
            return self.radioButton_4.text()
        elif self.radioButton_5.isChecked():
            return self.radioButton_5.text()
        elif self.radioButton_6.isChecked():
            return self.radioButton_6.text()

    def run(self):
        flag = self.choose()
        # print(flag)
        a = self.lineEdit.text()
        b = self.lineEdit_3.text()
        h = self.lineEdit_2.text()

        # print([a, b, h])
        if flag == '三角形形':
            if not b and a and h:
                area = 0.5*float(a)*float(h)
                # display result.
                self.lineEdit_14.setText(str(area))

        elif flag == '平行四边形':
            if not b and a and h:
                area = float(a)*float(h)
                # display result.
                self.lineEdit_14.setText(str(area))

        elif flag == '圆形':
            if not b and not h and a:
                area = 3.141*float(a)**2
                # display result.
                self.lineEdit_14.setText(str(area))

        elif flag == '长立方体':
            if a and b and h:
                area = float(a)*float(b)*float(h)
                # display result.
                self.lineEdit_14.setText(str(area))

        elif flag == '圆柱体':
            if not b and a and h:
                area = 3.141*float(a)**2*float(h)
                # display result.
                self.lineEdit_14.setText(str(area))
            elif b == 'cone' and a and h:
                area = (1/3)*3.141*float(a)**2*float(h)
                # display result.
                self.lineEdit_14.setText(str(area))

        elif flag == '球体':
            if not b and not h and a:
                area = (4/3)*3.141*float(a)**3
                # display result.
                self.lineEdit_14.setText(str(area))


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = Widget()

    win.show()

    sys.exit(app.exec_())

