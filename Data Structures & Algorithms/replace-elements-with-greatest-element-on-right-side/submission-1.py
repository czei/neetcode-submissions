class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_val = [0] * len(arr)
        max_val[len(arr)-1] = arr[len(arr)-1]
        for i in range(len(arr)-2, -1, -1):
            max_val[i] = max(max_val[i+1],arr[i+1])

        max_val[len(arr)-1] = -1
        return max_val