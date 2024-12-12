from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

from .ui_warningwindow import Ui_WarningWindow

class WarningWindow(QtWidgets.QMainWindow, Ui_WarningWindow):
    def __init__(self, message: str):
        super().__init__()
        self.setupUi(self)
        
        self.label_warning.setText(message)
        self.button_ok.clicked.connect(self.close)