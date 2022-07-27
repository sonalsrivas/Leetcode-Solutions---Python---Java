class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        def processForRight(i, j):
            count = 0
            for x in range(i, j):
                if start[x] == 'R':
                    count += 1
                if end[x] == 'R':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def processForLeft(i, j):
            count = 0
            for x in range(i, j):
                if start[x] == 'L':
                    count -= 1
                if end[x] == 'L':
                    count += 1
                if count < 0:
                    return False
            return count == 0

        n = len(start)
        i = 0
        while i < n:
            if start[i] != 'X' and end[i] != 'X' and start[i] != end[i]:
                return False
            cur = None
            if start[i] != 'X':
                cur = start[i]
            elif end[i] != 'X':
                cur = end[i]
            temp_i = i
            if cur == 'R':
                j = i
                while j < n and start[j] in 'XR' and end[j] in 'XR':
                    j += 1
                i = j
                resR = processForRight(temp_i, j)

                if not resR:
                    return resR
            elif cur == 'L':
                j = i
                while j < n and start[j] in 'XL' and end[j] in 'XL':
                    j += 1

                i = j
                resL = processForLeft(temp_i, j)
                if not resL:
                    return resL
            else:
                i += 1
        return True