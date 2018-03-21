from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys
import calculator_interface
import calculate

class Calculator_Class(calculator_interface.Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super(Calculator_Class, self).__init__()
		self.setupUi(self)
		self.last_sender = None

		self.BUTTON_ZERO.clicked.connect(lambda: self.display_screen('0'))
		self.BUTTON_ONE.clicked.connect(lambda: self.display_screen('1'))
		self.BUTTON_TWO.clicked.connect(lambda: self.display_screen('2'))
		self.BUTTON_THREE.clicked.connect(lambda: self.display_screen('3'))
		self.BUTTON_FOUR.clicked.connect(lambda: self.display_screen('4'))
		self.BUTTON_FIVE.clicked.connect(lambda: self.display_screen('5'))
		self.BUTTON_SIX.clicked.connect(lambda: self.display_screen('6'))
		self.BUTTON_SEVEN.clicked.connect(lambda: self.display_screen('7'))
		self.BUTTON_EIGHT.clicked.connect(lambda: self.display_screen('8'))
		self.BUTTON_NINE.clicked.connect(lambda: self.display_screen('9'))
		self.BUTTON_PERIOD.clicked.connect(lambda: self.display_screen('.'))

		self.BUTTON_LPAR.clicked.connect(lambda: self.display_screen('('))
		self.BUTTON_RPAR.clicked.connect(lambda: self.display_screen(')'))

		self.BUTTON_MINUS.clicked.connect(lambda: self.display_screen('-'))
		self.BUTTON_PLUS.clicked.connect(lambda: self.display_screen('+'))
		self.BUTTON_DIV.clicked.connect(lambda: self.display_screen('/'))
		self.BUTTON_MULT.clicked.connect(lambda: self.display_screen('*'))

		self.BUTTON_A.clicked.connect(lambda: self.var_button('A'))
		self.BUTTON_B.clicked.connect(lambda: self.var_button('B'))
		self.BUTTON_C.clicked.connect(lambda: self.var_button('C'))

		self.BUTTON_BACK.clicked.connect(self.EDITOR_LINE.backspace)
		self.BUTTON_CLEAR.clicked.connect(self.EDITOR_LINE.clear)

		self.BUTTON_ENTER.clicked.connect(self.calculation)

		self.BUTTON_STORE.clicked.connect(self.store_start)

	def var_button(self, name):
		if self.last_sender == 'BUTTON_STORE':
			screen_value = self.EDITOR_LINE.text()
			value = float(screen_value)
			calculate.variables[name] = value
			print(calculate.variables)
			self.last_sender = None
		else:
			self.display_screen(name)

	def store_start(self):
		screen_value = self.EDITOR_LINE.text()
		last_sender = self.sender()
		self.last_sender = last_sender.objectName()
		try:
			value = float(screen_value)
		except ValueError:
			self.EDITOR_LINE.clear()
			self.display_screen("error")


	def display_screen(self, value):
		self.EDITOR_LINE.insert(value)

		self.last_sender = None

	def calculation(self):
		screen_value = self.EDITOR_LINE.text()
		print(screen_value)
		result = calculate.main_calc(screen_value)
		print(result)
		self.update_screen(result)
		self.last_sender = None


	def update_screen(self, result):
		self.EDITOR_LINE.clear()
		self.display_screen(str(result))

		self.last_sender = None

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	calc = Calculator_Class()
	calc.show()
	sys.exit(app.exec_())