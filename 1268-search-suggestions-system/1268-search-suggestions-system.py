class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        out = []
        products.sort()
        
        for i,c in enumerate(searchWord):
            temp = []
            for p in products:
                if i < len(p) and p[i] == c:
                    temp.append(p)
            out.append(temp[:3])
            products = temp
        
        return out