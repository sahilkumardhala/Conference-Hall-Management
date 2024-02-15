# from tkinter import *

# root =Tk()
# root.title("simran")

# bt1 = Button(root, width=20,height=10, text="stop", command=root.destroy)
# # bt1.pack()

# root.mainloop()

import sqlite3

db = sqlite3.connect('example.db')

c = db.cursor()
try:
    c.execute('''CREATE TABLE records(
                NAME text    NOT NULL,
                HALL text    NOT NULL,
                CHAIRS integer  NOT NULL,
                PROJECTOR text  NOT NULL,
                HEADCOUNT integer   NOT NULL,
                TOTALCOST integer)''')
    
except Exception as e:
    print(e)
    # print("Table Succesfully Created")