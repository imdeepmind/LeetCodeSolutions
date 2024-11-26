class TrieNode:
  def __init__(self, key: str, children = None, isWord = False):
    self.key = key
    self.children = children or {}
    self.isWord = isWord
  
  def __repr__(self):
    return f"Key: {self.key} Children{self.children} isWord:{self.isWord}"

class Trie:
    def __init__(self):
        self.trie = TrieNode("ROOT")

    def insert(self, word: str) -> None:
        head = self.trie
        
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode(c)
            
            head = head.children[c]
        
        head.isWord = True
        

    def search(self, word: str) -> bool:
        head = self.trie
        
        for c in word:
            if c not in head.children:
              return False

            head = head.children[c]
        
        return head and head.isWord
        

    def startsWith(self, prefix: str) -> bool:
        head = self.trie
        
        for c in prefix:
            if c not in head.children:
              return False
            
            head = head.children[c]
            
        return head and head.key != "ROOT"
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("CAT")
# param_2 = obj.search("CAT")
# param_3 = obj.startsWith("CA")

# print(param_2, param_3)