import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class CrossRailCalc(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		btn = QPushButton('Button', self)
		btn.move(50, 50)

		le = QLineEdit(self)

		gb = QGroupBox('Alloys')

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(le)

		gb.setLayout(vbox)

		self.setGeometry(300, 150, 800, 600)
		self.setWindowTitle('CrossRailCalc')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	crc = CrossRailCalc()
	sys.exit(app.exec_())
