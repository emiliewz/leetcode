class Solution:
    # def valid(self, s, map):
    #     return True if s in map else False

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        n = len(s)
        a = [0] * (n+1)
        a[0] = a[1] = 1
        
        for i in range(2, n+1):
            if int(s[i-1]) != 0:
                a[i] = a[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                a[i] += a[i-2]
        
        return a[n]
        
        
        # Tabulation approach
        n = len(s)
        dp = [0] * (n + 1)
        # base case
        dp[n] = 1

        for i in range(n - 1, -1, -1):

            if s[i] != '0': # another base case

                dp[i] = dp[i + 1] # single digit

                # double digit
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                    dp[i] += dp[i + 2]
        
        return dp[0]


        # # Memoization approach
        # dp = {len(s): 1}
        # res = 0

        # def dfs(i):
        #     # base cases
        #     if i in dp:
        #         return dp[i]
            
        #     if s[i] == '0':
        #         return 0
        
        #     # if the input val not in dp, find it and store it in dp
        #     # single digit
        #     res = dfs(i + 1)

        #     # double digit
        #     if i + 1 < len(s) and ((s[i] == '1') or (s[i] == '2' and s[i + 1] in "0123456")):
        #         res += dfs(i + 2)
            
        #     # update the dp 
        #     dp[i] = res
        #     print(f"{i}: {res}")
        #     print(dp)
        #     return res

        # return dfs(0)


        # input: s = "1"
        # output: 1

        # input: s = "12"
        # output: 2

        # input: s = "123"
        # output: 3

        # input: s = "106"
        # output: 1

        # edge cases
        # input: s = "0"
        # output: 0

        # input: s = "09621"
        # output: 0

        # input: s = "90"
        # output: 0

        # map for 26 chars {num char: string char}
        # recursion 
        # first, chunking the string into different chars approaches
        # check if the chunked str are valid 
        #   increment the count
        
        # if there is only one char in the input --> return 1
        # [:1] and [1:] 
        # [:2] and [2:]
        # [:3] and [3:]
        # ...
        # check if the substring are valid
        # if the substring is in the map --> valid --> increment the count

        # map = defaultdict()
        # ascii_value = 65
        # count = 0

        # for i in range(1, 27):
            
        #     map[str(i)] = chr(ascii_value)
        #     ascii_value += 1
        # print(map)

        # # chunk the input str
        # for i in range(len(s)):
        #     # if self.valid(s[i], map):
        #     #     count += 1

        #     if self.valid(s[ :i + 1], map) and self.valid(s[i + 1:], map):
        #         count += 1

        # return count

