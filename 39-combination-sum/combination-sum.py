class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                backtrack(
                    i,                      # allow reuse
                    remaining - candidates[i],
                    path + [candidates[i]]
                )

        backtrack(0, target, [])
        return result
