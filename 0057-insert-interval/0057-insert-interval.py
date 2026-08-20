class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        start, end = newInterval

        for i, j in intervals:
            # 1. Current interval is completely before newInterval
            if j < start:
                result.append([i, j])

            # 2. Current interval overlaps with newInterval
            elif i <= end:
                start = min(start, i)
                end = max(end, j)

            # 3. Current interval is completely after newInterval
            else:
                result.append([start, end])
                result.extend(intervals[intervals.index([i, j]):])
                return result

        # Add newInterval at the end
        result.append([start, end])

        return result