from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk

root = Tk()

root.title('CRUD Application')

#icon

icon = PhotoImage(file='C:/Users/dharshan/Desktop/git/tkinter-crud-application/images/—Pngtree—3d cute smile emoji_5858820.png')
root.iconphoto(True,icon)

#Functions

def submit_record():

    if not (first_name.get() and last_name.get() and address.get() and city.get() and state.get() and zipcode.get()):

        messagebox.showerror('Error','All fields are required')
        return
    
    if not zipcode.get().isdigit():

        messagebox.showerror('Error','ZIP code must be a number')
        return
    
    conn = sqlite3.connect("tkinter-crud-application/tkldb.db")

    query = conn.cursor()

    query.execute("""CREATE TABLE IF NOT EXISTS addresses(
                    first_name text,
                    last_name text,
                    address text,
                    city text,
                    state text,
                    zipcode integer
                    )""")

    query.execute("INSERT INTO addresses VALUES (:fn,:ln,:addr,:city,:state,:zipcode)",
                {
                    'fn':first_name.get(),
                    'ln':last_name.get(),
                    'addr':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zipcode':zipcode.get()
                })
        
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

    conn.commit()

    conn.close()

def view_record():

    conn = sqlite3.connect("tkinter-crud-application/tkldb.db")

    query = conn.cursor()

    query.execute("SELECT rowid, * FROM addresses")
    row = query.fetchall()

    data = ''
    for r in row:
        data += str(r[0]) +'\t'+r[1] +' '+ r[2] +'\t\t'+ r[4] +'\n'

    view_data = Label(root,text=data)
    view_data.grid(row=11,column=0,columnspan=2)

    conn.commit()

    conn.close()
    

def delete_record():

    if not select_id.get().isdigit():
        
        messagebox.showerror('Error','ID must be a number')
        return
    
    conn = sqlite3.connect("tkinter-crud-application/tkldb.db")

    query = conn.cursor()

    query.execute("DELETE FROM addresses WHERE rowid = (?)",(select_id.get()))

    conn.commit()

    conn.close()

    select_id.delete(0,END)
    

def edit_record():
    global edit
    edit = Tk()
    edit.title("Update record")

    if not select_id.get().isdigit():
        
        messagebox.showerror('Error','ID must be a number')
        return
    
    conn = sqlite3.connect("tkinter-crud-application/tkldb.db")

    query = conn.cursor()

    first_name_label_edit = Label(edit,text="First name")
    first_name_label_edit.grid(row=0,column=0)
    last_name_label_edit = Label(edit,text="Last name")
    last_name_label_edit.grid(row=1,column=0)
    address_label_edit = Label(edit,text="Address")
    address_label_edit.grid(row=2,column=0)
    city_label_edit = Label(edit,text="City")
    city_label_edit.grid(row=3,column=0)
    state_label_edit = Label(edit,text="State")
    state_label_edit.grid(row=4,column=0)
    zipcode_label_edit = Label(edit,text="Zip code")
    zipcode_label_edit.grid(row=5,column=0)

    global first_name_edit,last_name_edit , address_edit , city_edit, state_edit,zipcode_edit

    first_name_edit = Entry(edit,width=30)
    first_name_edit.grid(row=0,column=1,columnspan=2,padx=10,pady=(10,5))
    last_name_edit = Entry(edit,width=30)
    last_name_edit.grid(row=1,column=1,columnspan=2,padx=10,pady=(10,5))
    address_edit = Entry(edit,width=30)
    address_edit.grid(row=2,column=1,columnspan=2,padx=10,pady=(10,5))
    city_edit = Entry(edit,width=30)
    city_edit.grid(row=3,column=1,columnspan=2,padx=10,pady=(10,5))
    state_edit = Entry(edit,width=30)
    state_edit.grid(row=4,column=1,columnspan=2,padx=10,pady=(10,5))
    zipcode_edit = Entry(edit,width=30)
    zipcode_edit.grid(row=5,column=1,columnspan=2,padx=10,pady=(10,5))


    query.execute("Select rowid, * from addresses where rowid = (?)",(select_id.get()))
    row = query.fetchall()

    for r in row:
        first_name_edit.insert(0,r[1])
        last_name_edit.insert(0,r[2])
        address_edit.insert(0,r[3])
        city_edit.insert(0,r[4])
        state_edit.insert(0,r[5])
        zipcode_edit.insert(0,r[6])



    Save_btn = Button(edit,text="Save",command=update_record)
    Save_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=110)

    conn.commit()

    conn.close()

    edit.mainloop()

def update_record():

    if not (first_name_edit.get() and last_name_edit.get() and address_edit.get() and city_edit.get() and state_edit.get() and zipcode_edit.get()):

        messagebox.showerror('Error','All fields are required')
        return

    if not zipcode_edit.get().isdigit():

        messagebox.showerror('Error','ZIP code must be a number')
        return

    conn = sqlite3.connect("tkinter-crud-application/tkldb.db")

    query = conn.cursor()

    query.execute("""UPDATE addresses SET 
                  first_name = :fn, 
                  last_name = :ln, 
                  address = :addr, 
                  city = :cy , 
                  state = :st , 
                  zipcode = :zc 
                  Where rowid = :rw""",{
                      
                      'fn': first_name_edit.get(),
                      'ln': last_name_edit.get(),
                      'addr': address_edit.get(),
                      'cy': city_edit.get(),
                      'st': state_edit.get(),
                      'zc': zipcode_edit.get(),
                      'rw': select_id.get()
                  })

    conn.commit()

    conn.close()

    select_id.delete(0,END)

    edit.destroy()
    

# Labels section

first_name_label = Label(root,text="First name")
first_name_label.grid(row=0,column=0)
last_name_label = Label(root,text="Last name")
last_name_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zip code")
zipcode_label.grid(row=5,column=0)

select_id_label = Label(root,text="Select Id")
select_id_label.grid(row=8,column=0)

#Entry section

first_name = Entry(root,width=30)
first_name.grid(row=0,column=1,columnspan=2,padx=10,pady=(10,5))
last_name = Entry(root,width=30)
last_name.grid(row=1,column=1,columnspan=2,padx=10,pady=(10,5))
address = Entry(root,width=30)
address.grid(row=2,column=1,columnspan=2,padx=10,pady=(10,5))
city = Entry(root,width=30)
city.grid(row=3,column=1,columnspan=2,padx=10,pady=(10,5))
state = Entry(root,width=30)
state.grid(row=4,column=1,columnspan=2,padx=10,pady=(10,5))
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,columnspan=2,padx=10,pady=(10,5))

select_id = Entry(root,width=30)
select_id.grid(row=8,column=1,columnspan=2,padx=10,pady=10)

#Buttons section

submit_btn = Button(root,text="Submit",command=submit_record)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=102)

view_btn = Button(root,text="View records",command=view_record)
view_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=89)

delete_btn = Button(root,text="Delete record",command=delete_record)
delete_btn.grid(row=9,column=0,columnspan=2,padx=10,pady=10,ipadx=85)

Update_btn = Button(root,text="Update record",command=edit_record)
Update_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=85)

root.mainloop()