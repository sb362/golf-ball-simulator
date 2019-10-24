from PySide2.QtCore import QObject


class BallModel(QObject):
	def __init__(self, parent = None):
		super().__init__(parent)
