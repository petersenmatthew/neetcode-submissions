class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        maxWealth = 0

        for i in range(len(accounts)):
            wealth = 0
            for x in range(len(accounts[i])):
                wealth += accounts[i][x]
            if wealth >= maxWealth:
                maxWealth = wealth

        return maxWealth
