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
        if username == "admin" and password == "admin":
            # show the main window
            self.destroy()
            main = Main()
            main.mainloop()
        else:
            self.lbl_message["text"] = "Username or password incorrect"

#tinker main window
# show a crud window with the database "Tie-House.db"
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("House selling machine")
        self.geometry("800x600")   
        self.resizable(False, False)
        self.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):
        # create labels
        self.lbl_title = ttk.Label(self, text="House selling machine")
        self.lbl_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # create treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Price", "Administrator","status", "Update", "Delete"))
        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Price")
        self.tree.heading("#3", text="Administrator")
        self.tree.heading("#4", text="Status")
        self.tree.heading("#5", text="Update")
        self.tree.heading("#6", text="Delete")





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

        # Load images
        update_img = ImageTk.PhotoImage(Image.open(r"tie-venta-casas\icons\update_icon.png"))
        delete_img = ImageTk.PhotoImage(Image.open(r"tie-venta-casas\icons\delete_icon.png"))

        # Insert data
        for row_id, row in enumerate(db_rows):
            house_id, house_type, price, seller_first_name, status = row
            update_button = ttk.Button(self.tree, image=update_img, command=lambda row=row: self.update(row))
            delete_button = ttk.Button(self.tree, image=delete_img, command=lambda row=row: self.delete(row))
            update_button.image = update_img  # Store a reference to avoid garbage collection
            delete_button.image = delete_img  # Store a reference to avoid garbage collection
            self.tree.insert("", tk.END, values=(house_id, house_type, price, seller_first_name, status, update_button, delete_button))

        # Adjust column widths to accommodate the headings
        self.tree.column("#0", width=80)
        self.tree.column("#1", width=80)
        self.tree.column("#2", width=80)
        self.tree.column("#3", width=80)
        self.tree.column("#4", width=80)
        self.tree.column("#5", width=80)
        self.tree.column("#6", width=80)

    def delete(self, event):
        # get id
        selected_item = self.tree.selection()[0]
        id = self.tree.item(selected_item, "text")

        # delete from database
        query = "DELETE FROM House WHERE id=?"
        cur.execute(query, (id,))
        con.commit()

        # show message
        self.lbl_message["text"] = "Deleted successfully"

        # update data
        self.load_data()

    def update(self, event):
        # get id
        selected_item = self.tree.selection()[0]
        id = self.tree.item(selected_item, "text")

        # create update window
        update_window = Update(id)

        # bind button
        update_window.btn_update.bind("<Button-1>", self.update_row)

    def update_row(self, event):
        # get id
        id = self.tree.item(self.tree.selection()[0], "text")

        # get values
        name = self.ent_name.get()
        price = self.ent_price.get()
        description = self.ent_description.get()

        # update database
        query = "UPDATE House SET type=?, price=?, description=? WHERE id=?"
        cur.execute(query, (name, price, description, id))
        con.commit()

        # show message
        self.lbl_message["text"] = "Updated successfully"

        # update data
        self.load_data()

#tinker update window
# show a window to update a row in the database
class Update(tk.Toplevel):
    def __init__(self, id):
        super().__init__()
        self.title("Update House")
        self.geometry("400x250")
        self.resizable(False, False)
        self.configure(bg="white")

        self.id = id

        self.create_widgets()

    def create_widgets(self):
        # get data of the selected row
        query = "SELECT * FROM House WHERE id=?"
        result = cur.execute(query, (self.id,)).fetchone()

        # create labels
        self.lbl_name = ttk.Label(self, text="Name:")
        self.lbl_name.grid(row=0, column=0, padx=5, pady=5)
        self.lbl_price = ttk.Label(self, text="Price:")
        self.lbl_price.grid(row=1, column=0, padx=5, pady=5)
        self.lbl_description = ttk.Label(self, text="Description:")
        self.lbl_description.grid(row=2, column=0, padx=5, pady=5)

        # create entry
        self.ent_name = ttk.Entry(self)
        self.ent_name.grid(row=0, column=1, padx=5, pady=5)
        self.ent_name.insert(0, result[1])
        self.ent_price = ttk.Entry(self)
        self.ent_price.grid(row=1, column=1, padx=5, pady=5)
        self.ent_price.insert(0, result[2])
        self.ent_description = ttk.Entry(self)
        self.ent_description.grid(row=2, column=1, padx=5, pady=5)
        self.ent_description.insert(0, result[3])

        # create button
        self.btn_update = ttk.Button(self, text="Update")
        self.btn_update.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")


# test login window

if __name__ == "__main__":
    app = Main()
    app.mainloop()





