from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout, QLineEdit
)
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.setWindowTitle("Definition of BMI")
window.resize(459,213)

weight = QLabel("Body weight:")
height = QLabel("Body height:")
result = QLabel("Your BMI = ")
button = QPushButton("Find out your BMI")
button2 = QPushButton("What does it mean")
wrt_weight = QLineEdit()
wrt_height = QLineEdit()

def equaling():
   weight_num = int(wrt_weight.text())
   height_num = int(wrt_height.text())
   equal = weight_num / ((height_num / 100) ** 2)
   equal = round(equal)
   return str(equal)

def cal_bmi():
   result1 = equaling()
   result.setText("Your BMI = " + result1)

button.clicked.connect(cal_bmi)

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

main_layout = QVBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()
col4 = QVBoxLayout()
col5 = QVBoxLayout()

col1.addWidget(weight)
col2.addWidget(wrt_weight)
col3.addWidget(height)
col5.addWidget(wrt_height)
col4.addWidget(button)
col4.addWidget(result)
col4.addWidget(button2)

row1.addLayout(col1)
row1.addLayout(col2)
row2.addLayout(col3)
row2.addLayout(col5)
row3.addLayout(col4)
row3.addLayout(col4)

main_layout.addLayout(row1)
main_layout.addLayout(row2)
main_layout.addLayout(row3)
window.setLayout(main_layout)

window.show()
app.exec_()