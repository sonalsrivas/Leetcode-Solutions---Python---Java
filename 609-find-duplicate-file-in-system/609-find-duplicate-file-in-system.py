class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapContentPath=dict()
        res=defaultdict(set)
        for path in paths:
            
            root=re.findall(r"([\w*/\w*]*) ",path)[0]
            filecont = re.findall(r" (\w*\.\w*)\((\w*)\)", path)
            for file, content in filecont:
                if content not in mapContentPath:
                    mapContentPath[content]=root+'/'+file
                else:
                    res[content].add(root+'/'+file)
                    res[content].add(mapContentPath[content])
        return res.values()