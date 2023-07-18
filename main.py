#region Импортирование
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import randint
#endregion


#region Создание приложение и окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Испытай удачу, друг!')
window.resize(500,500)
window.move(0,0)
#endregion


#region Создание виджетов
button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')
winner = QLabel('Поздравляю ты выйграл!')
#endregion


#region Размещение виджетов
line0 = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line1.addWidget(button1,alignment = Qt.AlignLeft)
line1.addWidget(button2,alignment = Qt.AlignRight)
line3.addWidget(button3,alignment = Qt.AlignCenter)
line2.addWidget(button4,alignment = Qt.AlignLeft)
line2.addWidget(button5,alignment = Qt.AlignRight)
line0.addLayout(line1)
line0.addLayout(line3)
line0.addLayout(line2)
window.setLayout(line0)
#endregion


#region Запуск приложения
window.show()
app.exec_()
#endregion