class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        pp = 0
        tp = 0
        while pp < len(players) and tp < len(trainers):
            if players[pp] <= trainers[tp]:
                pp += 1
                tp += 1
            else:
                tp += 1
        return pp
