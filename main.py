from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class Bill_App:
   def __init__(self, root):
      self.root = root
      self.root.geometry("1530x800+0+0")
      self.root.title("Billing Software")

      # VARIABLES

      self.bill_number=self.generate_bill_no()
      self.customer_name=tk.StringVar()
      self.customer_mob=tk.StringVar()
      self.customer_email=tk.StringVar()
      self.product_list=[]


      # dicitionary of  categories and subcategories

      self.categories={
         "Electronics": ["Mobile", "Laptop", "Camera"],
         "Groceries": ["Fruits", "Vegetables", "Snacks"],
         "Furniture": ["Sofa", "Table", "Chair"]

      }
      
      # dicitionary of subcategories and product name
      
      self.sub_categories={
         "Mobile": ["Realme", "Vivo", "oppo"],
         "Laptop":["Hp","Dell","MI"],
         "Camera":["Canon","Nikon","Sony"],
         "Fruits": ["Banana", "Apple", "Grape"],
         "Vegetables": ["Bhindi", "Allau", "Rajma"],
         "Snacks": ["Samosa", "Bhel", "Pizza"],
         "Sofa": ["Sectional", "Loveseat", "Futon"],
         "Table": ["Dining", "Coffee", "End"],
         "Chair": ["Rocking", "Club", "Cane"]

      }
      
      # Dictionary of product-Name and price
     
      self.prices = {
       "Realme": 15000, "Vivo": 20000, "oppo": 18000,
       "Hp": 55000, "Dell": 60000, "MI": 45000,
       "Canon": 40000, "Nikon": 45000, "Sony": 50000,
       "Banana": 30, "Apple": 120, "Grape": 90,
       "Bhindi": 40, "Allau": 20, "Rajma": 80,
       "Samosa": 15, "Bhel": 25, "Pizza": 200,
       "Sectional": 25000, "Loveseat": 15000, "Futon": 20000,
       "Dining": 30000, "Coffee": 15000, "End": 10000,
       "Rocking": 5000, "Club": 7000, "Cane": 600
       
       }
      # IMAGE 1
      img = Image.open("images/1.jpg")
      img = img.resize((500, 130), Image.LANCZOS)
      self.photoimg = ImageTk.PhotoImage(img)
      lbl_img = tk.Label(self.root, image=self.photoimg)
      lbl_img.place(x=0, y=0, width=500, height=140)
      
      # IMAGE 2
      img_1 = Image.open("images/2.jpg")
      img_1 = img_1.resize((500, 130), Image.LANCZOS)
      self.photoimg_1 = ImageTk.PhotoImage(img_1)
      lbl_img_1 = tk.Label(self.root, image=self.photoimg_1)
      lbl_img_1.place(x=500, y=0, width=500, height=140)
      
      # IMAGE 3
      img_2 = Image.open("images/3.jpg")
      img_2 = img_2.resize((500, 130), Image.LANCZOS)
      self.photoimg_2 = ImageTk.PhotoImage(img_2)
      lbl_img_2 = tk.Label(self.root, image=self.photoimg_2)
      lbl_img_2.place(x=1000, y=0, width=272, height=140)
      
    
      

    
      # Label Title
      lbl_title = tk.Label(
          self.root,
          text="SHARMA-BILLING",
          font=("times new roman", 35, "bold"),
          bg="#656B83",
          fg="white",
          anchor="center"
      )
      lbl_title.place(relx=0.5, y=140, anchor="n", width=1530, height=45)


      #MAIN FRAME

      Main_Frame=tk.Frame(self.root,bd=5,relief="groove",bg="white")
      Main_Frame.place(x=0,y=185,width=1530,height="620")

      #Customer LAbel frame
      Cust_frame=tk.LabelFrame(Main_Frame,text="Customer",font=("times new roman", 14, "bold"),
          
          fg="red",)
      Cust_frame.place(x=10,y=5,width=350,height=140)

      #customer data

     # Customer name
      self.lbl_name=tk.Label(Cust_frame,text="Name.",font=("times new roman",12,"bold"),bg="white")
      self.lbl_name.grid(row=0,column=0,padx=5,pady=2)
      
      self.entry_name=ttk.Entry(Cust_frame,font=("times new roman",12,"bold"),width=25,textvariable=self.customer_name)
      self.entry_name.grid(row=0,column=1)
     
      #mobile number
      self.lbl_mob=tk.Label(Cust_frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
      self.lbl_mob.grid(row=1,column=0,padx=5,pady=2) 
      self.entry_mob=ttk.Entry(Cust_frame,font=("times new roman",12,"bold"),width=25,textvariable=self.customer_mob)
      self.entry_mob.grid(row=1,column=1)
     
     # Customer email

      self.lbl_email=tk.Label(Cust_frame,text="Email-id.",font=("times new roman",12,"bold"),bg="white")
      self.lbl_email.grid(row=2,column=0,padx=5,pady=2)
      
      self.entry_id=ttk.Entry(Cust_frame,font=("times new roman",12,"bold"),width=25,textvariable=self.customer_email)
      self.entry_id.grid(row=2,column=1)



      # Product frame

      Prod_frame=tk.LabelFrame(Main_Frame,text="Product",font=("times new roman", 14, "bold"),
          
          fg="red",)
      Prod_frame.place(x=370,y=5,width=500,height=140)

      # Select Categories

      self.lbl_catgr=tk.Label(Prod_frame,text="Select-Categories",font=("arial",12,"bold"),bg="white")
      self.lbl_catgr.grid(row=0,column=0,padx=5,pady=2)

      self.combo_catgr = ttk.Combobox(Prod_frame, font=("arial", 12, "bold"), width=13, state="readonly")
      self.combo_catgr['values'] = ["Select-option"] + list(self.categories.keys())
      self.combo_catgr.current(0)  # Set default value to "Select"
      self.combo_catgr.grid(row=0, column=1, sticky="W",padx=2, pady=2)
      self.combo_catgr.bind("<<ComboboxSelected>>", self.update_subcategories)

      
      # Select Sub-Categories

      self.lbl_sub_catgr=tk.Label(Prod_frame,text="Select Sub-Categories",font=("arial",12,"bold"),bg="white")
      self.lbl_sub_catgr.grid(row=1,column=0,sticky="W",padx=2,pady=2)

      self.combo_sub_catgr=ttk.Combobox(Prod_frame,font=("arial",12,"bold"),width=13,state="readonly")
      self.combo_sub_catgr['values'] = list(self.sub_categories.keys())
      self.combo_sub_catgr.grid(row=1,column=1,sticky="W",padx=2,pady=2)
      self.combo_sub_catgr.bind("<<ComboboxSelected>>",self.update_product)
      

      # Select Product-Name

      self.lbl_prod_name=tk.Label(Prod_frame,text="Product-Name",font=("arial",12,"bold"),bg="white")
      self.lbl_prod_name.grid(row=2,column=0,sticky="W",padx=2,pady=2)

      self.combo_prod_name=ttk.Combobox(Prod_frame,font=("arial",12,"bold"),width=13,state="readonly")
      self.combo_prod_name['values'] = list(self.prices.keys())
      self.combo_prod_name.grid(row=2,column=1,sticky="W",padx=2,pady=2)
      self.combo_prod_name.bind("<<ComboboxSelected>>",self.update_price)
      
      # Select Price

      self.lbl_price=tk.Label(Prod_frame,text="Price",font=("arial",12,"bold"),bg="white")
      self.lbl_price.grid(row=0,column=3,sticky="W",padx=2,pady=2)
      self.price_var=tk.StringVar()
      self.combo_price=tk.Entry(Prod_frame,font=("arial",12,"bold"),bg="white",width=8,textvariable=self.price_var)
      self.combo_price.grid(row=0,column=4,sticky="W",padx=2,pady=2)
      
      # Select Quantity

      self.lbl_quant=tk.Label(Prod_frame,text="Quantity",font=("arial",12,"bold"),bg="white")
      self.lbl_quant.grid(row=1,column=3,sticky="W",padx=2,pady=2)
      self.quantity_var=tk.StringVar()
      self.combo_quant=ttk.Entry(Prod_frame,font=("arial",12,"bold"),width=8,textvariable=self.quantity_var)
      self.combo_quant.grid(row=1,column=4,sticky="W",padx=2,pady=2)


      # MIDDLE-FRAME

      Middle_frame=tk.LabelFrame(Main_Frame,bd=1)
      Middle_frame.place(x=0,y=150,width=870,height=150)

     # IMAGE 6
      img_6 = Image.open("images/6.jpg")
      img_6 = img_6.resize((500, 140), Image.LANCZOS)
      self.photoimg_6 = ImageTk.PhotoImage(img_6)
      lbl_img_6 = tk.Label(Middle_frame, image=self.photoimg_6)
      lbl_img_6.place(x=0, y=0, width=420, height=143)
    
     # IMAGE 4
      img_4 = Image.open("images/4.jpg")
      img_4 = img_4.resize((500, 140), Image.LANCZOS)
      self.photoimg_4 = ImageTk.PhotoImage(img_4)
      lbl_img_4 = tk.Label(Middle_frame, image=self.photoimg_4)
      lbl_img_4.place(x=420, y=0, width=450, height=143)
    






      # SEARCH-FRAME

      Search_frame=tk.LabelFrame(Main_Frame)
      Search_frame.place(x=883,y=10,width=320,height=75)

      self.lbl_search=tk.Label(Search_frame,text="Bill-No.",font=("arial",12,"bold"),fg="blue")
      self.lbl_search.grid(row=0,column=0,sticky="W",padx=2,pady=2)

      self.search_entry=ttk.Entry(Search_frame,font=("arial",12,"bold"),width=16)
      self.search_entry.grid(row=0,column=1,sticky="W",padx=2,pady=2)

       # 7 Search-Button

      self.btn_Search=tk.Button(Search_frame,text="Search",font=("arial",12,"bold"),fg="black",bg="white",cursor="hand2",bd=2)
      self.btn_Search.grid(row=0,column=2)

     







      # RIGHT FRAME FOR BILL AREA

      RightLabel=tk.LabelFrame(Main_Frame,text="Bill-Area",font=("times new roman",14,"bold"))
      RightLabel.place(x=872,y=45,width=380,height=400)

      #Scrool-BAR

      scroll_y=ttk.Scrollbar(RightLabel,orient="vertical")
      self.textarea=tk.Text(RightLabel,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("arial",12,"bold"))
      scroll_y.pack(side="right",fill="y")
      scroll_y.config(command=self.textarea.yview)
      self.textarea.pack(fill="both",expand=1)


     # BILL AREA-Header
      self.textarea.insert(tk.END,f"\n{'SHARMA-BILLING':^30}\n")
      self.textarea.insert(tk.END,f"\nBill No.:{self.bill_number}")
      self.textarea.insert(tk.END,f"\nCustomer Name:{self.customer_name.get()}")
      self.textarea.insert(tk.END,f"\n Mobile No.:{self.customer_mob.get()}")
      self.textarea.insert(tk.END,f"\n Email:{self.customer_email.get()}")
      self.textarea.insert(tk.END,"\n"+"-"*50)
      self.textarea.insert(tk.END,f"\n{'Product':<20}{'Qty':<10}{'Price'}")
      self.textarea.insert(tk.END,"\n"+"-"*50)




      # Govt tax area label

      Bill_counter=tk.LabelFrame(Main_Frame,text="Bill-Counter",font=("times new roman", 14, "bold"),fg="red")
      Bill_counter.place(x=0,y=300,width=300,height=140)


      # Sub-Total 

      self.lbl_sub=tk.Label(Bill_counter,text="Sub-Total",font=("arial",12,"bold"),bg="white")
      self.lbl_sub.grid(row=0,column=0,sticky="W",padx=2,pady=2)

      self.sub_entry=ttk.Entry(Bill_counter,font=("arial",12,"bold"),width=15)
      self.sub_entry.grid(row=0,column=1,sticky="W",padx=2,pady=2)
      
      # Govt. TAX

      self.lbl_govt=tk.Label(Bill_counter,text="GOVT-TAX",font=("arial",12,"bold"),bg="white")
      self.lbl_govt.grid(row=1,column=0,sticky="W",padx=2,pady=2)

      self.gov_entry=ttk.Entry(Bill_counter,font=("arial",12,"bold"),width=15)
      self.gov_entry.grid(row=1,column=1,sticky="W",padx=2,pady=2)
      
      # Sub-Total 

      self.lbl_total=tk.Label(Bill_counter,text="TOTAL",font=("arial",12,"bold"),bg="white")
      self.lbl_total.grid(row=2,column=0,sticky="W",padx=2,pady=2)

      self.total_entry=ttk.Entry(Bill_counter,font=("arial",12,"bold"),width=15)
      self.total_entry.grid(row=2,column=1,sticky="W",padx=2,pady=2)



     

      #bottom corner Label

      Exit=tk.LabelFrame(Main_Frame,text="System-Options",font=("times new roman", 14, "bold"),fg="red",)
      Exit.place(x=312,y=300,width=550,height=147)

      # Buttons

      # 1 Add to cart

      self.btn_ATC=tk.Button(Exit,text="ADD-TO-CART",font=("arial",16,"bold"),fg="black",bd=10,cursor="hand2",command=self.add_to_cart)
      self.btn_ATC.grid(row=0,column=0)
      
      # 2 Generate Bill

      self.btn_GC=tk.Button(Exit,text="GENERATE-BILL",font=("arial",16,"bold"),fg="black",bd=10,cursor="hand2")
      self.btn_GC.grid(row=0,column=1)
      
      # 3 SAVE-BILL

      self.btn_BC=tk.Button(Exit,text="SAVE-BILL",font=("arial",16,"bold"),fg="black",bd=10,cursor="hand2")
      self.btn_BC.grid(row=0,column=2)
      

      # 4 PRINT-BILL

      self.btn_PC=tk.Button(Exit,text="PRINT-BILL",font=("arial",16,"bold"),fg="black",bd=10,cursor="hand2")
      self.btn_PC.grid(row=1,column=0)
     
     
       # 5 CLEAR-BILL

      self.btn_CB=tk.Button(Exit,text="CLEAR-BILL",font=("arial",16,"bold"),fg="black",bd=10,cursor="hand2",width=10)
      self.btn_CB.grid(row=1,column=1)
     
      # 6 EXIT

      self.btn_exit=tk.Button(Exit,text="EXIT",font=("arial",16,"bold"),fg="black",bd=10,cursor="hand2",width=5)
      self.btn_exit.grid(row=1,column=2)
     
      # Bind functions to buttons
      self.btn_ATC.config(command=self.add_to_cart)
      self.btn_GC.config(command=self.generate_bill)
      self.btn_BC.config(command=self.save_bill)
      self.btn_PC.config(command=self.print_bill)
      self.btn_CB.config(command=self.clear_bill)
      self.btn_exit.config(command=self.exit_app)


  
   
    # Function to update subcategories based on selected category
   def update_subcategories(self, event):
        selected_category = self.combo_catgr.get()
        if selected_category in self.categories:
            self.combo_sub_catgr['values'] = self.categories[selected_category]
            self.combo_sub_catgr.current(0)  # Automatically select first subcategory
            self.update_product(None)  # Update the product combobox based on the first subcategory
        else:
            self.combo_sub_catgr['values'] = []
            self.combo_prod_name['values'] = []
            self.combo_price.delete(0, tk.END)

    # Function to update product names based on subcategory
   def update_product(self, event):
        selected_subcategory = self.combo_sub_catgr.get()
        if selected_subcategory in self.sub_categories:
            self.combo_prod_name['values'] = self.sub_categories[selected_subcategory]
            self.combo_prod_name.current(0)
            # Automatically update the price for the first product
            self.update_price(None)
        else:
            self.combo_prod_name['values'] = []
            self.combo_price.delete(0, tk.END)

    # Function to update price based on product name
   def update_price(self, event):
        selected_product = self.combo_prod_name.get()
        if selected_product in self.prices:
            self.price_var.set(self.prices[selected_product])
        else:
            self.price_var.set('')    

  # function to generate bill number
   def generate_bill_no(self):
       return str(random.randint(1000,9999))
   
 # Function to update the bill area with customer details
  
   def update_bill_area(self):
    self.textarea.delete('1.0', tk.END)
    self.textarea.insert(tk.END, f"\n{'SHARMA-BILLING':^30}\n")
    self.textarea.insert(tk.END, f"\nBill No.: {self.bill_number}")
    self.textarea.insert(tk.END, f"\nCustomer Name: {self.customer_name.get()}")
    self.textarea.insert(tk.END, f"\nMobile No.: {self.customer_mob.get()}")
    self.textarea.insert(tk.END, f"\nEmail: {self.customer_email.get()}")
    self.textarea.insert(tk.END, "\n" + "-" * 50)
    self.textarea.insert(tk.END, f"\n{'Product':<20}{'Qty':<10}{'Price'}")
    self.textarea.insert(tk.END, "\n" + "-" * 50)
    
    sub_total = 0
    for product_name, quantity, price in self.product_list:
        self.textarea.insert(tk.END, f"\n{product_name:<20}{quantity:<10}{price}")
        sub_total += price

    # Update subtotal and total
    self.sub_entry.delete(0, tk.END)
    self.sub_entry.insert(0, str(sub_total))
    tax = sub_total * 0.01  # Example tax calculation (1% of subtotal)
    self.gov_entry.delete(0, tk.END)
    self.gov_entry.insert(0, str(tax))
    total = sub_total + tax
    self.total_entry.delete(0, tk.END)
    self.total_entry.insert(0, str(total))


   
   #function to add items to the cart
   
   def add_to_cart(self):
    product_name = self.combo_prod_name.get()
    quantity = self.combo_quant.get()
    
    if quantity.isdigit() and int(quantity) > 0:
        price = self.prices.get(product_name, 0) * int(quantity)
        self.product_list.append((product_name, quantity, price))
        self.update_bill_area()  # Update the bill area with the new product list
    else:
        # Optional: Show a message if quantity is invalid
        tk.messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity.")
   


   def generate_bill(self):
        self.update_bill_area()
        tk.messagebox.showinfo("Success", "Bill Generated Successfully")

   def save_bill(self):
        self.update_bill_area()
        bill_content = self.textarea.get('1.0', tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(bill_content)
            tk.messagebox.showinfo("Success", "Bill Saved Successfully")

   def print_bill(self):
        self.update_bill_area()
        tk.messagebox.showinfo("Success", "Bill Sent to Printer")

   def clear_bill(self):
        self.product_list = []
        self.customer_name.set("")
        self.customer_mob.set("")
        self.customer_email.set("")
        self.combo_catgr.set("Select-option")
        self.combo_sub_catgr.set("")
        self.combo_prod_name.set("")
        self.combo_price.delete(0, tk.END)
        self.combo_quant.delete(0, tk.END)
        self.sub_entry.delete(0, tk.END)
        self.gov_entry.delete(0, tk.END)
        self.total_entry.delete(0, tk.END)
        self.textarea.delete('1.0', tk.END)
        self.textarea.insert(tk.END, f"\n{'SHARMA-BILLING':^30}\n")
        self.textarea.insert(tk.END, f"\nBill No.: {self.bill_number}")
        self.textarea.insert(tk.END, f"\nCustomer Name: {self.customer_name.get()}")
        self.textarea.insert(tk.END, f"\nMobile No.: {self.customer_mob.get()}")
        self.textarea.insert(tk.END, f"\nEmail: {self.customer_email.get()}")
        self.textarea.insert(tk.END, "\n" + "-" * 50)
        self.textarea.insert(tk.END, f"\n{'Product':<20}{'Qty':<10}{'Price'}")
        self.textarea.insert(tk.END, "\n" + "-" * 50)

   def exit_app(self):
        self.root.destroy()







 
 
 
 
 
 
 
 
 
    


      
      








if __name__ == '__main__':
   root = tk.Tk()
   obj = Bill_App(root)
   root.mainloop()
