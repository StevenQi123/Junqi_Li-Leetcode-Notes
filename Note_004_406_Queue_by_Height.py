"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/queue-reconstruction-by-height
    难度：中等
    解法：贪心算法、排序、插入
    题目描述：
    假设有打乱顺序的一群人站成一个队列，数组 people表示队列中一些人的属性（不一定按顺序）。
    每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面正好有 ki个身高大于或等于 hi 的人。
    请你重新构造并返回输入数组 people所表示的队列。返回的队列应该格式化为数组 queue，
    其中 queue[j] = [hj, kj] 是队列中第 j个人的属性（queue[0] 是排在队列前面的人）

    Input_1：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    Output_1：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    Input_2：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    Output_2：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

"""

"""
    这道题其实更像是在给每个人按照身高”归位“，属性已经是安排好了的。这道题最绝妙的思想在于，
    因为属性代表身高大于等于的人的个数，那么往有一个排了一半的队列中，插入一个矮个子的人，该队列不会有任何影响，
    那么我们可以按照每个数组的[0]进行降序排序，优先处理高个子的，这样后续处理矮个子时可以较随意的插入，
    对于数组的[1]我们进行升序排序，毕竟同身高的人，数组的[1]越大越在队列后面
    多变量的排序我们可以使用lambda，例如sort(key = lambda x:(-x[0],x[1]))，lambda就像宏一样可以由我们定义  
    
"""


# Leetcode版
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        # 此时列表为[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
        result = []  # 新列表用来存放结果
        for res in people:
            if res[1] >= len(result):
                result.append(res)
            else:
                # 这里就体现了矮个子插队进来不影响队列，当处理到[6，1]，它可以很自然的排到[7,1]前面
                result.insert(res[1], res)

        return result


# ACM版
"""
    笔者不太确定这类二维数组ACM的输入方式，我把它假设为先输入一个数代表接下来数组的长度，然后每行输入一个数组
    6
    7 0 
    4 4
    7 1
    5 0
    6 1
    5 2
    输出的话看题目具体要求，格式可以参考Note 001基本输出，这里为了方便直接打印数组
    
"""

while True:
    try:
        n = int(input())
        people = []
        for i in range(n):
            a = list(map(int, input().split()))
            people.append(a)
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for res in people:
            if res[1] >= len(result):
                result.append(res)
            else:
                result.insert(res[1], res)

        print(result)

    except:
        break
