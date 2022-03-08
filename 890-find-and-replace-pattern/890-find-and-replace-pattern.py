class Solution:
    def findAndReplacePattern(self, w: List[str], p: str) -> List[str]:
        a=[]
        for wd in w:
            d={i:'' for i in p}
            e={i:'' for i in wd}
            match_word=True
            for c,j in zip(wd,p):
                if d[j]==c and e[c]==j:
                    pass
                elif d[j]=='' and e[c]=='':
                    d[j]=c
                    e[c]=j
                else:
                    match_word=False
                    break
            if match_word:
                #print(f"for word {wd}, dict is {d}")
                a.append(wd)
        return a