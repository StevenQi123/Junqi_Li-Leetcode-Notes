"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/path-sum
    难度：简单
    解法：递归
    题目描述：
    给你二叉树的根节点root和一个表示目标和的整数targetSum 。判断该树中是否存在根节点到叶子节点的路径，
    这条路径上所有节点值相加等于目标和targetSum如果存在返回 true否则，返回 false。叶子节点是指没有子节点的节点

    Input_1: root = [1,2,3], targetSum = 5
    Output_1: false
    Input_2: root = [], targetSum = 0
    Output_2: false

"""

"""
    对于树一类的题目，往往采用自递归，我们首先明确使用前序遍历，那么就是root节点，然后左子树，右子树
"""


# Leetcode版
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right


"""

    接下来是对于ACM模式，数组转二叉树的处理
    class TreeNode(object):
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def creat_tree(input_list):
        if len(input_list) == 0 or input_list is None:
            return None
        data = input_list.pop(0)
        if data is None:
            return None
        node = TreeNode(data)
        node.left = creat_tree(input_list)
        node.right = creat_tree(input_list)
        return node
        
"""

# ACM版
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def creat_tree(input_list):
    if len(input_list) == 0 or input_list is None:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = creat_tree(input_list)
    node.right = creat_tree(input_list)
    return node

def hasPathSum(root,targetSum):
    if not root:
        return False
    if root.left is None and root.right is None and root.val == targetSum:
        return True
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

# root = [5,4,8,11,0,13,4,7,2,0,0,0,1]
while True:
    try:
        s = list(map(int,input().split()))
        targetSum = int(input())
        root = creat_tree(s)
        print(hasPathSum(root,targetSum))
    except:
        break
