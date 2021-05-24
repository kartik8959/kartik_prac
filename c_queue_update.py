class cque:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*size
        self.rear=self.front=-1

    def insert(self,data):
        if ((self.rear+1)%self.size==self.front):
            print("queue overflow")
            return False
        
        elif  self.front==-1:
            print("**********************")
            self.front=0
            self.rear =0
        
        else:
            self.rear=((self.rear+1)%self.size)
        self.arr[self.rear]=data
        print(f"{data} inserted successfully.{self.rear}")

    def delete(self):
        if self.front==-1:
            print("queue underflow.")
            return False
        
        x=self.arr[self.front]
        
        if (self.rear==self.front):
            self.front=-1
            self.rear=-1
        
        else:
            self.front=((self.front+1) % self.size)
        return x

    def display(self):
        if self.front==-1:
            print("underflow")
            return False
        if self.rear>=self.front:
            for i in range (self.front,self.rear+1):
                print(self.arr[i])

        else:
            for i in range(self.front,self.size):
                print(self.arr[i])
            
            for i in range(0,self.rear+1):
                print(self.arr[i])
#main body
n=int(input("enter size."))
obj=cque(n)
while True:
    choice=int(input("enter your choice."))
    if choice==1:
        item=int(input(f"enter item for insertion. "))
        obj.insert(item)
    elif choice==2:
        x=obj.delete()
        if x!=False and x!=None:
            print(f"deleted item is :{x}....front{obj.front}")
    elif choice==3:
        exit(0)
    elif choice==4:
        obj.display()
    else:
        print("invalid input")

        