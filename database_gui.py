from tkinter import *
import sqlite3

root = Tk()
root.title('DATABASE GUI')
root.geometry("550x650")

conn = sqlite3.connect('address_book.db')
c = conn.cursor()


# button function
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # insert into tables
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': 'f_name.get()',
                  'l_name': 'l_name.get()',
                  'address': 'address.get()',
                  'city': 'city.get()',
                  'state': 'state.get()',
                  'zipcode': 'zipcode.get()'
              })

    conn.commit()
    conn.close()
    # Clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records[0]:
        print_records += str(record) + "\n"
    query_label = Label(root, text=print_records).grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


# create textboxes
f_name = Entry(root, width=30).grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30).grid(row=1, column=1, padx=20)
address = Entry(root, width=30).grid(row=2, column=1, padx=20)
city = Entry(root, width=30).grid(row=3, column=1, padx=20)
state = Entry(root, width=30).grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30).grid(row=5, column=1, padx=20)
# creating textbox labels
f_name_label = Label(root, text="First name").grid(row=0, column=0)
l_name_label = Label(root, text="Last name").grid(row=1, column=0)
address_label = Label(root, text="Address").grid(row=2, column=0)
city_label = Label(root, text="City").grid(row=3, column=0)
state_label = Label(root, text="State").grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode").grid(row=5, column=0)
# submit button
submit_btn = Button(root, text="ADD RECORD TO DATABASE", command=submit, bg="orange", fg="white")
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
# query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()
