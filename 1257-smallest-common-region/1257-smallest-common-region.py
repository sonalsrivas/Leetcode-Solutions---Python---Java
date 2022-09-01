class Solution:
    def findSmallestRegion(self, regions, region1, region2):
        mapNodeParent={}
        for regionFamily in regions:
            parent=regionFamily[0]
            for region in regionFamily[1:]:
                mapNodeParent[region]=parent

        setOfAncestors=set()
        setOfAncestors.add(region1)
        regionAncestor=region1
        while regionAncestor in mapNodeParent:
            regionAncestor=mapNodeParent[regionAncestor]
            setOfAncestors.add(regionAncestor)

        while region2 not in setOfAncestors:
            region2=mapNodeParent[region2]

        return region2