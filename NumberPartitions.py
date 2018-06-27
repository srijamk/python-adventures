class NumberPartitions:
	def solve(self, num):
		dp = [[0 for x in range(num + 1)] for y in range(num + 1)]

		for i in range(len(dp[0])):
			dp[0][i] = 0
			dp[i][0] = 1		

		for row in range(len(dp)):
			for col in range(len(dp[0])):

				num_coins = col
				sub_sum = row
				
				if row != 0:
					dp[row][col] = dp[row - 1][col]
				if row != 0 and sub_sum <= num_coins:
					dp[row][col] += dp[row][num_coins - sub_sum]
		
		return dp[-1][-1]

N = NumberPartitions()
print(N.solve(4)) 
print(N.solve(5)) 

