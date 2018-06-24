class LevenshteinDistance:
	def dist(self, s1, s2):
		dp = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)] 

		for i in range(0, len(dp)):
			dp[0][i] = i

		for j in range(0, len(dp)):
			dp[j][0] = j

		for row in range(1, len(dp)):
			for col in range(1, len(dp[0])):
				min_dist = min([dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]])

				if s1[row - 1] == s2[col - 1]:
					dp[row][col] = min_dist
				else:
					dp[row][col] = min_dist + 1

		return dp[-1][-1]
L = LevenshteinDistance()
print(L.dist("kitten", "sitting"))
