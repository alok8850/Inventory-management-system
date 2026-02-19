from tkinter import*
from PIL import Image,ImageTk #install pip
from tkinter import ttk,messagebox
from employee import employeeClass  #from a new file and import class
from supplier import supplierclass
from category import categoryclass
from product import productClass
from sales import salesClass
import sqlite3
import os
import time
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x740+0+0")
        self.root.title("Inventory mangement system | Developed by mangesh")
        self.root.config(bg="white")
        
        #title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory mangement system",image=self.icon_title,compound=LEFT ,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=140).place(x=0,y=0,relwidth=1,height=70)
        
        #logout button
        btn_logout=Button(self.root,text="logout",command=self.logout,font=("times new roman",19,"bold"),bg="yellow",cursor="hand2",anchor="w").place(x=1250,y=18,width=85,height=35)
        
        #clock
        self.lbl_clock=Label(self.root,text= " Welcome to Inventory mangement system \t\t Date:DD\MM\YYYY \t\t Time: HH\\MM\\SS" ,font=("times new roman",15,"bold"),bg="#4d636d",fg="white",padx=140)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=40)
        
        #leftmenu
        self.menulogo=Image.open("images/menu_im.png")
        #self.menulogo=self.menulogo.resize((200,200),Image.ANTIALIAS)
        self.menulogo=self.menulogo.resize((200,200),resample=Image.LANCZOS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")  #bd is border and ridge is border style
        LeftMenu.place(x=0,y=110,width=200,height=565)
        
        lb1_menulogo=Label(LeftMenu,image=self.menulogo)
        lb1_menulogo.pack(side=TOP,fill=X) 
        
        #button of employee with a small img
        self.icon_side=PhotoImage(file="images/side.png")
        
        lb1_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w" ,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w" ,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w" ,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w" ,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w" ,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w" ,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #content
        self.lbl_employee=Label(self.root,text="Total Employee \n [0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white" ,font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=200,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier \n [0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white" ,font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=200,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total Product \n [0]",bd=5,relief=RIDGE,bg="#009688",fg="white" ,font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=1000,y=200,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total Category \n [0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white" ,font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=300,y=400,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total Sales \n [0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white" ,font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=400,height=150,width=300)
        
        
        #footer
        lbl_footer=Label(self.root,text= " IMS- Inventory mangement system | Developed by Alok \n For any Technical issue contact-832913973" ,font=("times new roman",10,"bold"),bg="#4d636d",fg="white",padx=140)
        lbl_footer.place(x=0,y=700,relwidth=1,height=40) 
        
        self.update_content()
        
        
    #=====================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
        
    #=====================================================
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)
        
        
    #=====================================================
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)
        
    #=====================================================
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    
    #=====================================================
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db') #this con is here for creating the connection of sqlite3.
        cur=con.cursor()
        try:
            cur.execute("select * from  product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Products \n [{str(len(product))}]")   # this code is use for to print the total number of product.
            
            cur.execute("select * from  supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers \n [{str(len(supplier))}]") 
            
            cur.execute("select * from  category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total category \n [{str(len(category))}]") 
            
            cur.execute("select * from  employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employees \n [{str(len(employee))}]") 
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total sales \n [{str(bill)}]")
            
            time_=time.strftime("%I:%M:%S") #we can't write H here bcz in which there is 24 hour we have to write for I time for indian standard time from 1 to 12 ,if write only ("%T") it will show time from 1 24.
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f" Welcome to Inventory mangement system \t\t Date:{str(date_)} \t\t Time:{str(time_)}")  #no need to write parent self.root here.
            self.lbl_clock.after(200,self.update_content) #it will update the time after 2milli second.
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")  
        
    
        
if __name__=="__main__":    
    root=Tk()
    obj=IMS(root)
    root.mainloop()   
        