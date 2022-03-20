#User function Template for python3

# return the first non-repeating char in S.
# if there's no non-repeating char, return "-1"
class Node:
    def __init__(self, c=""):
        self.k=c
        self.n=None
        self.p=None
    
def find(s):
    st=dict()
    head=Node("@")
    tail=head
    for i in s:
        
        if i not in st:
            #print(st.keys())
            st[i]=Node(i)
            tail.n=st[i]
            st[i].p=tail
            tail=tail.n
            #if head.k=="@":
            #    head.n=st[i]
        elif st[i]:
            #print(i, st[i].k, st[i].p.k)
            #print(st[i].k)
            while st[i]==tail:
                tail=tail.p
            if st[i].p:
                st[i].p.n=st[i].n
            if st[i].n:
                st[i].n.p=st[i].p
            st[i]=None
    #h=head
    #while h:
    #    print(h.k)
    #    h=h.n
    return head.n.k if head.n else -1
            
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=input().strip()
        print(find(s))
# } Driver Code Ends