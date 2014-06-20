class B:
	def __init__(self):
		hope = "hope"
class A:
	def __init__(self):
		self.one = "one"
		b = B()
	def func(self):
		print self.one

a = A()
a.func()