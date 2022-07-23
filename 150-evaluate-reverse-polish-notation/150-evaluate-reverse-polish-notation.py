class Solution:
    def evalRPN(self, t):
        stack=[]
        opert='+-*/'
        d={'+':self.add,'-':self.subtract,'*':self.multiply, '/':self.divide}
        for i in t:
            if i in opert:
                
                b=stack.pop()
                a=stack.pop()
                #print(a,i,b)
                stack.append(d[i](a,b))
            else:
                #print("getting in ",i)
                stack.append(int(i))
        return stack[-1]
    def add(self, a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self, a,b):
        return a*b
    def divide(self,a,b):
        return int(a/b)