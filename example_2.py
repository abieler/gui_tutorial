#!/usr/bin/env python
# Filename: example2.py

import sys import PyQt4.QtCore as QTC
import PyQt4.QtGui as QTG from numpy import *
import ui_example2

class Window(QTG.QWidget,ui_example2.Ui_Form):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.pushButton_load_data, QTC.SIGNAL("clicked()"),\
        self.load_data_clicked)

        self.connect(self.pushButton_refresh, QTC.SIGNAL("clicked()"),\
        self.refresh_clicked)

        self.connect(self.pushButton_save_plot, QTC.SIGNAL("clicked()"),\
        self.save_plot_clicked)


    def load_data_clicked(self):
        self.filename=str(QTG.QFileDialog.getOpenFileName\
        (filter='*.asc', caption="load data file"))
        delimiter_gui = str(self.lineEdit_delimiter.text())
        if delimiter_gui.lower() == 'tab':
            delimiter_gui = '\t' 		

        xcol = self.spinBox_xcol.value()
        ycol = self.spinBox_ycol.value() 	

        self.x, self.y = loadtxt(self.filename,delimiter=delimiter_gui,\
        usecols=(xcol,ycol), unpack=True)

        self.refresh_clicked() 	

    def refresh_clicked(self):
        xlabel = self.lineEdit_xlabel.text()
        ylabel = self.lineEdit_ylabel.text()
        logyaxis = self.checkBox_logaxis.isChecked() 	
        self.mpl_widget.canvas.ax.clear()
        if logyaxis:
            if min(self.y) == 0:
                y_nozeros = [element for element in self.y if element > 0]
                ylogaxis = []
                new_lowest = np.min(y_nozeros)/10
                for element in self.y:
                    if element == 0:
                        ylogaxis.append(new_lowest)
                    else:
                        ylogaxis.append(element)

                self.mpl_widget.canvas.ax.semilogy(self.x,ylogaxis,'-k')
            else:
                self.mpl_widget.canvas.ax.semilogy(self.x,self.y,'-k')
        else:
            self.mpl_widget.canvas.ax.plot(self.x,self.y,'-k') 		

        self.mpl_widget.canvas.ax.grid(True)
        self.mpl_widget.canvas.ax.set_xlabel(xlabel)
        self.mpl_widget.canvas.ax.set_ylabel(ylabel)
        self.mpl_widget.canvas.draw()

    def save_plot_clicked(self):
        self.mpl_widget.canvas.fig.savefig\
        ('/home/andre/Desktop/testfig.png') 	
	
app = QTG.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
