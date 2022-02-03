from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate
Form, Window = uic.loadUiType("maker.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def on_click():
    print(form.textEdit.toPlainText())
    

form.btn.clicked.connect(on_click)


#form.label.setText('asdasdsa')


app.exec_()