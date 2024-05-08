class Solution(object):
    def findRelativeRanks(self, scores):
        sorted_scores = sorted(scores, reverse=True)
        ranks = {}
        for i, score in enumerate(sorted_scores):
            if i == 0:
                ranks[score] = "Gold Medal"
            elif i == 1:
                ranks[score] = "Silver Medal"
            elif i == 2:
                ranks[score] = "Bronze Medal"
            else:
                ranks[score] = str(i+1)
                
        return [ranks[score] for score in scores]
