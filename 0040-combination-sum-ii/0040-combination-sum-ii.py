class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to explore further
                if total + candidates[i] > target:
                    break

                current.append(candidates[i])
                backtrack(i + 1, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result