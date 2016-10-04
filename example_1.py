#!/usr/bin/env python
#Filename: example_1.py

import sys
import PyQt4.QtCore as QTC
import PyQt4.QtGui as QTG
import ui_example_1


class Window(QTG.QWidget,ui_example_1.Ui_Form):
	def __init__(self, parent = None): 		
		super(Window, self).__init__(parent) 		
		self.setupUi(self)

		self.connect(self.pushButton_start, QTC.SIGNAL("clicked()"), \
		self.myfunc)
	
	def myfunc(self):
		yourName = self.lineEdit_name.text()
		message = 'Hello,%s.' %yourName
		
		self.label_message.setText(message)
	
	
app = QTG.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
