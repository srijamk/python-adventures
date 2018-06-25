class LongestIncreasingSubsequence:
	def longest_increasing_subsequence(self, arr):
		dp = [1 for x in range(len(arr))]
		
		length = 0

		j = 0
		i = 1
		
		while i < len(arr):
			if arr[j] < arr[i]:
				dp[i] = max(dp[j] + 1, dp[i])
				length = max(length, dp[i])
			if j == i:
				j = 0
				i += 1
			else:
				j += 1
		return length

L = LongestIncreasingSubsequence()
print(L.longest_increasing_subsequence([3, 4, -1, 0, 6, 2, 3]))

		
