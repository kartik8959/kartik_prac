class Stack:
    def __init__(self):
        self.arr=[None]*5
        self.tos=-1

    def push(self,item):
        if(self.tos==4):
            print("stack overflow")
            
        else:
            self.tos+=1
            self.arr[self.tos]=item
            print(f"{item} pushed into the stack...")
    def pop(self):
        if self.tos==-1:
            print("stack underflow")
            return 0
        else:
            x=self.arr[self.tos]
            self.tos-=1
            return x
    def display(self):
        if self.tos==-1:
            print("stack underflow")
        else:
            i=0
            
            while(i<=s.tos):
                print(self.arr[i]) 
                i+=1

s=Stack()
while True:
    
    ch=int(input("enter your choice : "))
    if ch==1:
        inp1=int(input("enter element to push : "))
        s.push(inp1)
    elif ch==2:
        x=s.pop()
        if x!=0:
            print("poped element is ",x)
    elif ch==3:
        print("bye bye...")
        break
    elif ch==4:
        s.display()




        

    
