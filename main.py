
import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, uic
from finance import Ui_MainWindow
from termcolor import colored
import time
import mysql.connector


class financas(QMainWindow):
    def __init__(self):
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.ui.pushButton.clicked.connect(self.adicionar)
      self.valor_entrou = 0
      self.valor_total = 0
      self.valor_saiu = 0
      self.linha = 0
      self.apagar()
      self.connect()

    def timer(self):
        tempo = threading.Timer(5, self.apagar())
        tempo.start()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host='localhost', database='sistema', user='root', password='1')
        except:
            self.ui.frame_error.show()

            self.ui.label_error.setText("Erro ao conectar no Banco de dados")
            self.timer()







            '''if con.is_connected():
                db_info = con.get_server_info()
                print("Conectado ao servidor MySQL versão ", db_info)
                cursor = con.cursor()
                cursor.execute("select database();")
                linha = cursor.fetchone()
                print("Conectado ao banco de dados ", linha)
            if con.is_connected():
                cursor.close()
                con.close()
                print("Conexão ao MySQL foi Finalizada")'''


    def apagar(self):
        self.ui.frame_error.hide()
        
    def adicionar(self):
        self.descricao = self.ui.lineEdit.text()
        self.valor = self.ui.lineEdit_2.text()
        
        if  self.descricao == "" or self.valor == "":
            self.ui.frame_error.show()
            self.ui.label_error.setText("Erro! Campo(s) vazios(s)") 
            
        elif not self.valor.isnumeric():    
            self.ui.frame_error.show()
            self.ui.label_error.setText("Erro! Somente numero(s)") 
        else:
            self.apagar()
    
            if self.ui.radioButton.isChecked():

                self.valor_entrou = float(self.valor_entrou) + float(self.valor)
                self.valor_total = float(self.valor_total) + float(self.valor)

                self.ui.label_7.setText(f'R$ {self.valor_entrou:>.2f}'.replace('.', ','))
                self.ui.label_9.setText(f'R$ {self.valor_total:>.2f}'.replace('.', ','))
                self.ui.lineEdit.setText("")
                self.ui.lineEdit_2.setText("")

                self.tipo = 'Entrada '

            if self.ui.radioButton_2.isChecked():

                self.valor_saiu = float(self.valor_saiu) + float(self.valor)
                self.valor_total = float(self.valor_total) - float(self.valor)

                self.ui.label_8.setText(f'R$ {self.valor_saiu:>.2f}'.replace('.', ','))
                self.ui.label_9.setText(f'R$ {self.valor_total:>.2f}'.replace('.', ','))

                self.tipo = 'Saída'

            self.ui.tableWidget.setRowCount(self.linha+1)
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setItem(self.linha,0,QtWidgets.QTableWidgetItem(f'{self.descricao}'))
            self.ui.tableWidget.setItem(self.linha,1,QtWidgets.QTableWidgetItem(f' R$ {float(self.valor):>.2f}'.replace('.', ',')))
            self.ui.tableWidget.setItem(self.linha,2,QtWidgets.QTableWidgetItem(f'{self.tipo}'))

            self.linha = self.linha + 1


if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = financas()
    w.show()
    sys.exit(app.exec_())