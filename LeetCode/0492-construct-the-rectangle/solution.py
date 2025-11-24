class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # find all pairs
        pairs = []
        for i in range(1, (area // 2) + 2):
            if area % i == 0:
                pairs.append([i, int(area / i)])

        print(pairs)

        # find smallest difference in pairs
        smallest_diff = 99999999999
        current_diff = 0
        smallest_diff_index = 0
        for i in range(len(pairs)):

            # make sure length is bigger
            if pairs[i][0] < pairs[i][1]:
                pairs[i][0], pairs[i][1] = pairs[i][1], pairs[i][0]
            current_diff = pairs[i][0] - pairs [i][1]
            if current_diff < smallest_diff:
                smallest_diff = current_diff
                smallest_diff_index = i

        return pairs[smallest_diff_index]



