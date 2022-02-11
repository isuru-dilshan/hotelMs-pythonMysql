from tkinter import *
from PIL import Image, ImageTk    # ==== pip install pillow
from tkinter import ttk
import random,os
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import tempfile

class Hotel_Report:
    def __init__(self, root):
        self.root=root
        self.root.title(" Meal Billing")
        self.root.geometry("1295x550+230+220")

        # ============== Variables ================================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z = random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        # ============= Product Categories list =========================

        # Breakfast
        self.Category=["Select Option","Breakfast","Lunch","Dinner","Dessert","Drink"]

        self.SubCatBreakfast=["SeaFoods","Soups","Sandwich",]
        self.BSeaFoods=["Salmon","Octopus","Crab","Shrimp"]
        self.Price_salmon=500
        self.Price_octopus=150
        self.Price_crab=250
        self.Price_Shrimp=180

        self.BSoups=["SeaFood","Chicken","Vegitable"]
        self.Price_Bsoseafood=450
        self.Price_Bsochicken=500
        self.Price_Bsovegitable=250

        self.BSandwich=["Fish","Chicken","Vegitable"]
        self.Price_Bsfish=150
        self.Price_Bschicken=120
        self.Price_Bsvegitable=100

        # Lunch
        self.SubCatLunch=["Soups","Haney BBQ","Pizza"]
        self.LSoups=["SeaFood","Chicken","Vegitable"]
        self.Price_Lsoseafood = 200
        self.Price_Lsochicken = 400
        self.Price_Lsovegitable = 150

        self.LHaneyBBQ=["Beef","Fish","Chicken"]
        self.Price_Lhbeef = 200
        self.Price_Lhchicken = 400
        self.Price_Lhfish = 250

        self.LPizza=["Vegitable","Meat","SeaFood"]
        self.Price_Lpvagitable = 150
        self.Price_Lpmeat=100
        self.Price_Lpseafood=200

        # Dinner
        self.SubCatDinner=["SeaFoods","Grilled","Pasta"]
        self.DSeaFoods=["Salmon","Octopus","Crab","Shrimp"]
        self.Price_Dssalmon = 200
        self.Price_Dsoctopus = 100
        self.Price_Dscrab = 160
        self.Price_Dsshrimp = 80

        self.DGrilled = ["Chicken","Fish","Beef"]
        self.Price_Dgchicken = 300
        self.Price_Dgfish = 100
        self.Price_Dgbeef = 150

        self.DPasta = ["Vegitable","Chicken"]
        self.Price_Dpvegitable = 200
        self.Price_Dpchicken = 150

        # Dessert
        self.SubCatDessert=["IceCreams","salad","Cakes"]
        self.DeIceCreams = ["Apple","Chocolate","Vanilla"]
        self.Price_Deiapple = 80
        self.Price_Deichocolate = 50
        self.Price_Deivanilla = 40

        self.DeSalad = ["Banana","Apple","Mango"]
        self.Price_Desbanana = 40
        self.Price_Desapple = 30
        self.Price_Desmango = 50

        self.DeCake = ["Apple","Banana","Vanilla"]
        self.Price_Decapple = 30
        self.Price_Decbanana = 40
        self.Price_Decvanilla = 50

        # Drink
        self.SubCatDrink=["Beers","Non-Alcoholic","Spirits","Wines"]
        self.DrBeers = ["CoorsLight","Corona","Guinness"]
        self.Price_Drbcoorslight = 200
        self.Price_Drbcorona = 250
        self.Price_Drbguinness = 300

        self.DrNonAlcoholic = ["Ginger","Lemonade","Raspberry"]
        self.Price_DrNginger = 150
        self.Price_DrNlemonade = 200
        self.Price_DrNraspberry = 250

        self.DrSpirits = ["Vodka","Tequila","Bourbon"]
        self.Price_DrSvodka = 1500
        self.Price_DrStequila = 2000
        self.Price_DrSbourbon = 3500

        self.DrWines = ["RedWines","WhiteWines"]
        self.Price_DrWredwines = 2000
        self.Price_DrWwhitewines = 2500



        # ===================== Title ===================================#

        lbl_title = Label(self.root, text=" Meal Billing Details", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =============== LOGO ======================================#

        img2 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\hotel MS\hMS\hotelPackage\image\h.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=50,width=1530,height=620)

        # ===================  Customer LabelFrame ======================
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman", 12, "bold"), bg="white",fg="dark red")
        Cust_Frame.place(x=10,y=5,width=350,height=125)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No:", font=("arial", 12, "bold"), bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman", 10, "bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,text="Customer Name:",font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial", 10, "bold"),width=24)
        self.txtCustName.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lblEmail = Label(Cust_Frame, text="Email:", font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblEmail.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial", 10, "bold"), width=24)
        self.txtEmail.grid(row=2, column=1, stick=W, padx=5, pady=2)

        # ===================  Product LabelFrame ======================
        Product_Frame= LabelFrame(Main_Frame, text="Product", font=("times new roman", 12, "bold"), bg="white",fg="dark red")
        Product_Frame.place(x=370, y=5, width=635, height=125)

        # Category
        self.lblCategory = Label(Product_Frame, text="Select Categories:", font=("arial", 12, "bold"), bg="white",fg="black",bd=4)
        self.lblCategory.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial", 10, "bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # SubCategory
        self.lblSubcategory = Label(Product_Frame, text="Sub Categories:", font=("arial", 12, "bold"),bg="white", fg="black",bd=4)
        self.lblSubcategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.Combo_Subcategory = ttk.Combobox(Product_Frame,value=[""],font=("arial", 10, "bold"), width=24,state="readonly")
        self.Combo_Subcategory.grid(row=1, column=1, stick=W, padx=5, pady=2)
        self.Combo_Subcategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lblProduct = Label(Product_Frame, text="Product Name:", font=("arial", 12, "bold"),bg="white", fg="black", bd=4)
        self.lblProduct.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.Combo_Product = ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial", 10, "bold"), width=24,state="readonly")
        self.Combo_Product.grid(row=2, column=1, stick=W, padx=5, pady=2)
        self.Combo_Product.bind("<<ComboboxSelected>>",self.Price_add)


        # Price
        self.lblPrice = Label(Product_Frame, text="Price:", font=("arial", 12, "bold"), bg="white",fg="black", bd=4)
        self.lblPrice.grid(row=0, column=2, stick=W, padx=5, pady=2)

        self.Combo_Price = ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial", 10, "bold"), width=24,state="readonly")
        self.Combo_Price.grid(row=0, column=3, stick=W, padx=5, pady=2)

        # Qty
        self.lblQty = Label(Product_Frame, text="Qty:", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lblQty.grid(row=1, column=2, stick=W, padx=5, pady=2)

        self.txt_Qty = ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial", 10, "bold"), width=26)
        self.txt_Qty.grid(row=1, column=3, stick=W, padx=5, pady=2)

        # Middle Frame ========================================================
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=135,width=980,heigh=340)

        img=Image.open("image/cool.jpg")
        img=img.resize((490,340),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(MiddleFrame,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=490,height=340)

        img3 = Image.open("image/chiken.jpg")
        img3 = img3.resize((490, 340), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(MiddleFrame, image=self.photoimg3)
        lbl_img3.place(x=490, y=0, width=490, height=340)

        # Search ==============================================================
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=1000, y=10,width=500,height=40)

        self.lblBill = Label(Search_Frame, text="Bill Number:", font=("arial", 12, "bold"), bg="red", fg="white")
        self.lblBill.grid(row=0, column=0, stick=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial", 10, "bold"), width=14)
        self.txt_Entry_Search.grid(row=0, column=1, stick=W, padx=2)

        self.BtnSearch = Button(Search_Frame,command=self.find_bill,text="Search", font=("arial", 10, "bold"), bg="black", fg="white", width=8, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)

        # ===================== Right Frame Bill Aria ===============================

        RightLableFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman", 12, "bold"),bg="white",fg="dark red")
        RightLableFrame.place(x=1000,y=38,width=290,height=364)

        scroll_y=Scrollbar(RightLableFrame,orient=VERTICAL)
        self.textarea=Text(RightLableFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # ===================  Bill counter LabelFrame ======================
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white",fg="dark red")
        Bottom_Frame.place(x=0, y=400, width=1290, height=115)

        self.lblSubTotal = Label(Bottom_Frame, text="SubTotal:", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lblSubTotal.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.txtSubTotal = ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial", 10, "bold"), width=26)
        self.txtSubTotal.grid(row=0, column=1, stick=W, padx=5, pady=2)

        self.lbl_tax = Label(Bottom_Frame, text="Gov Tax:", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lbl_tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.txt_tax = ttk.Entry(Bottom_Frame,textvariable=self.tax_input, font=("arial", 10, "bold"), width=26)
        self.txt_tax.grid(row=1, column=1, stick=W, padx=5, pady=2)

        self.lblAmountTotal = Label(Bottom_Frame, text="Total:", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lblAmountTotal.grid(row=0, column=2, stick=W, padx=5, pady=2)

        self.txtAmountTotal = ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial", 10, "bold"), width=26)
        self.txtAmountTotal.grid(row=0, column=3, stick=W, padx=5, pady=2)

        #  ===================== Button Frame ============
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=560,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",font=("times new roman", 12, "bold"),bg="black",fg="gold",width=12,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill = Button(Btn_Frame,command=self.gen_bill,text="Generate Bill", font=("times new roman", 12, "bold"), bg="black", fg="light Green",width=12,cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnSave = Button(Btn_Frame,command=self.save_bill,text="Save Bill", font=("times new roman", 12, "bold"), bg="black", fg="orange",width=12,cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_Frame,command=self.iprint, text="Print", font=("times new roman", 12, "bold"), bg="black", fg="magenta",width=12,cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_Frame,command=self.clear, text="Clear", font=("times new roman", 12, "bold"), bg="black", fg="white",width=12,cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_Frame,command=self.root.destroy,text="Exit", font=("times new roman", 12, "bold"), bg="black",fg="red",width=12,cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
        self.Welcome()

        self.l=[]

# ========================================= Function Declaration ==========================
    def Welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t ** Welcome To\t4U Hotel **")
        self.textarea.insert(END, f"\n Bill Number:\t{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:\t{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:\t{self.c_phon.get()}")
        self.textarea.insert(END, f"\n Customer Email:\t{self.c_email.get()}")

        self.textarea.insert(END, "\n===========================")
        self.textarea.insert(END, f"\n Products\t\tQTY\tPrice")
        self.textarea.insert(END, "\n=============================\n")

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n{self.product.get()}\t\t{self.qty.get()}\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error", "Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.Welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END, "\n===========================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t{self.total.get()}")
            self.textarea.insert(END, "\n============================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+"txt",'w')
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved",f" Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                    f1.close()
                    found="yes"
            if found=='no':
                messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        z = random.randint(1000, 9999)
        self.bill_no.set(str(X))
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set('')
        self.total.set("")






    def Categories(self,event=""):
        if self.Combo_Category.get()=="Breakfast":
            self.Combo_Subcategory.config(value=self.SubCatBreakfast)
            self.Combo_Subcategory.current(0)

        if self.Combo_Category.get() == "Lunch":
            self.Combo_Subcategory.config(value=self.SubCatLunch)
            self.Combo_Subcategory.current(0)

        if self.Combo_Category.get() == "Dinner":
            self.Combo_Subcategory.config(value=self.SubCatDinner)
            self.Combo_Subcategory.current(0)

        if self.Combo_Category.get() == "Dessert":
            self.Combo_Subcategory.config(value=self.SubCatDessert)
            self.Combo_Subcategory.current(0)

        if self.Combo_Category.get() == "Drink":
            self.Combo_Subcategory.config(value=self.SubCatDrink)
            self.Combo_Subcategory.current(0)

    def Product_add(self,event=""):
        if self.Combo_Subcategory.get()=="SeaFoods":
            self.Combo_Product.config(value=self.BSeaFoods)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Soups":
            self.Combo_Product.config(value=self.BSoups)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Sandwich":
            self.Combo_Product.config(value=self.BSandwich)
            self.Combo_Product.current(0)

        # Lunch
        if self.Combo_Subcategory.get()=="Soups":
            self.Combo_Product.config(value=self.LSoups)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Haney BBQ":
            self.Combo_Product.config(value=self.LHaneyBBQ)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Pizza":
            self.Combo_Product.config(value=self.LPizza)
            self.Combo_Product.current(0)

        # Dinner

        if self.Combo_Subcategory.get() == "SeaFoods":
            self.Combo_Product.config(value=self.DSeaFoods)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Grilled":
            self.Combo_Product.config(value=self.DGrilled)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Pasta":
            self.Combo_Product.config(value=self.DPasta)
            self.Combo_Product.current(0)

        # Dessert

        if self.Combo_Subcategory.get() == "IceCreams":
            self.Combo_Product.config(value=self.DeIceCreams)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "salad":
            self.Combo_Product.config(value=self.DeSalad)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Cakes":
            self.Combo_Product.config(value=self.DeCake)
            self.Combo_Product.current(0)

        # Drink

        if self.Combo_Subcategory.get() == "Beers":
            self.Combo_Product.config(value=self.DrBeers)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Non-Alcoholic":
            self.Combo_Product.config(value=self.DrNonAlcoholic)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Spirits":
            self.Combo_Product.config(value=self.DrSpirits)
            self.Combo_Product.current(0)

        if self.Combo_Subcategory.get() == "Wines":
            self.Combo_Product.config(value=self.DrWines)
            self.Combo_Product.current(0)

    def Price_add(self,event=""):           # sea food
        if self.Combo_Product.get()=="Salmon":
            self.Combo_Price.config(value=self.Price_salmon)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Octopus":
            self.Combo_Price.config(value=self.Price_octopus)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Crab":
            self.Combo_Price.config(value=self.Price_crab)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Shrimp":
            self.Combo_Price.config(value=self.Price_Shrimp)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "SeaFood":    # Soup
            self.Combo_Price.config(value=self.Price_Bsoseafood)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Chicken":
            self.Combo_Price.config(value=self.Price_Bsochicken)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vegitable":
            self.Combo_Price.config(value=self.Price_Bsovegitable)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Fish":       # Sandwich
            self.Combo_Price.config(value=self.Price_Bsfish)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Chicken":
            self.Combo_Price.config(value=self.Price_Bschicken)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vegitable":
            self.Combo_Price.config(value=self.Price_Bsvegitable)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Lunch

        if self.Combo_Product.get() == "SeaFood":          # soup
            self.Combo_Price.config(value=self.Price_Lsoseafood)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Chicken":
            self.Combo_Price.config(value=self.Price_Lsochicken)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vegitable":
            self.Combo_Price.config(value=self.Price_Lsovegitable)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Beef":               # Haney BBQ
            self.Combo_Price.config(value=self.Price_Lhbeef)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Fish":
            self.Combo_Price.config(value=self.Price_Lhfish)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Chicken":
            self.Combo_Price.config(value=self.Price_Lhchicken)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vegitable":               # Pizza
            self.Combo_Price.config(value=self.Price_Lpvagitable)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Meat":
            self.Combo_Price.config(value=self.Price_Lpmeat)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "SeaFood":
            self.Combo_Price.config(value=self.Price_Lpseafood)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Dinner

        if self.Combo_Product.get() == "Salmon":  # seafood
            self.Combo_Price.config(value=self.Price_Dssalmon)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Octopus":
            self.Combo_Price.config(value=self.Price_Dsoctopus)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Crab":
            self.Combo_Price.config(value=self.Price_Dscrab)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Shrimp":
            self.Combo_Price.config(value=self.Price_Dsshrimp)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Chicken":              # Grill
            self.Combo_Price.config(value=self.Price_Dgchicken)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Fish":
            self.Combo_Price.config(value=self.Price_Dgfish)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Beer":
            self.Combo_Price.config(value=self.Price_Dgbeef)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vegitable":                  # Pasta
            self.Combo_Price.config(value=self.Price_Dpvegitable)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Chicken":
            self.Combo_Price.config(value=self.Price_Dpchicken)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Dessert
        if self.Combo_Product.get() == "Apple":
            self.Combo_Price.config(value=self.Price_Deiapple)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Chocolate":
            self.Combo_Price.config(value=self.Price_Deichocolate)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vanilla":
            self.Combo_Price.config(value=self.Price_Deivanilla)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Banana":     # Salad
            self.Combo_Price.config(value=self.Price_Desbanana)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Apple":
            self.Combo_Price.config(value=self.Price_Desapple)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Mango":
            self.Combo_Price.config(value=self.Price_Desmango)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Apple":         # Cake
            self.Combo_Price.config(value=self.Price_Decapple)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Banana":
            self.Combo_Price.config(value=self.Price_Decbanana)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vanilla":
            self.Combo_Price.config(value=self.Price_Decvanilla)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Drinks

        if self.Combo_Product.get() == "CoorsLight":         # Beer
            self.Combo_Price.config(value=self.Price_Drbcoorslight)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Corona":
            self.Combo_Price.config(value=self.Price_Drbcorona)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Guinness":
            self.Combo_Price.config(value=self.Price_Drbguinness)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Ginger":           # Non Alcohol
            self.Combo_Price.config(value=self.Price_DrNginger)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Lemonade":
            self.Combo_Price.config(value=self.Price_DrNlemonade)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Raspberry":
            self.Combo_Price.config(value=self.Price_DrNraspberry)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Vodka":               # Spirits
            self.Combo_Price.config(value=self.Price_DrSvodka)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Tequila":
            self.Combo_Price.config(value=self.Price_DrStequila)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "Bourbon":
            self.Combo_Price.config(value=self.Price_DrSbourbon)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "RedWines":  # Wines
            self.Combo_Price.config(value=self.Price_DrWredwines)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get() == "WhiteWines":
            self.Combo_Price.config(value=self.Price_DrWwhitewines)
            self.Combo_Price.current(0)
            self.qty.set(1)






























if __name__ == '__main__':
    root = Tk()
    obj = Hotel_Report(root)
    root.mainloop()