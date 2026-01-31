# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        
        in_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(in_left, in_right, post_left, post_right):
            if in_left > in_right:
                return None
            
           
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            
            idx = in_map[root_val]
            left_size = idx - in_left
            
            
            root.left = helper(in_left, idx - 1, post_left, post_left + left_size - 1)
            root.right = helper(idx + 1, in_right, post_left + left_size, post_right - 1)
            
            return root
        
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
