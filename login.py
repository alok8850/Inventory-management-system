from tkinter import*
from PIL import Image,ImageTk #install pip
from tkinter import ttk,messagebox
import sqlite3
import os
import email_pass
import smtplib # this is simple mail transfer protocol library which is installed using pip.
import time 
class login_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login  system | Developed by Alok")
        self.root.config(bg="#fafafa")
        self.otp=''
        
        #variables
        self.employee_id=StringVar()
        self.password=StringVar()
        
        #images=====
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png") #image tk is written bcz it is used to access all types of images.
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50) #bd=0 is written bcz there should not be any border.
        #login frame===================================================================================================================================================================================================
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
        
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1) #relwidth is written for to give equal space at both the side
        
        
        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250) #show="*" is used here bcz to hide the details of password while entering.
        
        #Buttons
        btn_login=Button(login_frame,command=self.login,text="Log in",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35) #active bg and active fg will show the color when cursor is on button.
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",font=("times new roman",15,"bold"),fg="lightgray",bg="white").place(x=150,y=355)
        
        #forget password button
        btn_for=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",activeforeground="#00759E",bd=0).place(x=100,y=390) #activeforegroud is for when we click it will show that color.
        
        # #sign in frame===================================================================================================================================================================================================
        # signin_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        # signin_frame.place(x=650,y=570,width=350,height=70)
        
        # lbl_reg=Label(signin_frame,text="Don't have an account?",font=("times new roman",13),bg="white").place(x=60,y=20)
        # btn_signin=Button(signin_frame,text="Sign up",font=("times new roman",15,"bold"),bg="white",activebackground="white",fg="#00759E",activeforeground="#00759E",cursor="hand2",bd=0).place(x=220,y=15)
        
        #images
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")
        
        #code to change the image
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428) 
        
        self.animate() # Here we are  running these prrogram buy calling .
        
        
    
    def login(self):
        con=sqlite3.connect(database=r'ims.db') #this con is here for creating the connection of sqlite3.
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All inputs are required",parent=self.root)
            
            else:
                cur.execute("select utype from  employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get())) #we have written utype here bcz it will fetch usertype while fetching data  ,and we write * it will fetch all type of data.
                user=cur.fetchone() #fetchone and fetchall is that we getting data in row form .in fetchone we take one row data and fetchall we take all row data.
                if user==None:
                    messagebox.showerror("Error","Invalid UserId or Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py") #this code is written for to redirect to dashboard file if username and password both are correct.
                    else:
                        self.root.destroy()
                        os.system("python biling.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db') #this con is here for creating the connection of sqlite3.
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee id must be required",parent=self.root)         
            else:
                cur.execute("select email from  employee where eid=? ",(self.employee_id.get(),)) #we have written utype here bcz it will fetch usertype while fetching data  ,and we write * it will fetch all type of data.
                email=cur.fetchone() #fetchone and fetchall is that we getting data in row form .in fetchone we take one row data and fetchall we take all row data.
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    #variables
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    #we are sending email here
                    chk=self.send_email(email[0]) #we are calling here send_email fuction
                    if chk!='s':
                        messagebox.showerror("Error","Connection Error, Try again",parent=self.root)
                    else:
                        #call and email function
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("Reset Password")
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()
                        #reset password with otp and all
                        title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="OTP sent on registered Email ID",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        #button for confirmation submit of otp.
                        self.btn_reset=Button(self.forget_win,text="Submit",command=self.validate_otp,font=("times new roman",15),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30) # we kept this button in self bcz we want to make changes in future and now also.this button will be hide ,it will show after this otp entering and all.
                        #new password update
                        lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                        #confirm password update
                        lbl_conf_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                        txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)
                        
                        #Update button
                        self.btn_update=Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=("times new roman",15),bg="lightblue") #STATE DISABLED IS WRITTEN BCZ IT OTP IS WRONG ,HE CAN'T CHANGE THE PASSWORD . it will be normal when otp is correct.
                        self.btn_update.place(x=100,y=300,width=100,height=30)
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) #always put exception in def constructor
    
    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db') #this con is here for creating the connection of sqlite3.
            cur=con.cursor()
            try:
                cur.execute("Update employee SET pass=? where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    
    
    
    
    
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_reset.config(state=DISABLED)
            self.btn_update.config(state=NORMAL) #it was disabled before now it is normal ,bcz without correct otp it can't change the password.it will turn into normal if the otp is correct.
        else:
            messagebox.showerror("Error","Invalid OTP ,try again later",parent=self.forget_win) # it is written forget_win bcz if otp is wrong it redirect to the again submit otp page
        
    
    
    
    
    
    
    
    
    def send_email(self,to_): #to is written for to whom we want to send the email ,for that it is written to_.
        s=smtplib.SMTP('smtp.gmail.com',587) # this 587 is port number.for smtp 
        s.starttls() # this is transport layer  for providing security.
        
        email_=email_pass.email_
        pass_=email_pass.pass_
        
        s.login(email_,pass_)
        
        self.otp=int(time.strftime("%H%M%S"))+int(time.strftime("%S"))  #here we are creating otp
        
        subj="IMS- Reset Password OTP"
        msg=f'Dear SIR/MADAM \n\nYour Reset OTP is {str(self.otp)}.\n\n with regards,\n IMS team.' #this is a type of string.
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg) #sendmail is not variable name it is already exist in python file,we should not modify this name.this code is for that we are sending the mail from email_ ,in email_pass file email_ is aloktiwari3967@gmail.com so we are sending email from alok... to email which is registered in employee file.
        chk=s.ehlo() #this ehlo is used to check that email is sent or not.
        if chk[0]==250:   #250 is the number to identify that email is sent.
            return 's'  #s is succeed
        else:
            return 'f'  #f is failed





if __name__=="__main__":    
    root=Tk()
    obj=login_system(root)
    root.mainloop()        
