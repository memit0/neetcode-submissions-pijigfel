class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Compute the pre and postProduct
        # Get the value of i (index of the target) preProduct[i - 1]
        # Get the postProduct[i + 1]
        # postProduct[i + 1] * preProduct[i - 1]
        preProduct, postProduct = [], []
        total = 1
        for num in nums:
            total *= num
            preProduct.append(total)
        total = 1
        for num in nums[::-1]:
            total *= num
            postProduct.append(total)
        postProduct = postProduct[::-1]

        output = [0] * len(nums)
        output[0] = postProduct[1]
        output[-1] = preProduct[-2]
        for i in range(1, len(nums) - 1):
            output[i] = (preProduct[i - 1] * postProduct[i + 1]) 
        
        return output