import csv
import tkinter
import tkinter.ttk
import datetime
import tkinter.messagebox
class billing:
    def raise_bill(self):
        wr=open("bill.csv","a",newline="")
        writer=csv.writer(wr)
        for line in self.t1.get_children():
            row=[]
            for r in self.t1.item(line)["values"]:
                row.append(r)
            row.append(self.txt_date.get())
            row.append(self.txt_billid.get())
            row.append(self.txt_customer_name.get())
            writer.writerow(row)
            print(row)
        wr.close()

    def add_to_cart(self):
        if self.txt_customer_name.get()=="":
            tkinter.messagebox.showerror("Super Markert","Invalid Customer Name")
        else:
            rd=open("products.csv","r")
            reader=csv.reader(rd)
            flag=False
            for row in reader:#
                #tkinter.messagebox.showinfo("",row[0]+"="+self.txt_pid.get())
                if str(row[0])==str(self.txt_pid.get()):
                    flag=True
                    pname=row[1]
                    price=row[2]
                    discount=row[4]
                    netprice=int(price)-int(price)*float(discount)/100
                    self.tp=self.tp+int(price)*int(self.txt2_qty.get())
                    self.total_discount=self.total_discount+int(discount)*int(self.txt2_qty.get())

                    total=netprice*int(self.txt2_qty.get())
                    self.total_payable = self.total_payable+total
                    break
            if flag==True:
                self.srno=self.srno+1
                item=[self.srno,self.txt_pid.get(),pname,self.txt2_qty.get(),price,discount,netprice,total]

                self.t1.insert("",index=self.srno,values=item)
                self.txt_total_price.delete(0,tkinter.END)
                self.txt_total_price.insert(0,str(self.tp))
                self.txt_total_discount.delete(0, tkinter.END)
                self.txt_total_discount.insert(0,str(self.total_discount))
                self.txt_total_payable.delete(0, tkinter.END)
                self.txt_total_payable.insert(0,str(self.total_discount))
            else:
                tkinter.messagebox.showerror("Super Store","Invalid Product")

    def __init__(self):

        self.root=tkinter.Tk()
        self.srno=0
        self.tp=0
        self.total_discount=0
        self.total_payable=0
        self.p1=tkinter.PanedWindow(self.root)
        self.p2=tkinter.PanedWindow(self.root)
        self.p3=tkinter.PanedWindow(self.root)

        self.bt_bill=tkinter.Button(self.p3,text="Raise Bill",command=self.raise_bill)

        self.lb_total_price=tkinter.Label(self.p3,text="Total Price")
        self.txt_total_price=tkinter.Entry(self.p3)

        self.lb_total_discount=tkinter.Label(self.p3,text="Total Discount")
        self.txt_total_discount=tkinter.Entry(self.p3)

        self.lb_total_payable=tkinter.Label(self.p3,text="Net payabale")
        self.txt_total_payable=tkinter.Entry(self.p3)

        self.root.geometry("1000x800")

        self.bt1=tkinter.Button(self.p1,text="Add to Cart",command=self.add_to_cart)
        self.lb_date=tkinter.Label(self.p1,text="Date")
        self.txt_date=tkinter.Entry(self.p1)

        self.lb_billid=tkinter.Label(self.p1,text="Bill Number")
        self.txt_billid=tkinter.Entry(self.p1)

        self.lb_customer_name=tkinter.Label(self.p1,text="Customer Name")
        self.txt_customer_name=tkinter.Entry(self.p1,width=50)

        self.lb_pid=tkinter.Label(self.p1,text="Product Code")
        self.txt_pid=tkinter.Entry(self.p1)

        self.lb2_qty=tkinter.Label(self.p1,text="Quantity")
        self.txt2_qty=tkinter.Entry(self.p1)

        self.t1=tkinter.ttk.Treeview(self.p2,columns=("srno","pid","pname","qty","price","discount","netprice","totalprice"))
        self.t1.column("srno",width=15)
        self.t1.heading("srno",text="S No.")
        self.t1.heading("pid", text="Pcode")
        self.t1.heading("pname", text="pname")
        self.t1.heading("qty", text="Qty")
        self.t1.heading("price", text="price")
        self.t1.heading("discount", text="discount")
        self.t1.heading("netprice", text="netprice")
        self.t1.heading("totalprice", text="totalprice")
        self.t1["show"]="headings"

        self.lb_date.grid(row=0,column=0)
        self.txt_date.grid(row=0,column=1)

        self.lb_billid.grid(row=0,column=10)
        self.txt_billid.grid(row=0,column=11)

        self.lb_customer_name.grid(row=2,column=2)
        self.txt_customer_name.grid(row=2,column=3)

        self.lb_pid.grid(row=4,column=0)
        self.txt_pid.grid(row=4,column=1)

        self.lb2_qty.grid(row=4,column=2)
        self.txt2_qty.grid(row=4,column=3)
        self.bt1.grid(row=4,column=4)

        self.txt2_qty.insert(0,"1")
        self.txt_date.insert(0,datetime.date.today())

        self.lb_total_price.grid(row=0,column=0)
        self.txt_total_price.grid(row=0,column=1)

        self.lb_total_discount.grid(row=1,column=0)
        self.txt_total_discount.grid(row=1,column=1)

        self.lb_total_payable.grid(row=2,column=0)
        self.txt_total_payable.grid(row=2,column=1)

        self.txt_pid.bind('<Return>',self.add_to_cart)

        self.bt_bill.grid(row=3,column=1)
        self.t1.pack()

        self.p1.pack()
        self.p2.pack()
        self.p3.pack()

        self.root.mainloop()
#-----------------------------------
#obj=billing()