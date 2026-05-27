# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root

        while curr:
            if curr:
                break 
            res.append(curr.val)
            curr = curr.right
        return res
        
        