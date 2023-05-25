import tkinter as tk
from tkinter import ttk
import sqlite3


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
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Price", "Description"))
        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.tree.heading("#0", text="Name")
        self.tree.heading("#1", text="Price")
        self.tree.heading("#2", text="administrator")
        self.tree.heading("#3", text="status")

        # create buttons
        self.btn_add = ttk.Button(self, text="Add")
        self.btn_add.grid(row=2, column=0, padx=5, pady=5, sticky="we")
        self.btn_delete = ttk.Button(self, text="Delete")
        self.btn_delete.grid(row=2, column=2, padx=5, pady=5, sticky="we")

        # create label for messages
        self.lbl_message = ttk.Label(self, text="")
        self.lbl_message.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # bind buttons
        self.btn_add.bind("<Button-1>", self.add)
        self.btn_delete.bind("<Button-1>", self.delete)

        # load data
        self.load_data()

    def load_data(self):
        # delete previous data
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)


        #join the tables House and Seller by using the table SoldHouse that has the id of the house and the id of the seller
        query = "SELECT House.type, House.price, Seller.first_name, House.status FROM House INNER JOIN Seller ON House.seller_id = Seller.id"
        db_rows = cur.execute(query).fetchall()

        # insert data
        for row in db_rows:
            self.tree.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3]))

    def add(self, event):

        # create a new window
        self.new_window = tk.Toplevel(self)
        self.app = Add(self.new_window)

        # bind button
        self.app.btn_add.bind("<Button-1>", self.app.add)

    def delete(self, event):

        # create a new window
        self.new_window = tk.Toplevel(self)
        self.app = Delete(self.new_window)

        # bind button
        self.app.btn_delete.bind("<Button-1>", self.app.delete)




# test login window

if __name__ == "__main__":
    app = Login()
    app.mainloop()





