from typing import List
from functools import lru_cache


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 1
            if arr[i] == arr[j]:
                return dp(i+1, j-1)
            res = []
            for mid in range(i, j):
                if arr[mid] == arr[i] or arr[mid] == arr[j]:
                    r = dp(i, mid) + dp(mid+1, j)
                    res.append(r)
            return min(res)
        return dp(0, len(arr)-1)


if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2]
    print(solution.minimumMoves(arr))
    arr = [1, 3, 4, 3, 1, 2, 1]
    print(solution.minimumMoves(arr))
