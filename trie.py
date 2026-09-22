# *
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False # * marking valid word

class Trie(object):
    # I know trie is like, prefix tree so you store each letter as linked to its previous? 

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        # * 
        current = self.root

        for letter in word:
            # also specifically if not already existing
            if letter not in current.children:
                current.children[letter] = TrieNode()

            current = current.children[letter]

        current.end = True # mark as valid word    

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]

        return current.end
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        # similar to search but doesn't have to end w/ valid ending
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)