import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QLineEdit,QCheckBox
from PyQt5.QtWidgets import  QAction,qApp,QMainWindow
from PyQt5 import QtGui



class Exchance(QWidget):

    def __init__(self):
        super(). __init__()
        self.init_ui()



    def init_ui(self):

        self.intro = QLabel("Enter Value")
        self.writing_area = QLineEdit()
        self.output = QLabel("")
        self.checkbox1 = QCheckBox("EURO TO TURK LIRA")
        self.checkbox2= QCheckBox("TURK LIRA TO EURO")
        self.checkbox3 = QCheckBox("DOLAR TO TURK LİRA")
        self.checkbox4 = QCheckBox("TURK LIRA TO DOLAR")
        self.checkbox5 = QCheckBox("EURO TO DOLAR")
        self.checkbox6 = QCheckBox("DOLAR TO EURO")
        self.ok = QPushButton("Okay")
        self.clear = QPushButton("Delete")
        self.pic = QLabel("")
        self.pic.setPixmap(QtGui.QPixmap("döviz.jpg"))



        h_box = QHBoxLayout()
        h_box.addWidget(self.ok)
        h_box.addWidget(self.clear)
        h_box.addWidget(self.pic)

        v_box = QVBoxLayout()
        v_box.addWidget(self.intro)
        v_box.addWidget(self.writing_area)
        v_box.addWidget(self.output)
        v_box.addWidget(self.checkbox1)
        v_box.addWidget(self.checkbox2)
        v_box.addWidget(self.checkbox3)
        v_box.addWidget(self.checkbox4)
        v_box.addWidget(self.checkbox5)
        v_box.addWidget(self.checkbox6)
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("EXCHANGE PROGRAM")
        self.clear.clicked.connect(self.delete)
        self.ok.clicked.connect(lambda : self.okay(self.checkbox1.isChecked(),self.checkbox2.isChecked(),self.checkbox3.isChecked(),self.checkbox4.isChecked(),self.checkbox5.isChecked(),self.checkbox6.isChecked(),self.output))
        self.show()

    def delete(self):
        self.writing_area.clear()


    def okay(self,checkbox1,checkbox2,checkbox3,checkbox4,checkbox5,checkbox6,output):
        url = "https://www.doviz.com/"
        respons = requests.get(url)
        html_içeriği = respons.content
        soup = BeautifulSoup(html_içeriği, "html.parser")

        borsa_turleri = []
        borsa_degerleri = []

        for a in soup.find_all("span", {"class": "name"}):
            borsa_turleri.append(a.text)

        for b in soup.find_all("span", {"class": "value"}):
            borsa_degerleri.append((b.text).replace(",", "."))

        if checkbox1 :

            quantity = self.writing_area.text()
            quantity = float(quantity)
            result = str(quantity * float(borsa_degerleri[2]))
            output.setText(result)
        if checkbox2:
            quantity = self.writing_area.text()
            quantity = float(quantity)
            result = str(quantity / float(borsa_degerleri[2]))
            output.setText(result)
        if checkbox3:
            quantity = self.writing_area.text()
            quantity = float(quantity)
            result = str(quantity * float(borsa_degerleri[1]))
            output.setText(result)
        if checkbox4:
            quantity = self.writing_area.text()
            quantity = float(quantity)
            result = str(quantity / float(borsa_degerleri[1]))
            output.setText(result)
        if checkbox5:
            quantity = self.writing_area.text()
            quantity = float(quantity)
            result = str((float(borsa_degerleri[2]) / float(borsa_degerleri[1])) * quantity)
            output.setText(result)
        if checkbox6:
            quantity = self.writing_area.text()
            quantity =  float(quantity)
            result =str((float(borsa_degerleri[1]) / float(borsa_degerleri[2])) / quantity)
            output.setText(result)





class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ek = Exchance()
        self.setCentralWidget(self.ek)

        self.create_menu()


    def create_menu(self):
        menubar = self.menuBar()

        file = menubar.addMenu(" OPTIONS MENU")
        menubar.setNativeMenuBar(False)

        exit = QAction("Exit",self)
        file.addAction(exit)

        file.triggered.connect(self.response)

        self.show()

    def response (self,action):
        if action.text() == "Exit":
            qApp.quit()




app = QApplication(sys.argv)

menu =Menu()
sys.exit(app.exec_())







