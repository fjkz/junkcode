N = int(input())
itinerary = [[0, 0, 0]]
for _ in range(N):
    itinerary.append([int(w) for w in input().split()])

def possible(itinerary):
    for i in range(1, len(itinerary)):
        t0, x0, y0 = itinerary[i-1]
        t1, x1, y1 = itinerary[i]
        if (t1 - t0) < abs(x1 - x0) + abs(y1 - y0):
            return False
        if ((t1 - t0) - abs(x1 - x0) - abs(y1 - y0)) % 2 != 0:
            return False
    return True

if possible(itinerary):
    print("Yes")
else:
    print("No")
