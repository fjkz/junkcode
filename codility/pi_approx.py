import random

class Answer:
    def pi_approx(pts):
        return sum(x * x + y * y <= 1 for x, y in pts) / len(pts) * 4.0

rands = []
for i in range(0, 100000):
    arr = [random.random(), random.random()]
    rands.append(arr)

print(Answer.pi_approx(rands))
