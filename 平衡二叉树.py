# 在计算二叉树的最大深度的基础上，判断是否满足平衡二叉树的条件。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        if self.depth(root)==-1:    # 选择-1作为返回和判断条件
            return False
        else:
            return True
        
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)     
        if left==-1:           # 选择-1作为返回和判断条件
            return -1
        right = self.depth(root.right)
        if right==-1:
            return -1
        if left>right+1 or right>left+1:    
            return -1
        return max(left+1, right+1)
