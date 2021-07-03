from tkinter import *
import sqlite3

root = Tk()
root.title('Databases with Tkinter')
root.geometry("400x400")

# databases
# creating and connecting database

conn = sqlite3.connect('address_book.db')
# create cursor
c = conn.cursor()
# create table
c.execute("""CREATE TABLE addresses (
first_name text,
last_name text,
address text,
city text, 
state text,
zipcode integer)
""")

# save changes
conn.commit()
# close database
conn.close()

root.mainloop()
