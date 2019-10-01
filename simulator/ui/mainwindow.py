from PySide2.QtCore import QSize, Qt, qApp
from PySide2.QtWidgets import QMainWindow, QStyle, QAction, QMessageBox, QPushButton, QDockWidget, QInputDialog, \
	QLineEdit

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np

from .ballmodel import BallModel
from .ballcontroller import BallController


def centralisedRect(geometry, x_scale: float = 0.65, y_scale: float = 0.65):
	size = geometry.size()

	return QStyle.alignedRect(
		Qt.LeftToRight,
		Qt.AlignCenter,
		QSize(
			size.width() * x_scale,
			size.height() * y_scale,
		),
		geometry
	)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.modelMenu = None
		self.viewMenu = None
		self.aboutMenu = None
		self.populateMenuBar()

		self.figure = Figure()
		self.canvas = FigureCanvas(self.figure)
		self.setCentralWidget(self.canvas)

		self.navToolBar = NavigationToolbar(self.canvas, self)
		self.addToolBar(Qt.BottomToolBarArea, self.navToolBar)

		self.axes = self.figure.add_subplot(111)
		self.axes.grid(True)
		self.axes.set_title("Ballistic trajectory")
		self.axes.set_xlabel("Horizontal position (m)")
		self.axes.set_ylabel("Height (m)")

		self.lineFromName = {}

		self.ballController = BallController(self)
		self.ballController.modelAdded.connect(self.onModelAdded)
		self.ballController.modelRemoved.connect(self.onModelRemoved)
		self.ballController.modelModified.connect(self.onModelModified)

		self.setGeometry(centralisedRect(qApp.desktop().availableGeometry()))
		self.setWindowTitle("Golf Ball Simulator")

	def newBall(self, model_name: str = None):
		ok = True
		if not model_name:
			model_name, ok = QInputDialog.getText(self, "Enter model name", "Model name", QLineEdit.Normal, "Ball")

		if ok:
			self.ballController.addModel(BallModel(), model_name)

	def clearAllBalls(self):
		self.ballController.clear()
		self.refreshPlot()

	def onModelAdded(self, model: BallModel, model_name: str):
		x = np.linspace(0, 2 * np.pi)
		y = np.tanh(x)
		line = self.axes.plot(x, y, label = model_name)
		self.lineFromName[model_name] = line

		self.refreshPlot()

	def onModelRemoved(self, model: BallModel, model_name: str):
		self.lineFromName.pop(model_name, False)
		for i, line in enumerate(self.axes.lines):
			if line.get_label() == model_name:
				self.axes.lines.remove(line)
				break

		self.refreshPlot()

	def onModelModified(self, model: BallModel, model_name: str):
		line = self.lineFromName[model_name]

		x = np.linspace(0, 2 * np.pi)
		y = np.tanh(x)

		line.set_xdata(x)
		line.set_ydata(y)

		self.refreshPlot()

	def refreshPlot(self):
		self.axes.legend()
		self.canvas.draw()

	def populateMenuBar(self):
		self.createMenuBarModelMenu()
		self.createMenuBarViewMenu()
		self.createMenuBarAboutMenu()

	def createMenuBarModelMenu(self):
		self.modelMenu = self.menuBar().addMenu("&Model")

		new_ball_action = QAction("New ball", self.modelMenu)
		new_ball_action.setStatusTip("Create a new ball")
		new_ball_action.triggered.connect(self.newBall)
		self.modelMenu.addAction(new_ball_action)

		clear_all_balls_action = QAction("Clear all balls", self.modelMenu)
		clear_all_balls_action.setStatusTip("Remove all existing balls")
		clear_all_balls_action.triggered.connect(self.clearAllBalls)
		self.modelMenu.addAction(clear_all_balls_action)

		self.modelMenu.addSeparator()

		quit_action = QAction("Quit", self.modelMenu)
		quit_action.setStatusTip("Quit")
		quit_action.triggered.connect(self.close)
		self.modelMenu.addAction(quit_action)

	def createMenuBarViewMenu(self):
		self.viewMenu = self.menuBar().addMenu("&View")

	def createMenuBarAboutMenu(self):
		self.aboutMenu = self.menuBar().addMenu("&About")

		about_action = QAction("&About", self.aboutMenu)
		about_action.setStatusTip("Show about box")
		about_action.triggered.connect(self.showAboutBox)
		self.aboutMenu.addAction(about_action)

		about_qt_action = QAction("&About Qt", self.aboutMenu)
		about_qt_action.setStatusTip("Show Qt for Python's about box")
		about_qt_action.triggered.connect(qApp.aboutQt)
		self.aboutMenu.addAction(about_qt_action)

	def showAboutBox(self):
		QMessageBox.about(self, "About", f"Copyright (c) 2019 Stuart Ballantyne\nLast updated: {qApp.applicationVersion()}")
