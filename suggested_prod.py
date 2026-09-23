class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        # trie system <- just search for the prefix searchWord and return lists of 3 each time? 
        products.sort() # * 
        root = TrieNode()
        
        # classic building the trie
        for product in products:
            curr = root
            for char in product:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                # * keep only 3
                if len(curr.suggestions) < 3:
                    curr.suggestions.append(product)
                    
        # searching for prefixes ** 
        result = []
        curr = root
        not_found = False
        
        for char in searchWord:
            if not not_found and char in curr.children:
                curr = curr.children[char]
                result.append(curr.suggestions)
            else:
                not_found = True
                result.append([])
                
        return result