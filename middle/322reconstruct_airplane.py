class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ret = []
        start=""
        index=0
        for tic in tickets:
            small=""
            if len(ret)==0:
                start=="JFK"
            for idx,pair in enumerate(tic):
                if pair[0]==start:
                    if small=="":
                        small=pair[1]
                        index=idx
                    elif pair[1]<small:
                        small=pair[1]
                        index=idx
            ret.append(tic[idx])
