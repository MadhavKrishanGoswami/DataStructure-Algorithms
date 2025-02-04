class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        visiting_node = self.root
        
        for letter in word:
            if letter not in node.children:
                visiting_node.children[letter] = TrieNode()
            visiting_node = visiting_node.children[letter]  
        visiting_node.is_end = True
        
    def search(self, word) -> bool:
        visiting_node = self.root
        
        for letter in word:
            if letter not in visiting_node.children:
                return False
            visiting_node = visiting_node.children[letter]
        return visiting_node.is_end
    def startWith(self, prefix) -> bool:
        visiting_node = self.root
        
        for letter in prefix:
            if letter not in visiting_node.children:
                return False
            visiting_node = visiting_node.children[letter]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # True
    print(trie.search("app"))     # False
    print(trie.startWith("app"))  # True
    trie.insert("app")
    print(trie.search("app"))     # True
        
          
        



