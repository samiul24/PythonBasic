# Creating a decorator
class function_1:
	def __init__(self, func):
		self.func = func
		self.stats = []

	def __call__(self, *args, **kwargs):
		try:
			result = self.func(*args, **kwargs)
			print(*args)
		except Exception as e:
			self.stats.append((args, kwargs, e))
			raise e
		else:
			self.stats.append((args, kwargs, result))
			return result

	@classmethod
	def function_2(cls, func):
		print(cls)
		print(func)
		return cls(func)


def func(x, y):
    return x / y

fun=function_1.function_2(func)
print(fun(4,4))



