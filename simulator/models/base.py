
all_models = {}

class Golfball:
	def __init__(self):
		pass

	def __init_subclass__(cls, **kwargs):
		super().__init_subclass__(**kwargs)
		all_models[cls.__name__] = cls
