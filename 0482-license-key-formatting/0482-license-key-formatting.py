class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Removed - from the key
        cleaned_key = s.replace("-", "").upper()

        delta = 1
        while (len(cleaned_key) - delta) % k != 0:
            delta += 1

        # Dividing the first section codes, remaining codes
        first_section = cleaned_key[:delta]
        rest_section = cleaned_key[delta:]

        # Dibiding the remaining codes into k size segments
        i, j = 0, k
        chunked_rest_section = []

        while len(rest_section) > i:
            chunked_rest_section.append(rest_section[i:j])
            i,j = j, j+k
        
        # Joining the segments 
        joined_chunked_rest_section = "-".join(chunked_rest_section)
        
        # Returning the combined key
        return f"{first_section}-{joined_chunked_rest_section}" if joined_chunked_rest_section else first_section
