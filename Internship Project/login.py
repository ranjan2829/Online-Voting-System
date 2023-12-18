from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Login')
root.geometry('1000x700+300+200')
root.configure(bg="#fff")

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello MotherFucker!',bg='#fff', font=('Calibri (Body)', 50, 'bold')).pack(expand=True)
        screen.mainloop()

    elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid", "invalid username and password")

    elif password!="1234":
        messagebox.showerror("Invalid", "invalid username and password")



root1 = Frame(root,width=600,height=80,bg="white")
root1.place(x=500,y=20)

head = Label(root1, text='ONLINE VOTING SYSTEM', fg='black', bg="white", font=('Areal',30,'bold'))
head.place(x=40,y=0)

Frame(root, width=1500, height=2,bg='black').place(x=40, y=70)
Frame(root, width=1500, height=2,bg='black').place(x=40, y=750)

img1 = PhotoImage(file="Vote12.png")
Label(root,image=img1,bg='white').place(x=90,y=80)

#######################################################################################################################

frame = Frame(root,width=400,height=480,bg="light blue")
frame.place(x=1100,y=190)

login = Label(frame, text='User Credentials', fg='black', bg="light blue", font=('Areal',20,'bold'))
login.place(x=90,y=30)
Frame(frame, width=350, height=3,bg='black').place(x=20, y=90)

id=Label(frame, text='Username', fg='black', bg="light blue", font=('Areal',15))
id.place(x=150,y=130)
user = Entry(frame,width=36,fg='black',border=2,bg="light blue", font=('Areal',12))
user.place(x=30, y=165)
Frame(frame, width=330, height=2,bg='black').place(x=30, y=202)

pas=Label(frame, text='Password', fg='black', bg="light blue", font=('areal',15))
pas.place(x=150,y=230)
code = Entry(frame,width=36,fg='black', border=2,bg="light blue", font=('Areal',12))
code.place(x=30, y=265)
Frame(frame, width=330, height=2,bg='black').place(x=30, y=302)

#######################################################################################################################


b1 = Button(frame,width=34,pady=8,bg='#57a1f8', border=2 , command=signin)
b1.place(x=70,y=330)
sn = Label(b1, text='Sign In', fg='white',bg='#57a1f8', font=('areal',15,'bold'))
sn.place(x=90,y=0)

label1 = Button(frame, width=15, text='Forgot Password',border=0,bg='light blue', cursor='hand1',fg='blue')
label1.place(x=140,y=390)

label=Label(frame, text="Don't have an account?", border=0, bg='light blue', font=('Areal',10))
label.place (x=110,y=430)

sign_up = Button(frame, width=6, text='Sign in', border=0,bg='light blue', cursor='hand2',fg='blue')
sign_up.place(x=245, y=429)

root.mainloop()