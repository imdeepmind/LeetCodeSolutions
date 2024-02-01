class Solution:
    @staticmethod
    def list_ch_len(words):
        return len(" ".join(words))

    def break_text_for_justification(self, words, maxWidth):
        lines = []
        line = []
        
        for word in words:
            line_with_new_word = line + [word]
            
            n = self.list_ch_len(line)
            k = self.list_ch_len(line_with_new_word)
            
            if k <= maxWidth:
                line.append(word)
            else:
                lines.append(line)
                line = [word]
        
        if line:
            lines.append(line)
            
        return lines
    
    def add_text_padding(self, lines, maxWidth):
        padded_resp = []
        padded_line = []
        
        for idx, words in enumerate(lines):
            is_last_line = idx+1 == len(lines)
            total_len = self.list_ch_len(words)
            total_words = len(words)
["This", "is", "an", "example", "of", "text", "justification."]
