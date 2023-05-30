import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image


# import database
db = "Tie-House.db"
con = sqlite3.connect(db)
cur = con.cursor()



# tkinker login window
# from database "Tie-House.db" get users and passwords and compare them with the ones in the login window
# if they match, send a welcome message
# else, show an error message
class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x150")
        self.resizable(False, False)
        self.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):
        # create labels
        self.lbl_username = ttk.Label(self, text="Username:")
        self.lbl_username.grid(row=0, column=0, padx=5, pady=5)
        self.lbl_password = ttk.Label(self, text="Password:")
        self.lbl_password.grid(row=1, column=0, padx=5, pady=5)

        # create entry
        self.ent_username = ttk.Entry(self)
        self.ent_username.grid(row=0, column=1, padx=5, pady=5)
        self.ent_password = ttk.Entry(self, show="*")
        self.ent_password.grid(row=1, column=1, padx=5, pady=5)

        # create button
        self.btn_login = ttk.Button(self, text="Login")
        self.btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # create label for messages
        self.lbl_message = ttk.Label(self, text="")
        self.lbl_message.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # bind button
        self.btn_login.bind("<Button-1>", self.login)

    def login(self, event):
        # get username and password
        username = self.ent_username.get()
        password = self.ent_password.get()

        # get users and passwords from database
        # compare them with the ones in the login window
        # if they match, send a welcome message
        # else, show an error message
        if (username == "admin" and password == "admin") or (username == "user" and password == "user"):
            # show the main window
            self.destroy()
            main = Main()
            if username == "admin":
                main.set_user_admin()
            else:
                main.set_user_user()
            main.mainloop()
        else:
            self.lbl_message["text"] = "Username or password incorrect"

#tinker main window
# show a crud window with the database "Tie-House.db"
class Main(tk.Tk): 
    user = ""   
    def __init__(self):
        super().__init__()
        self.title("House selling machine")
        self.geometry("800x600")   
        self.resizable(False, False)
        self.configure(bg="white")


    def set_user_admin(self):
        self.user = "admin"
        self.create_widgets()
    
    def set_user_user(self):
        self.user = "user"
        self.create_widgets()

    def create_widgets(self):
        # create labels
        self.lbl_title = ttk.Label(self, text="House selling machine")
        self.lbl_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # create treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Price", "Administrator","status"))
        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Price")
        self.tree.heading("#3", text="Administrator")
        self.tree.heading("#4", text="Status")

        # if user is admin
        if self.user == "admin":
            # create delete label
            self.lbl_delete = ttk.Label(self, text="Enter ID to delete:")
            self.lbl_delete.grid(row=2, column=0, padx=5, pady=5)

            # create delete entry
            self.ent_delete = ttk.Entry(self)
            self.ent_delete.grid(row=2, column=1, padx=5, pady=5)

            # create delete button
            self.btn_delete = ttk.Button(self, text="Delete", command=self.delete)
            self.btn_delete.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

            # create add label
            self.lbl_name = ttk.Label(self, text="Name:")
            self.lbl_name.grid(row=4, column=0, padx=5, pady=5)
            self.lbl_price = ttk.Label(self, text="Price:")
            self.lbl_price.grid(row=5, column=0, padx=5, pady=5)
            self.lbl_admin = ttk.Label(self, text="Administrator:")
            self.lbl_admin.grid(row=6, column=0, padx=5, pady=5)
            self.lbl_status = ttk.Label(self, text="Status:")
            self.lbl_status.grid(row=7, column=0, padx=5, pady=5)

            query = "SELECT * FROM Seller"
            cur.execute(query)
            sellers = cur.fetchall()
            self.sellers = []
            for seller in sellers:
                self.sellers.append((seller[0], seller[1]))  # Store both ID and name as a tuple

            # create add entry
            self.ent_name = ttk.Entry(self)
            self.ent_name.grid(row=4, column=1, padx=5, pady=5)
            self.ent_price = ttk.Entry(self)
            self.ent_price.grid(row=5, column=1, padx=5, pady=5)
            # display seller names in combobox and bind seller IDs to them
            self.ent_admin = ttk.Combobox(self, values=[seller[1] for seller in sellers], state="readonly")
            self.ent_admin.grid(row=6, column=1, padx=5, pady=5)
            self.ent_admin.current(0)
            self.ent_status = ttk.Combobox(self, values=["available", "sold"], state="readonly")
            self.ent_status.grid(row=7, column=1, padx=5, pady=5)
            self.ent_status.insert(0, "available")

            # create add button
            self.btn_add = ttk.Button(self, text="Add", command=self.add)
            self.btn_add.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # if user is user
        if self.user == "user":
            # create sell label
            self.lbl_sell = ttk.Label(self, text="Enter ID to sell:")
            self.lbl_sell.grid(row=2, column=0, padx=5, pady=5)

            # create sell entry
            self.ent_sell = ttk.Entry(self)
            self.ent_sell.grid(row=2, column=1, padx=5, pady=5)

            # create sell button
            self.btn_sell = ttk.Button(self, text="Sell", command=self.sell)
            self.btn_sell.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

            
        # load data
        self.load_data()

    def load_data(self):
        # Delete previous data
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Join the tables House and Seller by using the table SoldHouse that has the id of the house and the id of the seller
        query = "SELECT House.Id, House.type, House.price, Seller.first_name, House.status FROM House INNER JOIN Seller ON House.seller_id = Seller.id"
        db_rows = cur.execute(query).fetchall()

        # Insert data
        for row_id, row in enumerate(db_rows):
            house_id, house_type, price, seller_first_name, status = row
            self.tree.insert("", tk.END, values=(house_id, house_type, price, seller_first_name, status))

        # Adjust column widths to accommodate the headings
        self.tree.column("#0", width=80, anchor="center")
        self.tree.column("#1", width=80, anchor="center")
        self.tree.column("#2", width=80, anchor="center")
        self.tree.column("#3", width=80, anchor="center")
        self.tree.column("#4", width=80, anchor="center")


    def delete(self):
        # get id
        id = self.ent_delete.get()

        # delete from database
        query = "DELETE FROM House WHERE id=?"
        cur.execute(query, (id,))
        con.commit()

        # load data
        self.load_data()

    def add(self):
        # get values
        name = self.ent_name.get()
        price = self.ent_price.get()
        admin_name = self.ent_admin.get()
        status = self.ent_status.get()

        # retrieve the seller id based on the selected name
        seller_id = None
        for seller in self.sellers:
            if seller[1] == admin_name:
                seller_id = seller[0]
                break

        if seller_id is not None:
            # insert into the database
            query = "INSERT INTO House (type, price, seller_id, status) VALUES (?, ?, ?, ?)"
            cur.execute(query, (name, price, seller_id, status))
            con.commit()

            # load data
            self.load_data()

            # clear the input fields
            self.ent_name.delete(0, tk.END)
            self.ent_price.delete(0, tk.END)
            self.ent_admin.current(0)
            self.ent_status.delete(0, tk.END)
        else:
            # handle the case when seller_id is not found
            print("Error: Seller ID not found for selected name.")

    def sell(self):
        # get id
        id = self.ent_sell.get()

        # update database
        query = "UPDATE House SET status='sold' WHERE id=?"
        cur.execute(query, (id,))
        con.commit()

        # load data
        self.load_data()

# test login window

if __name__ == "__main__":
    app = Login()
    app.mainloop()





