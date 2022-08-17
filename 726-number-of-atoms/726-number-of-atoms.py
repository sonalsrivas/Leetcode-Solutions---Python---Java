class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = [c for c in formula]
        n = len(formula)

        def processDigit(i):
            num = ''
            while i < n and formula[i].isdigit():
                num += formula[i]
                i += 1
            if not num:
                num = '1'
            return int(num), i

        def assimilateD(nd, d):
            for k in nd:
                if k in d:
                    d[k] += nd[k]
                else:
                    d[k] = nd[k]
            return d

        def recurseBranch(i):
            d = {}
            while i < n and formula[i] != ')':
                element = ''
                if formula[i].isupper():
                    element += formula[i]
                    i += 1
                    if i < n and formula[i].islower():
                        element += formula[i]
                        i += 1
                    num, i = processDigit(i)
                    if element in d:
                        d[element] += num
                    else:
                        d[element] = num
                if i < n and formula[i] == '(':
                    nd, i = recurseBranch(i + 1)
                    d = assimilateD(nd, d)
            num, i = processDigit(i + 1)
            if num > 1:
                for h in d:
                    d[h] *= num
            return d, i

        mapElementCount = {}
        index = 0
        while index < n:
            newMapElementCount, index = recurseBranch(index)
            mapElementCount = assimilateD(newMapElementCount, mapElementCount)

        resultString = ''
        for orderedElement in sorted(list(mapElementCount.keys())):
            countStr = str(mapElementCount[orderedElement])
            if countStr == '1':
                countStr = ''
            resultString += orderedElement + countStr
        return resultString