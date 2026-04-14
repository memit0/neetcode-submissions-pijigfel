# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # we found the node we want to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else: # the node has two children
                minNode = self.minNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val) # why I don't understand this line??

        return root

    def minNode(self, root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur