class UnboundedKnapsack:
	
	def arrange(self, weight_arr, value_arr):
		new_weight_arr = []
		new_value_arr = []
		for i in range(len(weight_arr)):
			new_value_arr.append(max(value_arr))
			new_weight_arr.append(weight_arr[value_arr.index(max(value_arr))])
			value_arr[value_arr.index(max(value_arr))] = min(value_arr) - 1
		return (new_weight_arr, new_value_arr)

	def solve(self, weight_arr, value_arr, weight_bound):
		dp = [[0 for x in range(len(weight_arr))] for y in range(weight_bound)]

		highest_value = 0
		
		new_arrs = self.arrange(weight_arr, value_arr)
		weight_arr = new_arrs[0]
		value_arr = new_arrs[1]

		for row in range(len(dp)):
			remainder = row + 1
			for col in range(len(dp[0])):

				if weight_arr[col] <= remainder:
					add = (remainder / weight_arr[col])

					if col == 0:
						dp[row][col] = add * value_arr[col]
					else:
						dp[row][col] = dp[row][col - 1] + add * value_arr[col]
					remainder -= add * weight_arr[col]
				elif col != 0:
					dp[row][col] = dp[row][col - 1]
				highest_value = max(highest_value, dp[row][col])

		return highest_value

U = UnboundedKnapsack()
print(U.solve([4, 12, 2, 1, 1], [10, 4, 2, 2, 1], 8))
