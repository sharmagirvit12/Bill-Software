
README.md
SHARMA-BILLING: A GUI-Based Billing Software
This is a graphical user interface (GUI) based billing software created using the Tkinter library in Python. The application allows users to generate bills for various products, manage customer details, and calculate totals with taxes.

Features
Customer Management: Easily add customer details such as name, mobile number, and email.

Product Selection: A multi-level selection system for products, including categories, sub-categories, and individual product names.

Dynamic Pricing: Product prices are automatically fetched and displayed upon selection.

Bill Generation: Generates a detailed bill with product-wise quantity and price, sub-total, and government tax.

Bill Actions: Functionality to save, print, and clear the generated bill.

Random Bill Numbers: Each new bill is assigned a unique, randomly generated bill number.

Prerequisites
To run this application, you need to have the following Python libraries installed:

Tkinter: This is a standard Python library, so it's likely already installed.

Pillow (PIL): Used for handling images in the GUI.
How to Use the Application
Enter Customer Details: On the left side of the main window, fill in the customer's name, mobile number, and email.

Select Products: In the "Product" section, use the dropdown menus to select the Category, Sub-Category, and Product-Name.

Add Quantity: Enter the desired quantity for the selected product. The price will be automatically displayed.

Add to Cart: Click the ADD-TO-CART button to add the item to the bill. You can repeat this process for multiple products.

Generate Bill: Once you have added all products, click the GENERATE-BILL button. This will update the bill area with all items, the sub-total, tax, and final total.

Save/Print: Use the SAVE-BILL button to save the bill as a text file or PRINT-BILL to simulate sending it to a printer.

Clear Bill: To start a new bill, click the CLEAR-BILL button.

Project Structure (Code Overview)
The core of this application is the Bill_App class, which handles the entire GUI and its functionality.

__init__(self, root): The constructor sets up the main window, GUI elements, and variables. It initializes the main frames, labels, entry fields, and buttons.

Variables: The application uses StringVar to manage customer details and a dictionary-based structure to hold product categories, sub-categories, and prices.

Image Handling: The Pillow library is used to open and resize images for the application's header.

Functionality: Methods like update_subcategories, update_product, and update_price handle the dynamic changes in the dropdown menus.

Bill Logic: The add_to_cart and update_bill_area methods are responsible for calculating totals, applying taxes, and populating the bill area.

Action Buttons: The buttons are bound to methods like generate_bill, save_bill, print_bill, clear_bill, and exit_app, each performing its respective task.







