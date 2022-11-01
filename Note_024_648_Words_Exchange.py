"""
    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/replace-words
    在英语中，我们有一个叫做词根(root)的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为继承词(successor)。
    例如，词根an，跟随着单词other(其他)，可以形成新的单词another(另一个)。现在，给定一个由许多词根组成的词典 dictionary和一
    个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词
    根替换它。你需要输出替换之后的句子。

    Input_1: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
    Output_1: "the cat was rat by the bat"
    Input_2: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
    Output_2: "a a b c"

"""
# Leetcode版
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isend = False
        self.iswhole = False

    def insert(self, word: str) -> None:
        node = self
        for wd in word:
            ch = ord(wd) - ord('a')
            if not node.children[ch] and not node.iswhole:
                node.children[ch] = Trie()
            elif not node.children[ch] and node.iswhole:
                node.children[ch] = Trie()
                node.iswhole = True
            node = node.children[ch]
        node.isend = True
        node.iswhole = True

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



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        obj = Trie()
        for word in dictionary:
            obj.insert(word)
        my_sentence = list(sentence.split())
        for i, word in enumerate(my_sentence):
            for j, ch in enumerate(word):
                node = obj.searchPrefix(word[:j])
                if not node:
                    break
                elif node and node.isend:
                    my_sentence[i] = word[:j]
                    break
        return ' '.join(my_sentence)
