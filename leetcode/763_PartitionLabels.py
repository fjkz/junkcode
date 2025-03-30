class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        set_list = [set(s[0])]
        size_list = [1]

        for c in s[1:]:
            n = len(set_list)

            # find "c"
            ic = -1
            for i in range(n):
                part = set_list[i]
                if c in part:
                    ic = i
                    break

            if ic < 0:
                # case where c is not found
                set_list.append(set(c))
                size_list.append(1)
                continue

            # case where c is found
            size_list[ic] += 1

            # concatinate right parts
            for j in range(ic + 1, n):
                part.update(set_list[j])
                size_list[ic] += size_list[j]

            # truncate right parts
            del set_list[ic + 1:]
            del size_list[ic + 1:]

        return size_list
