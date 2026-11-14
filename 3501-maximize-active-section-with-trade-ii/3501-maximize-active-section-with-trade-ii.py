
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:

        n = len(s)
        total_ones = s.count('1')

        starts = []
        ends = []

        # Step 1: Find all continuous 1-runs
        i = 0

        while i < n:
            if s[i] == '1':
                start = i

                while i < n and s[i] == '1':
                    i += 1

                starts.append(start)
                ends.append(i - 1)
            else:
                i += 1

        m = len(starts)

        if m == 0:
            return [0] * len(queries)

        # Step 2: Calculate left and right zero lengths
        left_zero = [0] * m
        right_zero = [0] * m

        for i in range(m):
            if i == 0:
                left_zero[i] = starts[i]
            else:
                left_zero[i] = starts[i] - ends[i - 1] - 1

            if i == m - 1:
                right_zero[i] = n - ends[i] - 1
            else:
                right_zero[i] = starts[i + 1] - ends[i] - 1

        # Maximum gain for each 1-run
        gain = [
            left_zero[i] + right_zero[i]
            for i in range(m)
        ]

        # Step 3: Build iterative Segment Tree (range maximum)
        size = 1
        while size < m:
            size *= 2

        seg = [0] * (2 * size)

        for i in range(m):
            seg[size + i] = gain[i]

        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        # Range maximum query: inclusive [left, right]
        def range_max(left, right):
            left += size
            right += size

            result = 0

            while left <= right:
                if left % 2 == 1:
                    result = max(result, seg[left])
                    left += 1

                if right % 2 == 0:
                    result = max(result, seg[right])
                    right -= 1

                left //= 2
                right //= 2

            return result

        # Step 4: Answer each query
        answer = []

        for l, r in queries:

            # First 1-run whose start > l
            p = bisect_right(starts, l)

            # Last 1-run whose end < r
            q = bisect_left(ends, r) - 1

            # No valid 1-run
            if p > q:
                answer.append(total_ones)
                continue

            if p == q:
                # Only one valid run:
                # Both zero blocks may be clipped.
                best = (
                    min(left_zero[p], starts[p] - l)
                    +
                    min(right_zero[p], r - ends[p])
                )

            else:
                # First valid run: left side may be clipped
                first_gain = (
                    min(left_zero[p], starts[p] - l)
                    + right_zero[p]
                )

                # Last valid run: right side may be clipped
                last_gain = (
                    left_zero[q]
                    + min(right_zero[q], r - ends[q])
                )

                best = max(first_gain, last_gain)

                # Fully contained middle runs
                if p + 1 <= q - 1:
                    middle_gain = range_max(p + 1, q - 1)
                    best = max(best, middle_gain)

            answer.append(total_ones + best)

        return answer
