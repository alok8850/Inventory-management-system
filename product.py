from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x550+200+145")
        self.root.title("Inventory Management System | Developed By Alok")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
        #===variables==========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_supp=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        #============
        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)
        
        #===title====
        title=Label(product_frame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d", fg="white").pack(side=TOP,fill=X)
        
        #==details section=====
        lbl_category=Label(product_frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_name=Label(product_frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(product_frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)
        
        #====input section
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style ",15))
        cmb_cat.place(x=150,y=65,width=200)
        cmb_cat.current(0)
        
        cmb_supp=ttk.Combobox(product_frame,textvariable=self.var_supp,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style ",15))
        cmb_supp.place(x=150,y=115,width=200)
        cmb_supp.current(0)
        
        txt_name=Entry(product_frame,textvariable=self.var_name,bg='lightyellow',font=("goudy old style",15)).place(x=150,y=165,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,bg='lightyellow',font=("goudy old style",15)).place(x=150,y=215,width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,bg='lightyellow',font=("goudy old style",15)).place(x=150,y=265,width=200)
        
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style ",15))
        cmb_status.place(x=150,y=315,width=200)
        cmb_status.current(0)
        
        #=====buttons=========
        btn_add=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
        
        #=====searchframe====
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #====options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","category","supplier","name"),state='readonly',justify=CENTER,font=("goudy old style ",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        
        
        #=======product details======

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(p_frame,columns=("pid","category","supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)


        self.productTable.heading("pid",text="P ID")
        self.productTable.heading("category",text="Category")
        self.productTable.heading("supplier",text="supplier")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        
        self.productTable["show"]="headings"

        self.productTable.column("pid",width=90)
        self.productTable.column("category",width=100)
        self.productTable.column("supplier",width=100)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=100)
        self.productTable.column("status",width=100)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
       

        self.show()
        
        
        #=============
    def fetch_cat_sup(self):
        self.cat_list.append("empty")
        self.sup_list.append("empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
                
                
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
            
#=================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_supp.get()=="Select" or self.var_name.get()=="Select" :
                messagebox.showerror("Error","All fields input Must be required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","product already present, try different",parent=self.root)
                else:
                    cur.execute("Insert into product (category,supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                                self.var_cat.get(),
                                                self.var_supp.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added successfully",parent=self.root)
                    self.show()    

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)   


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")   #i have changed here employee to product

        
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)          

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_supp.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="" :
                messagebox.showerror("Error","please select  from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),)) # we have to always give , here.
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product ID",parent=self.root)
                else:
                    cur.execute("update product set category=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?", (
                                                self.var_cat.get(),  #always carefull while writing the variable name it should be line wise from category to status and pid will be the in the last.
                                                self.var_supp.get(),
                                                self.var_name.get(),  
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                self.var_pid.get(),
                                                
                    ))
                    con.commit()
                    messagebox.showinfo("success","product Update successfully",parent=self.root)
                    self.show() 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)   
    
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="" :
                messagebox.showerror("Error","select product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                     cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                     con.commit()
                     messagebox.showinfo("Delete","product Deleted Successfuly",parent=self.root)
                     
                     self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)   

    def clear(self):
        self.var_pid.set("")
        self.var_cat.set("Select")
        self.var_supp.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option ", parent=self.root)
            elif self.var_searchtxt.get()=="": 
                messagebox.showerror("Error","Search input should be required ", parent=self.root)   
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE'%"+self.var_searchtxt.get()+"%'")

        
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!", parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()