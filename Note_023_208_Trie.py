"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/implement-trie-prefix-tree
    Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当
    多的应用情景，例如自动补完和拼写检查。请你实现 Trie 类：
    Trie() 初始化前缀树对象。
    void insert(String word)向前缀树中插入字符串 word 。
    boolean search(String word)如果字符串word在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
    boolean startsWith(String prefix) 如果之前已经插入的字符串word的前缀之一为 prefix,返回 true ；否则，返回
    false 。

    Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
           [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output: [null, null, true, false, true, null, true]
"""


# Leetcode 版
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isend = False

    def insert(self, word: str) -> None:
        node = self
        for wd in word:
            ch = ord(wd) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isend = True

    def searchPrefix(self, word: str) -> "Trie":
        node = self
        for wd in word:
            ch = ord(wd) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isend

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

