from collections import deque


class IslandableChecker(object):
    def __init__(self, geo_map, start_point=(0, 0)):
        # 10 x 10
        self.geo_map = [list(input()) for _ in range(10)]
        self.stack = deque()
        self.start_point = start_point

    def check(self, redefined_start_point=None):
        """
        Check if the map can unite as a new island 
        when a sea point is converted to a land one.
        """
        if redefined_start_point is not None:
            self.start_point = redefined_start_point
        # TODO:
        # 1. Search "oxo"(two lands and a sea sandwitches)
        # 2. Check if there are pairs which can reach each other via DFS
        # 3. "The reachable pair" detected -> "YES", or -> "NO"
        for row_idx, row_val in enumerate(self.geo_map):
            for col_idx, col_val in enumerate(row_val):
                if col_val == 'x':
                    self.get_land_pairs(col_idx, row_idx)

    def get_land_pair(self, sea_point):
        """
        Check if there are pairs which describe 
        "oxo"(two lands and a sea sandwitches)

        Returns
        -------
        land_pairs: list
            - Yes: pairs (e.g. [[(1, 2), (2, 3)]])
            - No: empty list
        """
        pass

    def can_reach_each_other(self, pairs_list):
        """Check if there are pairs which can reach each other via DFS"""
        pass

    def dfs(self, dfs_start_point):
        pass