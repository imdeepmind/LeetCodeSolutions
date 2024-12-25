class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        count = 0

        for segment in s.split(" "):
            if segment:
                count += 1

        return count