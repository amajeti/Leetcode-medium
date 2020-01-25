class Solution(object):
    def deckRevealedIncreasing(self, deck):
		deck.sort()
		res = [deck.pop()]
		while deck:
			res.insert(0, res.pop())
			res.insert(0, deck.pop())
		return res
