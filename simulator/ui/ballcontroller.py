from functools import partial

from PySide2.QtCore import QObject, Signal

from .ballmodel import BallModel


class BallController(QObject):
	modelAdded = Signal(BallModel, str)
	modelRemoved = Signal(BallModel, str)
	modelModified = Signal(BallModel, str)

	def __init__(self, parent = None):
		super().__init__(parent)

		self.models = {}

		# ugly
		self._modelCallbacks = {}

	def addModel(self, model: BallModel, model_name: str):
		if self.containsModel(model_name):
			model_name = self._fixModelName(model_name)

		model.setParent(self)

		callback = partial(self.modelModified.emit, model, model_name)
		model.modified.connect(callback)
		self._modelCallbacks[model_name] = callback

		self.models[model_name] = model
		self.modelAdded.emit(model, model_name)

	def removeModel(self, model_name: str):
		model = self.models.pop(model_name, False)
		if model:
			self._modelCallbacks.pop(model_name, False)
			self.modelRemoved.emit(model, model_name)

		return model

	def containsModel(self, model_name: str):
		return model_name in self.models

	def clear(self):
		for model_name, model in self.models.items():
			self.modelRemoved.emit(model, model_name)

		self._modelCallbacks.clear()
		self.models.clear()

	def _fixModelName(self, model_name: str):
		i = 2
		old_model_name = model_name
		model_name += "(" + str(i) + ")"
		while self.containsModel(model_name):
			i += 1
			model_name = old_model_name + "(" + str(i) + ")"

		return model_name
