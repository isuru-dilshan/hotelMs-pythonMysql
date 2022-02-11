from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  # pip install pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from customer import Cust_Win
from room import Roombooking
from deatails import DeatailsRoom
from report import Hotel_Report

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\login2.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\login incon.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

         # ============ lables ===============================
        username=Label(frame,text="User Name:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame, text="Password:",font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame,font=("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # ============== Icon Images ==========================
        img2 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\login incon.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\lock_60px.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        # =========================== LoginButton =============================
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman", 15, "bold"),bd=3,relief=RIDGE, fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # =========================== RegisterButton ==========================
        registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # =========================== forget password =========================
        loginbtn = Button(frame, text="Forget Password",command=self.forgot_password_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")

        elif self.txtuser.get()=="isuru" and self.txtpass.get()=="1223":
            messagebox.showinfo("Success","Welcome to Admin")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="7986@1223Id", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                      ))
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Inavalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=RestaurantManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ============================= Reset Password ============================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_security.get()==" ":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.txt_newpass.get()==" ":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="7986@1223Id", database="management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset please Login new Password",parent=self.root2)
                self.root2.destroy()

    # ====================================== Forgot Password Window ==============================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to Reset Password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="7986@1223Id", database="management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please Enter the valid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)
                # ==============================================================================================================================

                security_Q = Label(self.root2, text="Select Security Quetions", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Index Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black",bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15),show="*")
                self.txt_newpass.place(x=50, y=250, width=250)

                # ============================== btn ====================================
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15),fg="white",bg="green")
                btn.place(x=100,y=290)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Tab")
        self.root.geometry("1600x900+0+0")

        # ============================ Variables ===============================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ============================ bg image =================================
        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\reg1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ============================ left image ================================
        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\enjoy-the-little-things-470x550.jpg")
        left_bg = Label(self.root, image=self.bg1)
        left_bg.place(x=50, y=100, width=470, height=550)

        # ============================ main Frame =================================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen",
                             bg="white")
        register_lbl.place(x=20, y=20)

        # ============================ lablel and Entry =========================
        # ====================== row1

        fname = Label(frame, text="First Name:", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name:", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # ===================== row2

        contact = Label(frame, text="Contact No:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email:", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ====================== row3

        security_Q = Label(frame, text="Select Security Quetions", font=("times new roman", 15, "bold"), fg="black",
                           bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Index Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ======================= row4

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15),show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                             fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15),show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ======================= Check Button ======================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                               font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # ======================= Buttons ==========================
        img = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\button.png")
        img = img.resize((200, 55), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2",
                    font=("times new roman", 12, "bold"), fg="white")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\Log.png")
        img1 = img1.resize((200, 45), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"),fg="white")
        b1.place(x=330, y=420, width=200)

    # ===================== Function Declaration ============================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must been same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Plaese Agree Our Terms & Condition")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="7986@1223Id", database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist,Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")

    def return_login(self):
        self.root.destroy()

class RestaurantManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL Management System")
        self.root.geometry("1550x800+0+0")

        # ============================ 1 st img =======================
        img1=Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\hotel1 .jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # ============================ Logo ===========================
        img2 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\h.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ============================= Title ===========================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # ============================= Main Frame ======================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # ============================= Menu =============================
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman",20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ============================= btn Frame ======================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14, "bold"), bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS",command=self.details_room,width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="Meals", width=22,command=self.report,font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT",command=self.logout,width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ================================= Right side image ================
        img3 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\hotel.jpg")
        img3 = img3.resize((1310,590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1330, height=590)

        # ================================ down images =======================
        img4 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\oreng.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\pizza.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DeatailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = Hotel_Report(self.new_window)

if __name__=="__main__":
   main()
