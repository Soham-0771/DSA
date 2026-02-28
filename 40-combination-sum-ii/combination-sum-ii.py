class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                backtrack(
                    i + 1,                         # move forward, no reuse
                    remaining - candidates[i],
                    path + [candidates[i]]
                )

        backtrack(0, target, [])
        return result
