class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lens = []
        
        for sen in sentences:
            lens.append(len(sen.strip().split(" ")))
        
        return max(lens)