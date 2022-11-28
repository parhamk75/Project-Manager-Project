#%% Imports
import sys, os, time
import json
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.QtWidgets
print(PyQt5.QtWidgets.QStyleFactory.keys())

#%% Load Forms
TSW_Form = uic.loadUiType(os.path.join(os.getcwd(), 'UI','Time_Save_Window.ui'))[0]

#%% GUI Classes
#%% Time Save Window
class TSW(TSW_Form, QMainWindow):
    def __init__(self):
        TSW_Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.start_time = None
        self.stop_time = None

        self.total_time = None
        

        self.get_time_but_start.clicked.connect(self.get_time_start)
        self.get_time_but_stop.clicked.connect(self.get_time_stop)
        
        self.set_but_start.clicked.connect(self.set_start)
        self.set_but_stop.clicked.connect(self.set_stop)

        self.reset_but_start.clicked.connect(self.reset_start)
        self.reset_but_stop.clicked.connect(self.reset_stop)

        self.save_but.clicked.connect(self.save_file)
        self.reset_but.clicked.connect(self.reset_all)


    def get_time_start(self):        
        self.lineEdit_start.setText(time.ctime())        

    def get_time_stop(self):
        self.lineEdit_stop.setText(time.ctime())

    def set_start(self):
        if self.lineEdit_start.text() != '':
            self.start_time = self.lineEdit_start.text()

            self.set_but_start.setEnabled(False)
            self.lineEdit_start.setEnabled(False)
            self.get_time_but_start.setEnabled(False)
            self.set_but_start.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.set_but_start.setStyleSheet("background-color: rgb(255, 0, 0);")

    def set_stop(self):
        if  self.lineEdit_stop.text() != '':
            self.stop_time = self.lineEdit_stop.text()

            self.set_but_stop.setEnabled(False)
            self.lineEdit_stop.setEnabled(False)
            self.get_time_but_stop.setEnabled(False)
            self.set_but_stop.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.set_but_stop.setStyleSheet("background-color: rgb(255, 0, 0);")
            

    def reset_start(self):
        self.start_time = None
        self.lineEdit_start.clear()

        self.set_but_start.setEnabled(True)
        self.lineEdit_start.setEnabled(True)
        self.get_time_but_start.setEnabled(True)
        self.set_but_start.setStyleSheet("")
        
    def reset_stop(self):
        self.stop_time = None
        self.lineEdit_stop.clear()

        self.set_but_stop.setEnabled(True)
        self.lineEdit_stop.setEnabled(True)
        self.get_time_but_stop.setEnabled(True)
        self.set_but_stop.setStyleSheet("")

    def save_file(self):        
        tmp_prj:str = self.comboBox_Project.currentText()

        if (self.start_time == None) or (self.stop_time == None):
            self.save_but.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.total_time = time.mktime(time.strptime(self.stop_time))\
                            - time.mktime(time.strptime(self.start_time))
            
            if self.total_time < 0:
                self.save_but.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.save_but.setEnabled(False)

                with open(F'{tmp_prj}_LOG.txt', 'a') as log_file:
                    log_file.write('TOTAL => {:^15} | START => {} | STOP => {} | Details => {}\n'.format\
                                        (self.total_time, self.start_time, self.stop_time, repr(self.textEdit_details.toPlainText())))

                self.save_but.setStyleSheet("background-color: rgb(0, 255, 0);")

    def reset_all(self):
        self.reset_start()
        self.reset_stop()
        self.textEdit_details.setText("")

        self.save_but.setEnabled(True)
        self.save_but.setStyleSheet("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyle('Fusion')

    ts_window = TSW()
    ts_window.show()


    #sys.exit(app.exec_())
    
    app.exec_()
    print('this was the end!')

# %%
