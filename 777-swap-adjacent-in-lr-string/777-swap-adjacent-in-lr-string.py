class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        def processForRight(i, j):
            print("processing for R from i, j", i,j)
            count = 0
            for x in range(i, j):
                if start[x] == 'R':
                    count += 1
                if end[x] == 'R':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        result = True

        def processForLeft(i, j):
            print("processing for L from i, j", i,j)
            count = 0
            for x in range(i, j):
                print(x, start[x], end[x], count)
                if start[x] == 'L':
                    count -= 1
                if end[x] == 'L':
                    count += 1
                if count < 0:
                    return False
            return count == 0

        n = len(start)
        i = 0
        cur = None
        prev = None
        while i < n:
            print(i, start[i], end[i])
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
                    print("j, start[j], end[j] ",j, start[j], end[j])
                    j += 1
                i = j
                print("R side, i, j ",i, j)
                resR = processForRight(temp_i, j)

                if not resR:
                    return resR
            elif cur == 'L':
                j = i
                while j < n and start[j] in 'XL' and end[j] in 'XL':
                    j += 1

                i = j
                print("L side , ",i, j)
                resL = processForLeft(temp_i, j)
                if not resL:
                    return resL
            else:
                i += 1
        return True