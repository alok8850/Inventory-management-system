from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x550+200+145")
        self.root.title("Inventory Management System | Developed By Alok")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #variables=====
        self.bill_list=[]  # this is an empty list
        self.var_invoice=StringVar()
        
        
        
        #===title====
        title=Label(self.root,text="Customer Bill Reports",font=("goudy old style",30),bg="#184a45", fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_invoice=Label(self.root,text="Invoice No.",font=("Times new roman",20),bg="white").place(x=50,y=100)

        
        txt_invoice=Entry(self.root,text=self.var_invoice,font=("Times new roman",20),bg="lightyellow").place(x=180,y=100,width=180,height=28)
        
        lbl_button=Button(self.root,text="Search",command=self.search,font=("Times new roman",20,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=370,y=100,width=120,height=28)
        lbl_clear=Button(self.root,text="Clear",command=self.clear,font=("Times new roman",20,"bold"),bg="lightgray",fg="black",cursor="hand2").place(x=500,y=100,width=120,height=28)
        
        
        
        # bill list===
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=250,height=360)
        
        
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("goudy old style",15,),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
        
        
        #Bill Area===
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=330,y=140,width=470,height=360)
        
        #===title====
        title2=Label(bill_frame,text="Customer bill area",font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        #image===========
        
        self.bill_logo=Image.open("images/cat2.jpg")
        #self.menulogo=self.menulogo.resize((200,200),Image.ANTIALIAS)
        self.bill_logo=self.bill_logo.resize((450,300),resample=Image.LANCZOS)
        self.bill_logo=ImageTk.PhotoImage(self.bill_logo)
        
        lbl_image=Label(self.root,image=self.bill_logo,bd=0)
        lbl_image.place(x=800,y=130)
        
        self.show()
        
    #==============
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        # print(os.listdir('../WEBPYTHON'))
        # print(os.listdir('bill'))
        for i in os.listdir('bill'):
            # print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    
    #=====================
    def get_data(self,ev):
        index_=self.sales_list.curselection()   #this program is written for to print the bill list in terminal of vs code when we click the bill list box
        file_name=self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r') # this code is used for to print the list box file data by clicking the file in list box it will print the data in bill box
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
        
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice number should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r') # this code is used for to print the list box file data by clicking the file in list box it will print the data in bill box
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice NO.",parent=self.root)

    
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
    
if __name__ == "__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()