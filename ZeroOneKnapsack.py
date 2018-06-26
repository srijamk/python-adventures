class ZeroOneKnapsack:
	def solve(self, weight_arr, value_arr, weight_bound):
		dp = [[0 for x in range(len(weight_arr))] for y in range(weight_bound)]

		highest_value = 0
		
		for row in range(len(dp)):
			remainder = row + 1
			for col in range(len(dp[0])):
				if weight_arr[col] <= remainder:
					if col == 0:
						dp[row][col] = value_arr[col]
					else:
						dp[row][col] = dp[row][col - 1] + value_arr[col]
					remainder -= weight_arr[col]
				elif col != 0:
					dp[row][col] = dp[row][col - 1]
				highest_value = max(highest_value, dp[row][col])

		return highest_value

Z = ZeroOneKnapsack()
print(Z.solve([4, 12, 2, 1, 1], [10, 4, 2, 2, 1], 15))
