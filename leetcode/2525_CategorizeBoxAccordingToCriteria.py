class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        L = length
        W = width
        H = height

        is_bulky = any(a >= 10000 for a in (L, W, H)) or (L * W * H >= 1000000000)
        is_heavy = (mass >= 100)

        table = {
            (True, True): "Both",
            (False, False): "Neither",
            (True, False): "Bulky",
            (False, True): "Heavy"
        }

        return table[(is_bulky, is_heavy)]
