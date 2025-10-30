from tkinter import *
import mysql.connector as sql


df = Tk()
df.title("Banking App")

# database connectivity
id = IntVar()
 
ds1 = sql.connect(host = 'localhost',
                 user = 'root',
                 password = '12345',
                 use_pure = True)

cr = ds1.cursor()
cr.execute("use bank")
def enqur():
    ide = id.get()
    
    cr.execute("select * from customers where customer_id = "+str(ide))

def register():
    global fn,phone,alt,email,add
    fn= StringVar()
    phone= StringVar()
    alt= StringVar()
    email= StringVar()
    add=StringVar()
    
    r= Label(df,text="ENTER YOUR DETAILS :",
             font=("Times New Roman",14,"underline"),fg="black",bg="orange")
    r.place(x=950,y=150)
     
    r1= Label(df,text="Full Name :",font=("calibri",13),fg="black",bg="lightblue")
    r1.place(x=850,y=200)
    
    en1 = Entry(df,font=("calibri",13),fg="black",bg="white",textvariable=fn)
    en1.place(x=1000,y=200)
    
    r2= Label(df,text="Phone No :",font=("calibri",13),fg="black",bg="lightblue")
    r2.place(x=850,y=240)
    
    en2 = Entry(df,font=("calibri",13),fg="black",bg="white",textvariable=phone)
    en2.place(x=1000,y=240)
    
    r3= Label(df,text="Alternate No:",font=("calibri",13),fg="black",bg="lightblue")
    r3.place(x=850,y=280)
    
    en3 = Entry(df,font=("calibri",13),fg="black",bg="white",textvariable=alt)
    en3.place(x=1000,y=280)

    r4= Label(df,text="Email :",font=("calibri",13),fg="black",bg="lightblue")
    r4.place(x=850,y=320)
    
    en4 = Entry(df,font=("calibri",13),fg="black",bg="white",textvariable=email)
    en4.place(x=1000,y=320)

    r5= Label(df,text="Address :",font=("calibri",13),fg="black",bg="lightblue")
    r5.place(x=850,y=360)
    
    en5 = Entry(df,font=("calibri",13),fg="black",bg="white",textvariable=add)
    en5.place(x=1000,y=360)
    
    def sub():    
        cr.execute("insert into customers values(DEFAULT, %s,%s,%s,%s,%s)",(fn.get(),email.get(),phone.get(),alt.get(),add.get()))

    br1 = Button(df,text="submit",font=("calibri",12),
                 fg="white",bg="green",command=sub)
    br1.place(x=1050,y=410)


img = PhotoImage(file="C:/Users/Admin/OneDrive/Desktop/app icon.png")
df1 = Label(df,image=img) 
df1.pack()

lv1= Label(df,text= "BANK OF STUDENTS",
           font=("Times New Roman",23,"underline"),fg="black",bg="gold")
lv1.place(x=490,y=130)

lv2= Label(df,text= "Enter your Phone_no/Email",font=("calibri",13),fg="white",bg="brown")
lv2.place(x=470,y=190)

lv3 = Entry(df,font=("calibri",15),fg="black",bg="white")
lv3.place(x=470,y=230)

lv4= Label(df,text= "Enter your Password",font=("calibri",13),fg="white",bg="brown")
lv4.place(x=470,y=270)

lv5 = Entry(df,font=("calibri",15),fg="black",bg="white")
lv5.place(x=470,y=310)

lv6 = Button(df,text="Login✔",font=("calibri",11),fg="white",bg="green")
lv6.place(x=520,y=350)

lv6 = Button(df,text="Signup😍",font=("calibri",11),fg="white",bg="green",command=register)
lv6.place(x=620,y=350)

lv7= Label(df,text= "ENQURIY SECTION",font=("Times New Roman",16,"underline",),
           fg="black",bg="orange")
lv7.place(x=70,y=90)

lv8= Label(df,text= "Write your customer ID",font=("Times New Roman",13),
           fg="black",bg="orange")
lv8.place(x=80,y=140)

lv9 = Entry(df,font=("calibri",10),fg="black",bg="white",textvariable=id)
lv9.place(x=80,y=180)

lv10 = Button(df,text="Submit",font=("calibri",10),fg="white",bg="green",command=enqur)
lv10.place(x=120,y=210)

lv11= Label(df,text= "Full_name :",font=("Times New Roman",13),
           fg="black",bg="lightblue")
lv11.place(x=30,y=260)

e1 = Entry(df,font=("calibri",11),fg="black",bg="white")
e1.place(x=170,y=260)

lv12= Label(df,text= "Phone_no :",font=("Times New Roman",13),
           fg="black",bg="lightblue")
lv12.place(x=30,y=300)

e2 = Entry(df,font=("calibri",11),fg="black",bg="white")
e2.place(x=170,y=300)

lv15= Label(df,text= "Atlernate_no :",font=("Times New Roman",13),
           fg="black",bg="lightblue")
lv15.place(x=30,y=340)

e5 = Entry(df,font=("calibri",11),fg="black",bg="white")
e5.place(x=170,y=340)

lv13= Label(df,text= "Email_id :",font=("Times New Roman",13),
           fg="black",bg="lightblue")
lv13.place(x=30,y=380)

e3 = Entry(df,font=("calibri",11),fg="black",bg="white")
e3.place(x=170,y=380)

lv14= Label(df,text= "Address :",font=("Times New Roman",13),
           fg="black",bg="lightblue")
lv14.place(x=30,y=420)

e4 = Entry(df,font=("calibri",11),fg="black",bg="white")
e4.place(x=170,y=420)

lv15 = Button(df,text="Submit",font=("calibri",10),fg="white",bg="green",command=enqur)
lv15.place(x=75,y=480)





































df.mainloop() 