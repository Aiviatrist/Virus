from tkinter import*
import random
root=Tk()
root.title("Friends list")
root.geometry("400x400")
en=Entry(root)
en.place(relx=0.5,rely=0.2,anchor=CENTER)
la=Label(root)
la2=Label(root)
la3=Label(root)
list21=[]
def lankom():
    ma=en.get()
    list21.append(ma)
    la["text"]="Your friends list is: "+str(list21)

def randomk():
    length=len(list21)
    genrannum=random.randint(0,length-1)
    la2["text"]="Your generated random number is: "+str(genrannum)
    ranfrien=list21[genrannum]
    la3["text"]="Your lucky friend is: "+str(ranfrien)
    
btn=Button(root,text="Add to the friend list",command=lankom)
btn.place(relx=0.5,rely=0.3,anchor=CENTER) 
la.place(relx=0.5,rely=0.4,anchor=CENTER)
btn2=Button(root,text="Show my lucky friend",command=randomk)
btn2.place(relx=0.5,rely=0.5,anchor=CENTER)
la2.place(relx=0.5,rely=0.6,anchor=CENTER)
la3.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()