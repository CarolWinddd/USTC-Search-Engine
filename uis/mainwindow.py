import os
import sys
import json
from typing import Tuple, List

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

from .ui_mainwindow import Ui_MainWindow
from .warningwindow import WarningWindow

sys.path.append(os.path.dirname(__file__)+'/..')
from utils.hbase import HbaseConnection
from utils.docs import bytes_to_doc

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # GUI initializations
        self.item_model = QtGui.QStandardItemModel()
        self.list_result.setModel(self.item_model)
        self.list_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_result.resizeColumnsToContents()
            
        # buttons connection
        self.button_search.clicked.connect(self.button_search_clicked)
        self.list_result.clicked.connect(self.open_result)
        
        # hbase initialization
        with open('config.json', 'r') as f:
            self.config = json.load(f)
        self.hbase_connection = HbaseConnection(self.config['hbase_host'])
    
    def button_search_clicked(self):
        if query := self.input_search.text():
            print(f'Searching for: {query}')
            columns = [b'info:name', b'info:college']
            result = self.hbase_connection.search_ambigous(self.config['table_name'], columns, query)
            # result = [('test.txt', 'SDS', b'1234321')]    # test data
            self.show_results(result)
        else:
            self.create_warning('Please input file name!')
    
    def show_results(self, result: List[Tuple[str]]):
        self.item_model.clear()
        self.item_model.setHorizontalHeaderLabels(['Index', 'Document Name', 'College'])
        self.list_result.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        if result:
            for i, (key, name, college, data) in enumerate(result):
                index_item = QtGui.QStandardItem(str(i+1))
                name_item = QtGui.QStandardItem(name)
                name_item.setForeground(QtGui.QColor('blue'))
                name_item.setData(data, QtCore.Qt.UserRole+1)
                college_item = QtGui.QStandardItem(college)
                self.item_model.appendRow([index_item, name_item, college_item])
        else:
            pass
            
    def open_result(self, index):
        item = self.item_model.item(index.row(), 1)
        data = item.data(QtCore.Qt.UserRole+1)
        name = item.text()
        
        output_dir = self.config['output_dir']
        bytes_to_doc(data, name, output_dir)
        
        url = QtCore.QUrl.fromLocalFile(f'{output_dir}/{name}')
        QtGui.QDesktopServices.openUrl(url)
    
    def create_warning(self, message: str):
        self.warning = WarningWindow(message)
        self.warning.setWindowModality(Qt.ApplicationModal)
        self.warning.show()
    
    def closeEvent(self, event):
        self.hbase_connection.close()
        event.accept()