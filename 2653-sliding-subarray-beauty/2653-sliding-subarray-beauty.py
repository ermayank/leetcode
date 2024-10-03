class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        
        countArr = [0]*101
        
        # Get xth smallest element
        def getxSmallEl():
            count = x
            for i in range(len(countArr)-1, -1, -1):
                if countArr[i] > 0:
                    count -= countArr[i]
                    if count <= 0:
                        res.append(-i)
                        return
            res.append(0)
            

        # First Window
        for i in range(k):
            if nums[i] < 0:
                countArr[abs(nums[i])] += 1
        getxSmallEl()
        
        # Rest of the Array
        for i in range(k, len(nums)):
            elToAdd = nums[i]
            elToDelete = nums[i - k]
            print(i-k)
            if elToAdd < 0:
                countArr[abs(elToAdd)] += 1
                
            if elToDelete < 0:
                countArr[abs(elToDelete)] -= 1
                print(elToDelete)
                print(abs(elToDelete))
            
            getxSmallEl()
        
        return res

# class Solution:
#     def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
#         res = []
        
#         countArr = [0] * 101  # Adjusted size to accommodate nums values in range [-100, 100]
        
#         # Get xth smallest element
#         def getxSmallEl():
#             count = x
#             for i in range(len(countArr) - 1, -1, -1):
#                 if countArr[i] > 0:
#                     count -= 1
#                     if count == 0:
#                         res.append(-i)  # Append the correct negative value
#                         return
#             res.append(0)
            

#         # First Window
#         for i in range(k):
#             if nums[i] < 0:
#                 countArr[abs(nums[i])] += 1
#         getxSmallEl()
        
#         # Rest of the Array
#         for i in range(k, len(nums)):
#             elToAdd = nums[i]
#             elToDelete = nums[i - k]
#             if elToAdd < 0:
#                 countArr[abs(elToAdd)] += 1
#             if elToDelete < 0:
#                 countArr[abs(elToDelete)] -= 1
            
#             getxSmallEl()
        
#         return res

            
        
        