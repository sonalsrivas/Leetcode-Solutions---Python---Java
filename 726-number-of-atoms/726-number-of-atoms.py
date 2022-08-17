from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = [c for c in formula]
        n = len(formula)

        def processDigit(i):
            num = ''
            while i < n and formula[i].isdigit():
                num += formula[i]
                i += 1
            # i-=1
            if not num:
                num = '1'
                # i+=1
            print("returning :: processDigit :: ", num, " at index = ", i)  # ,formula[i])
            return int(num), i

        def assimilateD(nd, d):
            print("Inside :: assimilateD :: ", d, nd)
            for k in nd:
                if k in d:
                    d[k] += nd[k]
                else:
                    d[k] = nd[k]
            print("returning :: assimilateD :: ", d)
            return d

        def f(n, i):
            print("INSIDE OF F(), ", i, formula[i])
            d = {}
            j = i
            # if i < n and formula[i] == '(':

            #    i += 1
            while i < n and formula[i] != ')':
                # print(i,formula[i])
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
                    print("\t\tadded ", element, d[element])
                if i < n and formula[i] == '(':
                    nd, i = f(n, i + 1)
                    d = assimilateD(nd, d)
            num, i = processDigit(i + 1)
            print("here !! ", num, i, d)
            if num > 1:
                for h in d:
                    d[h] *= num
            return d, i

        d = {};
        i = 0
        while i < n:
            print("******THE LOOP BEGINS = ", i, d)
            nd, i = f(n, i)
            # i+=1
            d = assimilateD(nd, d)
            print("-----THE LOOP ENDS = ", i, d)
        res = ''
        sortedDict = sorted(list(d.keys()))
        for i in sortedDict:
            nm = str(d[i])
            if nm == '1':
                nm = ''
            res += i + nm
        return res
