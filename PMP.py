#%% Imports
import sys, os, time
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

#%% Load Forms
TSW_Form = uic.loadUiType(os.path.join(os.getcwd(), 'Time_Save_Window.ui'))[0]

#%% GUI Classes
#%% Time Save Window
class TSW(TSW_Form, QMainWindow):
    def __init__(self):
        TSW_Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.get_time_but_start.clicked.connect(self.get_time_start)
        self.get_time_but_stop.clicked.connect(self.get_time_stop)

    def get_time_start(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ts_window = TSW()
    ts_window.show()


    sys.exit(app.exec_())