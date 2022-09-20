class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        mapNameOccurrence={}
        for i in range(len(names)):
            name=names[i]
            
            if name in mapNameOccurrence:
                
                while name in mapNameOccurrence:
                    mapNameOccurrence[names[i]]+=1
                    newSuffix="("+str(mapNameOccurrence[names[i]])+")"
                    
                    name=names[i]+newSuffix
                    
                names[i]=name
                
            mapNameOccurrence[name]=0
        return names
    
"""
["pes","fifa","gta","pes","fifa","gta","pes(1)","fifa","gta","pes","fifa","gta","pes","pes"]
["kaido","kaido(1)","kaido","kaido(1)"]
"""