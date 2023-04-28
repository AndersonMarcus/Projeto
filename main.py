
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, uic
from finance import Ui_MainWindow
from termcolor import colored


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

    def adicionar(self):

        self.descricao = self.ui.lineEdit.text()
        self.valor = self.ui.lineEdit_2.text()

        if self.ui.radioButton.isChecked():

            self.valor_entrou = int(self.valor_entrou) + int(self.valor)
            self.valor_total = int(self.valor_total) + int(self.valor)

            self.ui.label_7.setText(f'R$ {self.valor_entrou:>1.2f}'.replace('.', ','))
            self.ui.label_9.setText(f'R$ {self.valor_total:>1.2f}'.replace('.', ','))
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")

            self.tipo = 'Entrada '

        if self.ui.radioButton_2.isChecked():

            self.valor_saiu = float(self.valor_saiu) + float(self.valor)
            self.valor_total = float(self.valor_total) - float(self.valor)

            self.ui.label_8.setText(f'R$ {self.valor_saiu:.3f}')
            self.ui.label_9.setText(f'R$ {self.valor_total:.3f}')

            self.tipo = 'Saída'

        self.ui.tableWidget.setRowCount(self.linha+1)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setItem(self.linha,0,QtWidgets.QTableWidgetItem(f'{self.descricao}'))
        self.ui.tableWidget.setItem(self.linha,1,QtWidgets.QTableWidgetItem(f'{self.valor}'))
        self.ui.tableWidget.setItem(self.linha,2,QtWidgets.QTableWidgetItem(f'{self.tipo}'))

        self.linha = self.linha + 1


if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = financas()
    w.show()
    sys.exit(app.exec_())