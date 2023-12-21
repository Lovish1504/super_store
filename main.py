import tkinter
import tkinter.messagebox
import add_products
import viewproducts
import updateproducts
import billing
class myprogram:
    def open_add_products(self):
        obj=add_products.demo()
    def open_viewproducts(self):
        obj=viewproducts.demo()
    def open_updateproducts(self):
        obj=updateproducts.demo()
    def open_raisebill(self):
        obj=billing.billing()
    def __init__(self):

        self.root=tkinter.Tk()
        self.root.geometry("700x600")

        self.mymenu = tkinter.Menu(self.root)
        self.root.title("Welcome to My Super Market")

        self.root.config(menu=self.mymenu)
        self.submenu1 = tkinter.Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Product Management", menu=self.submenu1)
        self.submenu1.add_command(label="Add product",command=self.open_add_products)
        self.submenu1.add_command(label="View product",command=self.open_viewproducts)
        self.submenu1.add_command(label="Remove product",command=self.open_updateproducts)

        self.submenu2 = tkinter.Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Billing Management", menu=self.submenu2)
        self.submenu2.add_command(label="Raise Bill", command=self.open_raisebill)


        self.root.mainloop()
#------------------------------------------
obj=myprogram()

