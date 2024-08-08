from tkinter import *

from tkinter import messagebox


# Initialize root window
root = Tk()
root.geometry('800x730')
root.config(bg='lightgrey')
root.title('MY CONTACT BOOK')
root.resizable(0,0)


# making a list for saved contacts
contactlist = [
    ['Priyanka Chopra', '369854712', 'jonas@us.com', 'USA'],
    ['Aishwarya Rai', '521155222', 'aishwarya@bacchan.com', 'MUMBAI'],
    ['Vicky Kaushal', '58745246', 'katrina@kaushal.com', 'MUMBAI'],
    ['Rohit Saraf', '5846975', 'coffee@mismatch.com', 'JAIPUR'],
    ['Divyendu', '5647892', 'munna@bhaiya.com', 'MIRZAPUR'],
    ['Pankaj Tripathi', '89685320', 'bhaiya@mirzapur.com', 'MIRZAPUR'],
    ['Manoj Bajpayee', '98564785', 'bhaiyaajee@wassepur.com', 'WASEEPUR'],
    ['Sushmita Sen', '85967412', 'hello@gmail.com', 'MUMBAI']
]

# variables 
Name = StringVar()
Number = StringVar()
Email = StringVar()
Address = StringVar()
search_term = StringVar()

is_search = False
term = ""

# Creating frame
frame = Frame(root)
frame.pack(side=RIGHT)

# creating scrollbar
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="grey", width=30, height=15, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Function to get selected value
def Selected():
    if len(select.curselection()) == 0:
        status_label.config(text="Error: Please Select a Contact")
        return None
    else:
        return [int(i) for i in select.curselection()]

# Function to add new contact
def AddContact():
    global is_search
    is_search = False
    if Name.get() and Number.get() and Email.get() and Address.get():
        contactlist.append([Name.get(), Number.get(), Email.get(), Address.get()])
        Select_set()
        status_label.config(text="Successfully Added New Contact")
        EntryReset()
    else:
        status_label.config(text="Error: Please fill in all fields")

# Function to update contact
def UpdateDetail():
    index = Selected()
    if index is not None:
        if Name.get() and Number.get():
            for i in index:
                contactlist[i] = [Name.get(), Number.get(), Email.get(), Address.get()]
            Select_set()
            EntryReset()
            status_label.config(text="Successfully Updated Contact")
        else:
            status_label.config(text="Error: Please fill in Name and Number")
    else:
        status_label.config(text="Error: Please Select a Contact and Load Details First")

# Function to delete contact
def Delete_Entry():
    index = Selected()
    if index is not None and index:
        result = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this contact?")
        if result:  # If the user clicks "Yes", result will be True
            for i in sorted(index, reverse=True):
                if i < len(contactlist):  # Ensure the index is within the valid range
                    del contactlist[i]
            
            select.delete(0, END)  # Clear the Listbox
            for contact in contactlist:
                select.insert(END, f"{contact[0]}, {contact[1]}")  # Update the Listbox
            
            EntryReset()
            status_label.config(text="Successfully Deleted Contact")
        else:
            status_label.config(text="Deletion Cancelled")
    else:
        status_label.config(text="Error: Please select a Contact")

# Function to view contact details
def VIEW():
    index = Selected()
    if index is not None:
        NAME, NUMBER, EMAIL, ADDRESS = contactlist[index[0]]
        Name.set(NAME)
        Number.set(NUMBER)
        Email.set(EMAIL)
        Address.set(ADDRESS)
    else:
        status_label.config(text="Error: Please Select a Contact")

# Function to search contacts
def Search():
    global search_term, term, is_search
    is_search = True
    term = search_term.get().lower()
    select.delete(0, END)
    matches = []
    
    # Clear previous selections
    select.selection_clear(0, END)
    
    # Rebuild the Listbox with search results
    for idx, contact in enumerate(contactlist):
        if term in contact[0].lower() or term in contact[1]:
            select.insert(END, f"{contact[0]}, {contact[1]}")
            matches.append(contact)
    
    # Select the items in the Listbox that match the search term
    if matches:
        for match in matches:
            # Adjusting index for the updated list
            actual_index = contactlist.index(match)
            select.selection_set(actual_index)
        select.activate(0)  # Making first match is visible
        status_label.config(text="Search results displayed")
    else:
        status_label.config(text="No contacts found")



# Function to reset fields
def EntryReset():
    Name.set("")
    Number.set("")
    Email.set("")
    Address.set("")
    status_label.config(text="")
    search_term.set("")
    if(is_search):
        for contact in contactlist:
            select.insert(END, f"{contact[0]}, {contact[1]}")
            

# Function to update contact list
def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for contact in contactlist:
        select.insert(END, f"{contact[0]}, {contact[1]}")


Select_set()

# Define labels and entry widgets
Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='lightgrey').place(x=30, y=20)
Entry(root, textvariable=Name, width=20, font=8).place(x=200, y=30)

Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='lightgrey').place(x=30, y=70)
Entry(root, textvariable=Number,  width=20, font=8).place(x=200, y=80)

Label(root, text='Email', font=("Times new roman", 20, "bold"), bg='lightgrey').place(x=30, y=120)
Entry(root, textvariable=Email,  width=20, font=8).place(x=200, y=130)

Label(root, text='Address', font=("Times new roman", 20, "bold"), bg='lightgrey').place(x=30, y=170)
Entry(root, textvariable=Address,  width=20, font=8).place(x=200, y=180)

Label(root, text='Search', font=("Times new roman", 20, "bold"), bg='lightgrey').place(x=30, y=220)
Entry(root, textvariable=search_term,  width=20, font=8).place(x=200, y=230)

# creating buttons

Button(root, text="ADD", font='Helvetica 18 bold', bg='tan', command=AddContact, pady=5).place(x=50, y=270)
Button(root, text="UPDATE", font='Helvetica 18 bold', bg='tan', command=UpdateDetail,pady=5).place(x=50, y=340)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='tan', command=VIEW).place(x=50, y=410)
Button(root, text="SEARCH", font='Helvetica 18 bold', bg='tan', command=Search).place(x=50, y=475)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='tan', command=Delete_Entry,pady=5).place(x=50, y=545)
Button(root, text="RESET", font='Helvetica 18 bold', bg='tan', command=EntryReset).place(x=50, y=620)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=root.destroy).place(x=640, y=600)

# Status labels
status_label = Label(root, text="", font=("Times new roman", 14), bg='lightgrey', pady=10)
status_label.place(x=280, y=680)

# running main GUI window
root.mainloop()


