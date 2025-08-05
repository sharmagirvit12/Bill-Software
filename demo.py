import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Bill_App:
   def __init__(self, root):
      self.root = root
      self.root.geometry("1530x800+0+0")
      self.root.title("Billing Software")
      
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
          text="SHARMA BILLING",
          font=("times new roman", 35, "bold"),
          bg="#656B83",
          fg="white",
          anchor="center"
      )
      lbl_title.place(relx=0.5, y=140, anchor="n", width=1530, height=45)

      # MAIN FRAME
      Main_Frame = tk.Frame(self.root, bd=5, relief="groove", bg="white")
      Main_Frame.place(x=0, y=185, width=1530, height="620")

      # Customer Label frame
      Cust_frame = tk.LabelFrame(Main_Frame, text="Customer", font=("times new roman", 14, "bold"),
                                 bg="white", fg="red")
      Cust_frame.place(x=10, y=5, width=350, height=140)

      # Customer data
      # Customer name
      self.lbl_name = tk.Label(Cust_frame, text="Name.", font=("times new roman", 12, "bold"), bg="white")
      self.lbl_name.grid(row=0, column=0, padx=5, pady=2)

      self.entry_name = ttk.Entry(Cust_frame, font=("times new roman", 12, "bold"), width=25)
      self.entry_name.grid(row=0, column=1)

      # Mobile number
      self.lbl_mob = tk.Label(Cust_frame, text="Mobile No.", font=("times new roman", 12, "bold"), bg="white")
      self.lbl_mob.grid(row=1, column=0, padx=5, pady=2)
      self.entry_mob = ttk.Entry(Cust_frame, font=("times new roman", 12, "bold"), width=25)
      self.entry_mob.grid(row=1, column=1)

      # Customer email
      self.lbl_email = tk.Label(Cust_frame, text="Email-id.", font=("times new roman", 12, "bold"), bg="white")
      self.lbl_email.grid(row=2, column=0, padx=5, pady=2)

      self.entry_id = ttk.Entry(Cust_frame, font=("times new roman", 12, "bold"), width=25)
      self.entry_id.grid(row=2, column=1)

      # Product frame
      Prod_frame = tk.LabelFrame(Main_Frame, text="Product", font=("times new roman", 14, "bold"),
                                 bg="white", fg="red")
      Prod_frame.place(x=370, y=5, width=500, height=140)

      # Select Categories
      self.lbl_catgr = tk.Label(Prod_frame, text="Select Categories", font=("arial", 12, "bold"), bg="white")
      self.lbl_catgr.grid(row=0, column=0, padx=5, pady=2, sticky="W")

      self.combo_catgr = ttk.Combobox(Prod_frame, font=("arial", 12, "bold"), width=18, state="readonly")
      self.combo_catgr.grid(row=0, column=1, padx=5, pady=2)

      # Select Sub-Categories
      self.lbl_sub_catgr = tk.Label(Prod_frame, text="Select Sub-Categories", font=("arial", 12, "bold"), bg="white")
      self.lbl_sub_catgr.grid(row=1, column=0, padx=5, pady=2, sticky="W")

      self.combo_sub_catgr = ttk.Combobox(Prod_frame, font=("arial", 12, "bold"), width=18, state="readonly")
      self.combo_sub_catgr.grid(row=1, column=1, padx=5, pady=2)

      # Select Product Name
      self.lbl_prod_name = tk.Label(Prod_frame, text="Product Name", font=("arial", 12, "bold"), bg="white")
      self.lbl_prod_name.grid(row=2, column=0, padx=5, pady=2, sticky="W")

      self.combo_prod_name = ttk.Combobox(Prod_frame, font=("arial", 12, "bold"), width=18, state="readonly")
      self.combo_prod_name.grid(row=2, column=1, padx=5, pady=2)

      # Price
      self.lbl_price = tk.Label(Prod_frame, text="Price", font=("arial", 12, "bold"), bg="white")
      self.lbl_price.grid(row=0, column=3, padx=5, pady=2, sticky="W")

      self.combo_price = ttk.Combobox(Prod_frame, font=("arial", 12, "bold"), width=10, state="readonly")
      self.combo_price.grid(row=0, column=4, padx=5, pady=2)

      # Quantity
      self.lbl_quant = tk.Label(Prod_frame, text="Quantity", font=("arial", 12, "bold"), bg="white")
      self.lbl_quant.grid(row=1, column=3, padx=5, pady=2, sticky="W")

      self.combo_quant = ttk.Entry(Prod_frame, font=("arial", 12, "bold"), width=10)
      self.combo_quant.grid(row=1, column=4, padx=5, pady=2)


if __name__ == '__main__':
   root = tk.Tk()
   obj = Bill_App(root)
   root.mainloop()
