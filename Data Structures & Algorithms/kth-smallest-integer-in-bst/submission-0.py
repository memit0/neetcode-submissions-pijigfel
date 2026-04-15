# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do preorder traversal and return the kth valid element in the array
        res = []
        self.inorder(root, res)
        print(res)
        i = 0
        while i < len(res):
            if i == k - 1:
                return res[i]
            if res[i]:
                i += 1
    
    def inorder(self, root, res):

        if not root:
            return None
        
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

