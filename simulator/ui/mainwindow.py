from PySide2.QtCore import qApp
from PySide2.QtWidgets import QMainWindow, QMessageBox

from .util import centralisedRect

from .ballcontroller import BallController


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ballController = BallController(self)

		self.setGeometry(centralisedRect(qApp.desktop().availableGeometry()))
		self.setWindowTitle(qApp.applicationDisplayName())

	def showAboutQtBox(self):
		QMessageBox.aboutQt(self, "About Qt")

	def showAboutBox(self):
		QMessageBox.about(self, "About", f"Copyright (c) 2019 Stuart Ballantyne\nLast updated: {qApp.applicationVersion()}")
