from PySide2.QtCore import QObject


class BallController(QObject):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.models = {}
		self.views = {}
