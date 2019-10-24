from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QStyle


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
