class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        block = {'A': [], 'B': []}
        previous_color = colors[0]
        length = 1
        for piece in colors[1:]:
            if piece == previous_color:
                length += 1
                continue
            block[previous_color].append(length)
            previous_color = piece
            length = 1
        block[previous_color].append(length)

        alice_moves = sum(max(block - 2, 0) for block in block['A'])
        bob_moves = sum(max(block - 2, 0) for block in block['B'])

        if alice_moves > bob_moves:
            return True
