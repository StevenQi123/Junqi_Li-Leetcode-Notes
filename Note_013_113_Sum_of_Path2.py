"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/path-sum-ii
    难度：中等
    解法：深度优先搜索
    题目描述：
    给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有从根节点到叶子节点 路径总和等于给定目标和的路径。
    叶子节点 是指没有子节点的节点。

    Input_1: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output_1: [[5,4,11,2],[5,8,4,5]]
    Input_2: root = [1,2,3], targetSum = 5
    Output_2: []


"""

"""
    和Leetcode112不同在于，112可以通过一个自递归实现，这里我们需要记录下路径，所以用辅函数实现，在不考虑消耗很多
    内存的情况下，我们每一次记录下新加入的路径，在dfs最后，将这个新路径弹出
    
"""

# Leetcode版
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(root, targetSum):
            if not root:
                return False
            path.append(root.val)
            if root.left is None and root.right is None and root.val == targetSum:
                res.append(path[:])
            left = dfs(root.left, targetSum - root.val)
            right = dfs(root.right, targetSum - root.val)
            path.pop()

        dfs(root, targetSum)

        return res

# ACM版（无法正确输出，跟二叉树的构建有关，无法按照题目意思层序构造二叉树）
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_tree(input_list):
    if len(input_list) == 0 or input_list is None:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_tree(input_list)
    node.right = create_tree(input_list)
    return node

while True:

    try:
        nums = input().split(',')
        s = [None if i == 'null' else i for i in nums]
        targetSum = int(input())
        root = create_tree(s)
        print(1)
        path = []
        res = []


        def dfs(root, target):
            if not root:
                print(2)
                return False
            path.append(root.val)
            print(root.left is None)
            print(root.right is None)
            print(root.val)
            print(target)
            if root.left is None and root.right is None and root.val == target:
                res.append(path[:])
            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)
            path.pop()
        dfs(root,targetSum)
        print(res)

    except:
        break

