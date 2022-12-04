#%% Imports
import sys, os, time
import json
import ftplib
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.QtWidgets
print(PyQt5.QtWidgets.QStyleFactory.keys())
#%% Load Forms
TSW_Form = uic.loadUiType(os.path.join(os.getcwd(), 'UI','Time_Save_Window.ui'))[0]
#%% Initiations
CONF_DIC: dict
with open(os.path.join("CONF", "CONF.json"), mode='r') as conf_file:
    CONF_DIC = json.loads(conf_file.read(-1))

REC_FILE_PATH = os.path.join(*CONF_DIC["LOCAL_SAVING_PATH"])

# FTP_SERVER = ftplib.FTP(**CONF_DIC["FTP"])
# FTP_SERVER.encoding= "utf-8"

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

        self.data_dic: dict
        self._data_loaded_flg = False

        self.pushButton_Load.clicked.connect(self.load_data)       

        self.get_time_but_start.clicked.connect(self.get_time_start)
        self.get_time_but_stop.clicked.connect(self.get_time_stop)
        
        self.set_but_start.clicked.connect(self.set_start)
        self.set_but_stop.clicked.connect(self.set_stop)

        self.reset_but_start.clicked.connect(self.reset_start)
        self.reset_but_stop.clicked.connect(self.reset_stop)

        self.save_but.clicked.connect(self.save_file)
        self.reset_but.clicked.connect(self.reset_all)
        self.save_but.setEnabled(False)

    def load_data(self):
        self.progressBar_Save.setValue(0)
        self._load_from_ftp()
        self.progressBar_Save.setValue(50)
        self._load_from_local()

        self._data_loaded_flg = True        
        self.save_but.setEnabled(True)
        self.checkBox_LoadFromFTP.setEnabled(False)
        self.pushButton_Load.setEnabled(False)
        self.progressBar_Save.setValue(100)

    def _load_from_ftp(self):
        """
            Overwrites the local file if the load from FTP checkbox is checked
        """
        self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
        if self.checkBox_LoadFromFTP.isChecked():
            with ftplib.FTP(**CONF_DIC["FTP"], encoding= 'utf-8') as ftp_server:
                self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
                # Load the record file from FTP if it exists
                tmp_ftp_nlst = []
                ftp_server.retrlines("NLST", tmp_ftp_nlst.append)
                self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

                if F"{CONF_DIC['FTP_SAVING_PATH']}" in tmp_ftp_nlst:
                    self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
                    with open(REC_FILE_PATH, mode='wb') as rec_file:
                        self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
                        ftp_server.retrbinary(F"RETR {CONF_DIC['FTP_SAVING_PATH']}", rec_file.write)
                        self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

    def _load_from_local(self):
        # Check if the file exists
        tmp_dic:dict
        if os.path.isfile(REC_FILE_PATH):
            self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
            # Just reads the file
            with open(REC_FILE_PATH, mode= 'r') as rec_file:
                tmp_dic = json.loads(rec_file.read(-1))
                self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
        else:
            # Create a new file
            with open(REC_FILE_PATH, mode= 'x') as rec_file:
                # put an empty dictionary in the file
                rec_file.write(json.dumps({}))
                self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
                tmp_dic = {}
        
        # Check if all labels were in the record file
        for expected_key in CONF_DIC["LABELS"]:
            if not(expected_key in list(tmp_dic.keys())):
                # add the missing labels to the dictionary
                tmp_dic.update({expected_key:[]})
        self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

        # initiate the data dictionary
        self.data_dic = tmp_dic.copy()
        self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

        # Verify the combo box labels are the same as the CONF json file
        for expected_key in CONF_DIC["LABELS"]:
            assert self.comboBox_Label.findText(expected_key) >= 0, "Combo Box's labels don't match the CONF.json file"
        self.progressBar_Save.setValue(self.progressBar_Save.value()+5)


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
        tmp_label:str = self.comboBox_Label.currentText()

        if (self.start_time == None) or (self.stop_time == None):
            self.save_but.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.total_time = time.mktime(time.strptime(self.stop_time))\
                            - time.mktime(time.strptime(self.start_time))
            
            if self.total_time < 0:
                self.save_but.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.save_but.setEnabled(False)
                self.comboBox_Label.setEnabled(False)
                self.checkBox_SaveToFTP.setEnabled(False)


                self.data_dic[tmp_label].append({
                    "START"     : self.start_time,
                    "STOP"      : self.stop_time,
                    "TOTAL"     : self.total_time,
                    "Details"   : repr(self.textEdit_details.toPlainText())
                })

                self.progressBar_Save.setValue(0)

                with open(REC_FILE_PATH, mode='w') as rec_file:
                    rec_file.write(json.dumps(self.data_dic))                
                self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
                
                if self.checkBox_SaveToFTP.isChecked():
                    with ftplib.FTP(**CONF_DIC["FTP"], encoding= 'utf-8') as ftp_server:
                        self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

                        with open("FTP_BACKUP", mode='wb') as ftp_bk_file:
                            self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

                            # Get the file on FTP server
                            ftp_server.retrbinary(F"RETR {CONF_DIC['FTP_SAVING_PATH']}", ftp_bk_file.write)
                            self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

                            # Delete the backup file on FTP if it exists
                            tmp_ftp_nlst = []
                            ftp_server.retrlines("NLST", tmp_ftp_nlst.append)
                            self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

                            if F"{CONF_DIC['FTP_SAVING_PATH']}_BK" in tmp_ftp_nlst:
                                ftp_server.delete(F"{CONF_DIC['FTP_SAVING_PATH']}_BK")
                                self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

                        # Save the new backup file on FTP server
                        with open("FTP_BACKUP", mode='rb') as ftp_bk_file:
                            ftp_server.storbinary(F"STOR {CONF_DIC['FTP_SAVING_PATH']}_BK", ftp_bk_file)
                            self.progressBar_Save.setValue(self.progressBar_Save.value()+5)
                            
                        with open(REC_FILE_PATH, mode= 'rb') as rec_file:
                            self.progressBar_Save.setValue(self.progressBar_Save.value()+5)

                            # Write the new record file on the FTP server
                            ftp_server.storbinary(F"STOR {CONF_DIC['FTP_SAVING_PATH']}", rec_file)
                            self.progressBar_Save.setValue(self.progressBar_Save.value()+5)


                self.save_but.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.progressBar_Save.setValue(100)

    def reset_all(self):
        self.reset_start()
        self.reset_stop()
        self.textEdit_details.setText("")
        self.progressBar_Save.setValue(0)

        self.comboBox_Label.setEnabled(True)
        self.checkBox_SaveToFTP.setEnabled(True)
        self.save_but.setStyleSheet("")
        if self._data_loaded_flg:
            self.save_but.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyle('Fusion')

    ts_window = TSW()
    ts_window.show()


    #sys.exit(app.exec_())
    
    app.exec_()
    print('this was the end!')

# %%
