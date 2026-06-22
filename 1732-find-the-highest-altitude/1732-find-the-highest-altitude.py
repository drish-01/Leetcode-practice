class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = [0]
        travel = 0
        for i in gain:
            travel += i
            alt.append(travel)

        alt.sort()
        return alt[len(alt)-1]