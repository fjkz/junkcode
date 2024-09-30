class CustomStack:

    def __init__(self, maxSize: int):
        self.space = [None] * maxSize
        self.top = - 1

    def push(self, x: int) -> None:
        if self.top == len(self.space) - 1:
            return
        self.top += 1
        self.space[self.top] = x

    def pop(self) -> int:
        if self.top < 0:
            return -1
        top_val = self.space[self.top]
        self.space[self.top] = None
        self.top -= 1
        return top_val

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top + 1)):
            self.space[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
