from tkinter import*
from PIL import Image,ImageTk #install pip
from tkinter import ttk,messagebox
import sqlite3
import time
import os 
import tempfile # it is used to stored the contents of billing 
class billClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x740+0+0")
        self.root.title("Inventory mangement system | Developed by mangesh")
        self.root.config(bg="white")
        self.cart_list=[]    #it is a cart list which is empty.for storing the data.of total price and quantity and etc.
        self.chk_print=0
        #title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory mangement system",image=self.icon_title,compound=LEFT ,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=140).place(x=0,y=0,relwidth=1,height=70)
        
        #logout button
        btn_logout=Button(self.root,text="logout",command=self.logout,font=("times new roman",19,"bold"),bg="yellow",cursor="hand2",anchor="w").place(x=1250,y=18,width=85,height=35)
        
        #clock
        self.lbl_clock=Label(self.root,text= " Welcome to Inventory mangement system \t\t Date:DD\MM\YYYY \t\t Time: HH\\MM\\SS",font=("times new roman",15,"bold"),bg="#4d636d",fg="white",padx=140)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=40)
        
        
        #=====product frame  1====
        #variables===================================================
        self.var_search=StringVar()
        # self.var_searchttxt=StringVar()
        
        product_frame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        product_frame1.place(x=6,y=120,width=410,height=570)
        #this is a title in productframe 1
        ptitle=Label(product_frame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #====product frame 2====
        
        product_frame2=Frame(product_frame1,bd=4,relief=RIDGE,bg="white")
        product_frame2.place(x=2,y=42,width=398,height=90)
        
        
        lbl_search=Label(product_frame2,text="Search product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(product_frame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(product_frame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=130,height=22)
        btn_search=Button(product_frame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",cursor="hand2").place(x=272,y=47,width=100,height=22)
        
        btn_show_all=Button(product_frame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=272,y=10,width=100,height=22)
        
        #=======All products======this is a frame 3 of all products containing data values

        product_frame3=Frame(product_frame1,bd=3,relief=RIDGE)
        product_frame3.place(x=2,y=140,width=398,height=385)

        scrolly=Scrollbar(product_frame3,orient=VERTICAL)
        scrollx=Scrollbar(product_frame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(product_frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)


        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="Qty")
        self.product_Table.heading("status",text="Status")
        self.product_Table["show"]="headings"


        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=80)
        self.product_Table.column("qty",width=50)
        self.product_Table.column("status",width=50)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        # self.show()
        lbl_not=Label(product_frame1,text="Note:'Enter 0 quantity to remove product from the cart'",font=("goudy old style",13),anchor=W,bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
        
        #====customer frame=====
        #variables================================================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        
        customer_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customer_frame.place(x=420,y=120,width=530,height=70)
        
        ctitle=Label(customer_frame,text="Customer details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(customer_frame,text="Name",font=("times new roman",13),bg="white").place(x=5,y=35)
        txt_name=Entry(customer_frame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=70,y=35,width=160)
        
        lbl_contact=Label(customer_frame,text="Contact no:",font=("times new roman",13),bg="white").place(x=250,y=35)
        txt_contact=Entry(customer_frame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=350,y=35,width=160)
        #this is a calculator cart frame
        cal_cart_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        cal_cart_frame.place(x=420,y=200,width=530,height=360)
        #this is calculator frame
        self.var_cal_input=StringVar()
        cal_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE,bg="white")
        cal_frame.place(x=5,y=10,width=268,height=340)
        
        txt_cal_input=Entry(cal_frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=9,relief=GROOVE,state="readonly",justify=RIGHT) # relief groove is used for to show that this is input field and we can give some input here
        txt_cal_input.grid(row=0,columnspan=4)
                                                                        #we used lambda here to pass argument by ourself.
        btn_7=Button(cal_frame,text="7",font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(cal_frame,text="8",font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(cal_frame,text="9",font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_7=Button(cal_frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
        btn_4=Button(cal_frame,text="4",font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(cal_frame,text="5",font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(cal_frame,text="6",font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(cal_frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(cal_frame,text="1",font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(cal_frame,text="2",font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(cal_frame,text="3",font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(cal_frame,text="*",font=("arial",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn_0=Button(cal_frame,text="0",font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(cal_frame,text="AC",font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(cal_frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(cal_frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
        
        
        
        #this is a  cart frame 
        cart_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=241,height=342)
        self.cart_title=Label(cart_frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray")
        self.cart_title.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cart_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)


        self.cart_table.heading("pid",text="PID")
        self.cart_table.heading("name",text="Name")
        self.cart_table.heading("price",text="Price")
        self.cart_table.heading("qty",text="Qty")
        # self.cart_table.heading("status",text="Status")
        # self.cart_table.heading("status",text="Status")
        self.cart_table["show"]="headings"


        self.cart_table.column("pid",width=40)
        self.cart_table.column("name",width=100)
        self.cart_table.column("price",width=90)
        self.cart_table.column("qty",width=40)
        # self.cart_table.column("status",width=60)
        # self.cart_table.column("status",width=90)
        self.cart_table.pack(fill=BOTH,expand=1)
        self.cart_table.bind("<ButtonRelease-1>",self.get_data_cart) #here we are calling the class of default get_data_cart to get the data from that class function/
        self.show() 
        
        #This is a frame of add cart widgets,this is also section of customer details.
        #variables
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        add_cart_widgets=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        add_cart_widgets.place(x=420,y=560,width=530,height=130)
        
        lbl_p_name=Label(add_cart_widgets,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(add_cart_widgets,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(add_cart_widgets,text="price per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(add_cart_widgets,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(add_cart_widgets,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(add_cart_widgets,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)
        #this lbl stock comes in second main form and in frame of add|update cart.
        self.lbl_stock=Label(add_cart_widgets,text="In Stock ",font=("times new roman",15),bg="white")
        self.lbl_stock.place(x=5,y=70)  # we write .place seperately when we want to modify and call it in function.in future the value will be fluctuatiing.
        
        btn_clear_cart=Button(add_cart_widgets,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(add_cart_widgets,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #Bill Area=====================
        
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=953,y=120,width=440,height=410)
        
        btitle=Label(bill_frame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y) # the right is for that scroll bar will be on the right side and it will fill in y axis.
        
        self.txt_bill_area=Text(bill_frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1) #expand 1 means it is true ,it can expand.
        scrolly.config(command=self.txt_bill_area.yview) # it is yview bcz while scrolling it will scroll in y axis means vertical.
    
        #Bill Area buttons=====================================================================================================================================
        
        bill_menu_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=953,y=530,width=440,height=160)
        
        self.lbl_amount=Label(bill_menu_frame,text="Bill Amount \n [0]",font=("goudy old style",15,"bold"),bd=3,bg="#3f51b5",fg="white")
        self.lbl_amount.place(x=2,y=5,width=130,height=80)    #we write using self when value will be fluctuating in the program as the program runs.
        
        self.lbl_discount=Label(bill_menu_frame,text="Discount \n [5%]",font=("goudy old style",15,"bold"),bd=3,bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=134,y=5,width=130,height=80)
        
        self.lbl_netpay=Label(bill_menu_frame,text="Net Pay \n [0]",font=("goudy old style",15,"bold"),bd=3,bg="#607d8b",fg="white")
        self.lbl_netpay.place(x=266,y=5,width=170,height=80)
        
        btn_print=Button(bill_menu_frame,text="Print",command=self.print_bill,font=("goudy old style",15,"bold"),bd=9,bg="lightgreen",cursor="hand2")
        btn_print.place(x=2,y=90,width=130,height=60)    #we write using self when value will be fluctuating in the program as the program runs.
        
        btn_clear_all=Button(bill_menu_frame,text="Clear All",command=self.clear_all,font=("goudy old style",15,"bold"),bd=9,bg="gray",cursor="hand2")
        btn_clear_all.place(x=134,y=90,width=130,height=60)
        
        btn_generate=Button(bill_menu_frame,text="Generate/Save Bill",command=self.generate_bill,font=("goudy old style",15,"bold"),bd=9,bg="#009688",cursor="hand2")
        btn_generate.place(x=266,y=90,width=170,height=60)
        
        #footer======================
        lbl_footer=Label(self.root,text= " IMS- Inventory mangement system | Developed by Alok \n For any Technical issue contact-832913973" ,font=("times new roman",10,"bold"),bg="#4d636d",fg="white",padx=140)
        lbl_footer.place(x=0,y=700,relwidth=1,height=40)
        
        self.show()
        self.date_time_update()
    #=============================================
    
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result)) #it is used to evaluate the result from the given input from calculator.
        
    #==========
    def show(self):
        con=sqlite3.connect(database=r'ims.db')  #this whole code written for to show the data in the table for showing we write self.show()
        cur=con.cursor()
        try:
            # self.product_Table=ttk.Treeview(product_frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute("select pid,name,price,qty,status from product")   
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())  #this show code is written for to get the data from the product file and put it here the data
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
            
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="": 
                messagebox.showerror("Error","Search input should be required ", parent=self.root)   
            else:
                cur.execute("select pid,name,price,qty,status from product where name LIKE'%"+self.var_search.get()+"%'")

        
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!", parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)      
    
    
    
    def get_data(self,ev):
        f=self.product_Table.focus()  #the data which is shown below calculator is getting from product table and stored in f variable
        content=(self.product_Table.item(f))    #now in content variable it will get the data in items form from f
        row=content['values']   # now it will take out values in row form and it will put the data in the below variables starting from 0 index form.
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_stock.config(text=f"In Stock [{str(row[3])}]")  #it will print the data which is coming from product table and it will paste the data in direct label form.
        self.var_stock.set(row[3])   #it will print the data which is coming from product table and it will paste where this variable is defined in entry.
        self.var_qty.set('1')
    
    
    def get_data_cart(self,ev):
        f=self.cart_table.focus()  #the data which is shown below calculator is getting from product table and stored in f variable
        content=(self.cart_table.item(f))    #now in content variable it will get the data in items form from f
        row=content['values']   # now it will take out values in row form and it will put the data in the below variables starting from 0 index form.
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3]) 
        self.lbl_stock.config(text=f"In Stock [{str(row[4])}]")  #it will print the data which is coming from product table and it will paste the data in direct label form.
        self.var_stock.set(row[4])   #it will print the data which is coming from product table and it will paste where this variable is defined in entry.
         
        
        
        
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error","Please select product from the list",parent=self.root)
        elif self.var_qty.get()=="":   #smalll mistakes can waste your time always focus on the goal
            messagebox.showerror('Error',"Quantity is required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):   #smalll mistakes can waste your time always focus on the goal
            messagebox.showerror('Error',"Invalid Quantity,Qty should be lower than available stock.",parent=self.root)    
        else:
            # price_cal=int(self.var_qty.get())*float(self.var_price.get())
            # price_cal=float(price_cal)
            price_cal=self.var_price.get()
            #pid,pname,total price,stock
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]  #price_cal ka liya .get() nhi aayega bcz ya variable nhi hai isma direct value stored hai.
            
            #the below code is for to update the cart which is in right of the cart table.
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('confirm',"product already present \nDo you want to Update| Remove from the cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #pid,name,price,qty,status
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_qty.get() #qty 
            else:
                self.cart_list.append(cart_data)           
            
            self.show_cart()
            self.bill_updates()
            
    
    def bill_updates(self):
        self.bill_amt=0
        self.net_pay=0  #pid,name,price,qty,stock
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amt*5)/100    
        self.net_pay=self.bill_amt-self.discount
        self.lbl_amount.config(text=f"Bill Amnt\n{str(self.bill_amt)}")
        self.lbl_netpay.config(text=f"Net Pay\n{str(self.net_pay)}")
        self.cart_title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")
        
        
    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())  #this show code is written for to get the data from the product file and put it here the data
            for row in self.cart_list:
                self.cart_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    def generate_bill(self):
        if self.var_cname.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error",f"Customer details required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please add product to the cart",parent=self.root)
        else:
            self.bill_top()#bill_top,bill_middle,bill_bottom. b
            self.bill_middle()
            self.bill_bottom()
            
            fp=open(f"bill/{str(self.invoice)}.txt",'w')  #here the code is written for to making the file and with invoice no and saved in txt form and then we write the text_bill area part it the txt file.
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been generated and saved successfully in the backend",parent=self.root)
            self.chk_print=1
    
            
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        bill_top_temp=f'''
 \t\t  Alok-Inventory
 \t  Phone No. 98725***** , Mumbai-125001
 {str("="*50)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
 {str("="*50)}
 Product Name\t\t\tQTY\tPrice
 {str("="*50)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)


    def bill_bottom(self):
        bill_bottom_temp=f'''
 {str("="*50)}
 Bill Amount\t\t\t\tRs.{self.bill_amt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
 {str("="*50)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db') #this con is here for creating the connection of sqlite3.
        cur=con.cursor()
        try:
            for row in self.cart_list:
                # pid,name,price,qty,stock
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                #we are updating here quantity in the product table after generating the bill.
                cur.execute('Update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit() # it is for doing the whole operattion which is written in the above code.
            con.close()  # this con is connection we are closing the connection here.
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('') 
        self.lbl_stock.config(text=f"In Stock ")  #it will print the data which is coming from product table and it will paste the data in direct label form.
        self.var_stock.set('')   
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cart_title=Label(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart() 
        self.chk_print=0
        
    def date_time_update(self):
        time_=time.strftime("%I:%M:%S") #we can't write H here bcz in which there is 24 hour we have to write for I time for indian standard time from 1 to 12 ,if write only ("%T") it will show time from 1 24.
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f" Welcome to Inventory mangement system \t\t Date:{str(date_)} \t\t Time:{str(time_)}")  #no need to write parent self.root here.
        self.lbl_clock.after(200,self.date_time_update) #it will update the time after 2milli second.
    
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while we printing",parent=self.root)  #parent=self.root is often used to set the parent or container widget for a child widget.      
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print","Please generate the bill,to print the recipt",parent=self.root)
    
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")  

if __name__=="__main__":    
    root=Tk()
    obj=billClass(root)
    root.mainloop()