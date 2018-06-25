class LongestCommonSubstring:
	def longest_common_substring(self, s1, s2):
		dp = [[0 for x in range(len(s1))] for y in range(len(s2))]
		
		length = 0

		for row in range(len(dp)):
			for col in range(len(dp[0])):
				if s1[col] == s2[row]:
					if row == 0 or col == 0:
						dp[row][col] = 1
						length = max(length, 1)
					else:
						add = dp[row - 1][col - 1] + 1
						dp[row][col] = add
						length = max([length, add])
				
		return length

L = LongestCommonSubstring()
print(L.longest_common_substring("ABABC", "BABCA"))
