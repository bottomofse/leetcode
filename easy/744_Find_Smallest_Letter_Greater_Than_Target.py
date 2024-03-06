class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for character in letters:
            if character > target:
                return character
        return letters[0]
