class LongestCommonSubsequence:
	
	def longest_common_subsequence(self, s1, s2):
		dp = [[0 for x in range(len(s1))] for y in range(len(s2))]
		
		for row in range(0, len(dp)):
			for col in range(0, len(dp[0])):
				if s1[col] == s2[row]:
					if row == 0:
						dp[row][col] = 1
					else:
						dp[row][col] = dp[row - 1][col] + 1
				else:
					if row == 0 and col == 0:
						dp[row][col] = 0
					elif row == 0:
						dp[row][col] = dp[row][col - 1]
					elif col == 0:
						dp[row][col] = dp[row - 1][col]
					else:
						dp[row][col] = max([dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]])
		return dp[-1][-1]

L = LongestCommonSubsequence()
print(L.longest_common_subsequence("abcdaf", "acbcf")) #4
print(L.longest_common_subsequence("AGGTAB", "GXTXAYB")) #4
print(L.longest_common_subsequence("me", "my")) #1
