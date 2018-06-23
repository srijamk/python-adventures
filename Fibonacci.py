class Fibonacci:
	def __init__(self):
		self.fib = [1, 1]
	
	def get_num(self, n):
		for i in range(0, n):
			self.fib.append(self.fib[-2] + self.fib[-1])
		return self.fib[n - 1]

F = Fibonacci()
print(F.get_num(9))
