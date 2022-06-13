# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob_node(self, root, rob_the_root):
        if root.left is None:
            left_value_robbing_the_root = 0
            left_value_not_robbing_the_root = 0
        else:
            left_value_robbing_the_root = self.rob_node(root.left, True)
            left_value_not_robbing_the_root = self.rob_node(root.left, False)
        
        if root.right is None:
            right_value_robbing_the_root = 0
            right_value_not_robbing_the_root = 0
        else:
            right_value_robbing_the_root = self.rob_node(root.right, True)
            right_value_not_robbing_the_root = self.rob_node(root.right, False)
        
        if rob_the_root:
            return left_value_not_robbing_the_root + right_value_not_robbing_the_root + root.val
        else:
            return max(
                left_value_robbing_the_root + right_value_robbing_the_root,
                left_value_robbing_the_root + right_value_not_robbing_the_root,
                left_value_not_robbing_the_root + right_value_robbing_the_root,
                left_value_not_robbing_the_root + right_value_not_robbing_the_root
            )
    
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rob_node(root, True), self.rob_node(root, False))