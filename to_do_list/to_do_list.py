from tkinter import *

root =  Tk()
root.title("My TO-DO-LIST")
root.geometry("400x650")
root.resizable(0,0)

# lists that stores tasks
task_list = []

#func to add task
def add():
    task = to_do_entry.get()
    to_do_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list_box.insert(END, task)


#func to delete task
def delete():
    global task_list
    task = str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        list_box.delete(ANCHOR)


#func to delete all tasks
def deleteAll():
    global task_list
    task_list.clear()
    with open("tasklist.txt", 'w') as taskfile:
        taskfile.write("")
    list_box.delete(0, END)


#func to update textfile
def openTo_do_file():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                list_box.insert(END, task)

    except:
        file=open('tasklist.txt','w')
        file.close()

#heading " MY TASKS"
heading =  Label(root, text="MY TASKS", font="arial 20 bold underline", fg="black")
heading.place(x=130,y=20)

# main frame

main_frame = Frame(root, width=400, height=50, bg ='white')
main_frame.place(x=0,y=180)

to_do = StringVar()
to_do_entry = Entry(main_frame, width=18, font = 'arial 20', bd=0)
to_do_entry.place(x=10,y=7)
to_do_entry.focus()  

#add button
button1 = Button(main_frame, text="ADD", font='arial 20 bold', width =6, bg = 'burlywood', fg='black',bd=1,command=add)
button1.place(x=300,y=0)

#list box frame and lists
list_frame = Frame(root, bd =3,width=700, height=280,bg = 'white')
list_frame.pack(pady = (230,0))

list_box = Listbox(list_frame, font=('arial',15),width=40,height=13,bg='grey', fg = 'white', cursor = 'hand2')
list_box.pack(side=RIGHT , fill = BOTH, padx=2)

#creating scroll bars

scroll = Scrollbar(list_frame)
scroll.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)

openTo_do_file()       

#delete  button
button2 = Button(root, text="DELETE", font='arial 12 bold', width =7, bg = 'lightgrey', fg='indianred',bd=3,command=delete)
button2.place(x=15,y=560)

# delete all button
button4 = Button(root, text="DELETE ALL", font='arial 12 bold', width =10, bg = 'lightgrey', fg='indianred',bd=3, command=deleteAll)
button4.place(x=105,y=560)


# save and exit button

button3 = Button(root, text="SAVE & EXIT", font='arial 12 bold', width =12, bg = 'lightgrey', fg='black',bd=5,command=exit)
button3.place(x=250,y=560)

# running main GUI loop
root.mainloop()


