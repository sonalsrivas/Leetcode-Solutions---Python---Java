#Function should return a list/array containing the required words

''' The function returns a  list of strings 
present in the dictionary which matches
the string pattern.
You are required to complete this method '''
def make_dict(p):
    d={}; k=0; l=[]
    for c in p:
        if c not in d:
            d[c]=k
            k+=1
        l.append(d[c])
    return l
    
def findSpecificPattern(a, p):
    lp=make_dict(p); res=[]
    for word in a:
        lw=make_dict(word)
        if lw==lp:
            res.append(word)
    return res

#{ 
#  Driver Code Starts
#function goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        string = input().strip()
        res = findSpecificPattern(arr, string)
        for i in res:
            print(i, end=" ")
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends