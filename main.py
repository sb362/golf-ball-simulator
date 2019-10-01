#!/usr/bin/env python3
import sys

from PySide2.QtWidgets import QApplication

from simulator.ui import MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)

	app.setApplicationName("GolfBallSimulator")
	app.setApplicationDisplayName("Golf Ball Simulator")
	app.setApplicationVersion("2019-09-30")

	main_window = MainWindow()
	main_window.show()

	sys.exit(app.exec_())
