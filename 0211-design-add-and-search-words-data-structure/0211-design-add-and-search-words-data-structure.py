class TrieNode:
  def __init__(self, key: str, children = None, isWord = False):
    self.key = key
    self.children = children or {}
    self.isWord = isWord
  
  def __repr__(self):
    return f"Key: {self.key} Children{self.children} isWord:{self.isWord}"


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode("ROOT")
        

    def addWord(self, word: str) -> None:
        head = self.trie
        
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode(c)
            
            head = head.children[c]
        
        head.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.isWord


        return dfs(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
param_2 = obj.search("aa")


# class TrieNode:
#   def __init__(self, key: str, children = None, isWord = False):
#     self.key = key
#     self.children = children or {}
#     self.isWord = isWord
  
#   def __repr__(self):
#     return f"Key: {self.key} Children{self.children} isWord:{self.isWord}"

# class Trie:
#     def __init__(self):
#         self.trie = TrieNode("ROOT")

#     def insert(self, word: str) -> None:
#         head = self.trie
        
#         for c in word:
#             if c not in head.children:
#                 head.children[c] = TrieNode(c)
            
#             head = head.children[c]
        
#         head.isWord = True
        

#     def search(self, word: str) -> bool:
#         head = self.trie
        
#         for c in word:
#             if c not in head.children:
#               return False

#             head = head.children[c]
        
#         return head and head.isWord
        

#     def startsWith(self, prefix: str) -> bool:
#         head = self.trie
        
#         for c in prefix:
#             if c not in head.children:
#               return False
            
#             head = head.children[c]
            
#         return head and head.key != "ROOT"
        


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert("CAT")
# # param_2 = obj.search("CAT")
# # param_3 = obj.startsWith("CA")

# # print(param_2, param_3)