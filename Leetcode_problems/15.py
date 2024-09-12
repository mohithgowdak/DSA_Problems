from typing import List
class UserMainCode:
    @classmethod
    def getMinimumScore(cls, n: int, arr: List[int]) -> int:
        if len(arr) != n or not all(isinstance(i, int) for i in arr):
            return -1
        
        min_result = min(arr[i - 1] ^ arr[i] for i in range(1, n))
        
        return min_result