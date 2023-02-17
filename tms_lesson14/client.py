from PyQt5 import QtWidgets, QtCore, uic
import os
import socket
import json


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent)
        uic.loadUi("MyForm.ui", self)
        self.button_add.clicked.connect(self.add_user)
        self.button_update.clicked.connect(self.update_user)
        self.button_delete.clicked.connect(self.delete_user)
        
    
    def add_user(self):
        print(1)
    
    
    def update_user(self):
        print(2)
    
    
    def delete_user(self):
        print(3)


class Client(object):
    def __init__(self) -> None:
        self.sock = socket.socket()
        self.sock.connect(('localhost', 8080))
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # client = Client()
    window = MainWindow()
    window.show()
    app.exec()