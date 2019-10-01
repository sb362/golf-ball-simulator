from PySide2.QtCore import QObject, Signal

from ..models import Golfball, SimpleGolfball


class BallModel(QObject):
	changed = Signal(Golfball, Golfball)
	modified = Signal()

	def __init__(self, parent = None):
		super().__init__(parent)

		self.golfball = SimpleGolfball()

	def setGolfball(self, golfball: Golfball):
		old_golfball = self.golfball
		if old_golfball != golfball:
			self.golfball = golfball
			self.changed.emit(old_golfball, golfball)
			self.modified.emit()
