class PrefixEval:
    def __init__(self,n):
        self.n=n
        self.arr=[None]*n
        self.tos=-1

    def push(self,item):
        if self.tos==self.n-1:
            print("stack overflow ")
            return 0
        else:
            self.tos+=1
            self.arr[self.tos]=item
            
    def pop(self):
        if self.tos==-1:
            print('stack underflow  ')
            return 0
        else:
            x=self.arr[self.tos]
            self.tos-=1
            return x
        
    def isOprand(self,ch):

        # if ord(ch)>=48 and ord(ch)<=57:
        #     return 1
        # else:
        #     return 0
        return ord(ch)>=48 and ord(ch)<=57


    def calculate(self,op1,op2,ch):
        print(ch,'ch')
        if ch=='+':
            return op1+op2
        
        elif ch=='-':
            return op1-op2

        elif ch=='*':
            return op1*op2

        elif ch=='/':
            return op1/op2

        elif ch=='$':
            return op1**op2

        elif ch=="%":
            return op1 % op2
        else:
            return 0.000

    def solve(self,exp):
        r=0.0
        for i in range(len(exp)-1,-1,-1):
            ch=exp[i]
            if self.isOprand(ch)==True:
                self.push(float(ch))
            else:
                op1=self.pop()
                op2=self.pop()
                res=self.calculate(op1,op2,ch)
                self.push(res)
        
        return self.pop()
        
#main body        
prefix=input("enter prefix expresion : ")
obj=PrefixEval(len(prefix))
ans=obj.solve(prefix)
print("your prefix evaluation is :",ans)

