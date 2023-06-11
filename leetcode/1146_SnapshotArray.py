import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.histarr = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        hist= self.histarr[index]
        last = hist[-1]
        if last[0] == self.snap_id:
            last[1] = val
            return
        hist.append([self.snap_id, val])

    def snap(self) -> int:
        cur = self.snap_id
        self.snap_id += 1
        return cur

    def get(self, index: int, snap_id: int) -> int:
        assert snap_id < self.snap_id
        hist= self.histarr[index]
        i = bisect.bisect_right(hist, snap_id, key=lambda a: a[0])
        return hist[i-1][1]
