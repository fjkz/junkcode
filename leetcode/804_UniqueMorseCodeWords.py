class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]
        atoc = {a: c for a, c in zip(string.ascii_lowercase, codes)}
        return len(
            set(
                "".join(atoc[a] for a in word) for word in words
            )
        )
