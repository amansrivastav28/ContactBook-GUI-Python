#Contact Login Databases
from tkinter import *
from tkinter import messagebox as ms
from pymysql import *
root=Tk()
frame=Frame(root,bg='#883000')
frame.pack(side=TOP,fill=X)
frame1=Frame(root,bg='grey')
frame1.pack(side=TOP,fill=BOTH,expand=YES)
root.geometry('300x300+500+200') 
root.title("Login") 
root.resizable(0,0)
con=connect(db='contact',user='root',host='localhost',password='srivastav')
cur=con.cursor()
root.config(background='#363636')
def fun1():
    if(cur.execute("select * from login where username='%s' and password='%s'"%(txt1.get(),txt2.get()))):
        root.destroy()
        root1=Tk()
        frame2=Frame(root1,bg='#883000')
        frame2.pack(side=TOP,fill=X)
        frame3=Frame(root1,bg='grey')
        frame3.pack(side=TOP,fill=BOTH,expand=YES)
        frame4=Frame(root1,bg='brown')
        frame4.pack(side=TOP,fill=X,expand=YES)
        root1.geometry('800x500+300+100')
        root1.title("Contact List")
        root1.resizable(0,0)
        def delete():
            cur=con.cursor()
            root2=Tk()
            root2.title("Delete Contact")
            root2.geometry('300x100+500+200')
            root2.resizable(0,0)
            text=Label(root2,text='Enter phone',height=1,width=10,font=(10),foreground='black',padx=10)
            text.grid(row=4,column=5)
            data=Entry(root2,width=20)
            data.grid(row=4,column=6)
            def warning():
                try:
                    if(data.get()=='' or data.get().isalpha() or data.get().isspace() or len(data.get())<=9 or len(data.get())>=11):
                        ms.showwarning('Error','Please Enter Valid Phone No')
                    else:
                        cur.execute("select name,phone from amansrivastav where phone='%s'"%(data.get()))
                        warning=cur.fetchone()
                        if(warning!=None):
                            warning =list(warning)
                            name='  '.join(warning)
                            confirm=ms.askyesnocancel('Warning',"Are you sure to delete rceord \n"+str(name))
                            if(confirm==True):
                                cur.execute("delete from amansrivastav where phone='%s'"%(data.get()))
                                con.commit()
                                root2.destroy()
                                ms.showinfo('Info','Contact Delete Successfully')
                        else:
                            ms.showinfo('Error','Not Found')
                        
                except:
                    ms.showwarning('Network Error','Please Check your Internet Connections')
            deldata=Button(root2,text='Submit',height=1,width=10,bg='brown',font=(10),foreground='black',command=warning)
            deldata.grid(row=5,column=6)
            root2.mainloop()
        def newcontact():
            root3=Tk()
            root3.title("New Contact")
            root3.geometry('300x300+500+200')
            root3.resizable(0,0)
            Information=Label(root3,text='Contact Details',height=1,width=10,font=(10),foreground='black')
            Information.grid(row=0,column=1)
            LabelId=Label(root3,text='ID         ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelId.grid(row=1,column=1)
            EntryId=Entry(root3,width=20)
            EntryId.grid(row=1,column=3)
            LabelName=Label(root3,text='Name      ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelName.grid(row=2,column=1)
            EntryName=Entry(root3,width=20)
            EntryName.grid(row=2,column=3)
            LabelPhone=Label(root3,text='Phone No   ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelPhone.grid(row=3,column=1)
            EntryPhone=Entry(root3,width=20)
            EntryPhone.grid(row=3,column=3)
            LabelCity=Label(root3,text='City       ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelCity.grid(row=4,column=1)
            EntryCity=Entry(root3,width=20)
            EntryCity.grid(row=4,column=3)
            LabelCountry=Label(root3,text='Country    ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelCountry.grid(row=5,column=1)
            EntryCountry=Entry(root3,width=20)
            EntryCountry.grid(row=5,column=3)
            LabelPin=Label(root3,text='Pin code   ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelPin.grid(row=6,column=1)
            EntryPin=Entry(root3,width=20)
            EntryPin.grid(row=6,column=3)

            def add():
                if(EntryId.get()=='' and EntryName.get()=='' and EntryPhone.get()==''):
                    ms.showwarning('Error','Please Enter \n Id \n Name \n Phone')
                elif(EntryId.get()==''):
                    ms.showwarning('Error','Please Enter Id')
                elif(EntryName.get()==''):
                    ms.showwarning('Error','Please Enter Name')
                elif(EntryPhone.get()=='' or len(EntryPhone.get())<=9 or len(EntryPhone.get())>=11 or EntryPhone.get().isalpha()  or EntryPhone.get().isspace()):
                    ms.showwarning('Error','Please Enter Valid Phone Number')
                else:
                    if(EntryId.get().isdigit()):
                        cur.execute("select ID,PHONE from amansrivastav where id='%d'"%(int(EntryId.get())))
                        result=cur.fetchone()
                        validate=[]
                        validate.append(result)
                        if(None in validate) and int(EntryId.get()) not in validate:
                            try:
                                cur.execute("insert into amansrivastav (id,name,phone,city,country,pin_code) values('%d','%s','%s','%s','%s','%s')"%(int(EntryId.get()),EntryName.get(),EntryPhone.get(),EntryCity.get(),EntryCountry.get(),EntryPin.get()))
                                con.commit()
                                ms.showinfo('Info','New Contact Add Successfully')
                                root3.destroy()
                            except:
                                ms.showwarning('Network Error','Please Check your Internet Connection...')
                        else:
                            ms.showinfo('Info','Contact Already Exists')
                    else:
                        ms.showwarning('Error','Id must be Integer')
            insertbutton=Button(root3,text='Submit',height=1,width=10,bg='brown',font=(10),foreground='black',command=add)
            insertbutton.grid(row=9, column=3)
            root3.mainloop()
        def update():
            root5=Tk()
            root5.title("Update Contact")
            root5.geometry('300x300+500+200')
            root5.resizable(0,0)
            Information=Label(root5,text='Update Details',height=1,width=10,font=(10),foreground='black')
            Information.grid(row=0,column=1)
            LabelId=Label(root5,text='ID         ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelId.grid(row=1,column=1)
            Entrybox=[]
            for i in range(0,6):
                if(i==2):
                    Entrybox.append(Entry(root5, text=i, width=20))
                else:
                    Entrybox.append(Entry(root5, text=i,state=DISABLED, width=20))
                Entrybox[i].grid(row=i+1,column=3)

            LabelName=Label(root5,text='Name      ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelName.grid(row=2,column=1)
            LabelPhone=Label(root5,text='Phone No   ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelPhone.grid(row=3,column=1)
            LabelCity=Label(root5,text='City       ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelCity.grid(row=4,column=1)
            LabelCountry=Label(root5,text='Country    ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelCountry.grid(row=5,column=1)
            LabelPin=Label(root5,text='Pin code   ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelPin.grid(row=6,column=1)
            def finddata():
                if(Entrybox[2].get()=='' or len(Entrybox[2].get())<=9 or len(Entrybox[2].get())>=11 or Entrybox[2].get().isalpha()):
                    ms.showwarning('Error','Please Enter Valid Phone Number')
                else:
                    cur.execute("select * from amansrivastav where phone='%s'"%(Entrybox[2].get()))
                    result=cur.fetchall()
                    validate=[]
                    for i in result:
                        validate.append(i)
                    if(len(validate)==0):
                        ms.showinfo('Info','Not Found')
                    else:       
                        for i in validate:
                            for j in range(0,6):
                                Entrybox[j].config(state=NORMAL)
                                Entrybox[j].delete(0,END)
                                Entrybox[j].insert(INSERT,i[j])
                        Entrybox[0].config(state=DISABLED)
            findbutton=Button(root5,text='Search',height=1,width=10,bg='brown',font=(10),foreground='black',command=finddata)
            findbutton.grid(row=9, column=3)
            def updatedata():
                try:
                    cur.execute("update amansrivastav set name ='%s',phone='%s',city='%s',country='%s',pin_code='%s' where id='%d'"%(Entrybox[1].get(),Entrybox[2].get(),Entrybox[3].get(),Entrybox[4].get(),Entrybox[5].get(),int(Entrybox[0].get())))
                    con.commit()
                    ms.showinfo('Info','Update Successfully')
                    root5.destroy()
                except:
                    ms.showwarning('Network Error','Please Check Your Internet Connection...')
            updatebutton=Button(root5,text='Submit',height=1,width=10,bg='brown',font=(10),foreground='black',command=updatedata)
            updatebutton.grid(row=10,column=3)
            root5.mainloop()
        def search():
            root4=Tk()
            root4.title("Search")
            root4.geometry('300x300+500+200')
            LabelId=Label(root4,text='ID         ',height=1,width=10,font=(10),foreground='black',padx=10)
            LabelId.grid(row=1,column=1)
            EntryId=Entry(root4,width=20)
            EntryId.grid(row=1,column=3)
            def fetchdata():
                if(EntryId.get()==''or EntryId.get().isalpha() or  EntryId.get().isspace()):
                    ms.showwarning('Error','Please Enter valid Id')
                else:
                    Iddata=EntryId.get()
                    if(Iddata.isdigit()):
                        try:
                            cur.execute("select * from amansrivastav where id='%d'"%(int(Iddata)))
                            result=cur.fetchall()
                        except:
                            ms.showwarning('Network Error','Please Check your Internet Connection...')
                        validate=[]
                        for i in result:
                            validate.append(i)
                        if(len(validate)==0):
                            ms.showinfo('Info','Not Found')
                        else:
                            LabelId.destroy()
                            EntryId.destroy()
                            root4.geometry('800x400+300+100')
                            root4.resizable(0,0)
                            searchbutton.destroy()
                            databox = Text(root4)
                            ctr = 1
                            databox.insert(INSERT,"ID\tName\t\tPhone No\t\tCity\t\tCountry\t\tPinCode\n")
                            for i in result:
                                databox.insert(INSERT,"%s\t%s\t\t%s\t\t%s\t\t%s\t\t%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5]))
                                ctr = ctr + 1
                            databox.insert(END,"")  
                            databox.pack()
                    else:
                        ms.showwarning('Error','Please Enter Valid Id')
            searchbutton=Button(root4,text='Submit',height=1,width=10,bg='brown',font=(10),foreground='black',command=fetchdata)
            searchbutton.grid(row=2,column=3)
            root4.mainloop()
            
        new=Button(frame2,text='New',height=1,width=10,bg='#b89d6b',font=(10),foreground='black',command=newcontact)
        new.grid(row=4,column=4)
        update=Button(frame2,text='Update',height=1,width=10,bg='#b89d6b',font=(10),foreground='black',command=update)
        update.grid(row=4,column=5)
        delete=Button(frame2,text='Delete',height=1,width=10,bg='#b89d6b',font=(10),foreground='black',command=delete)
        delete.grid(row=4,column=6)
        search=Button(frame2,text='Search',height=1,width=10,bg='#b89d6b',font=(10),foreground='black',command=search)
        search.grid(row=4,column=7)
        cur.execute("select * from amansrivastav")
        result=cur.fetchall()
        txt3 = Text(frame4)
        ctr = 1
        txt3.insert(INSERT,"ID\tName\t\tPhone No\t\tCity\t\tCountry\t\tPinCode\n")
        for i in result:
            txt3.insert(INSERT,"%s\t%s\t\t%s\t\t%s\t\t%s\t\t%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5]))
            ctr = ctr + 1
        txt3.insert(END,"") 
        txt3.pack()
        def refresh():
            cur.execute("select * from amansrivastav")
            result=cur.fetchall()
            txt3.delete(1.0,END)         
            ctr = 1
            txt3.insert(INSERT,"ID\tName\t\tPhone No\t\tCity\t\tCountry\t\tPinCode\n")
            for i in result:
                txt3.insert(INSERT,"%s\t%s\t\t%s\t\t%s\t\t%s\t\t%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5]))
                ctr = ctr + 1
            txt3.insert(END,"")  
            txt3.pack()
        refresh=Button(frame2,text='Refresh',height=1,width=10,bg='#b89d6b',font=(10),foreground='black',command=refresh)
        refresh.grid(row=4,column=8)
        root1.mainloop()   
    else:
        ms.showwarning('Error','Invalid username or password')
label=Label(frame,text='ContactBook',font=(10),height=2,background='#883000',foreground='white',justify=LEFT).pack()
label1=Label(frame1,text='USERNAME',height=2,width=10,background='grey',font=(10),foreground='black',padx=10)
label2=Label(frame1,text='PASSWORD',height=2,width=10,background='grey',font=(10),foreground='black',padx=10)
b1=Button(frame1,text='Login',height=1,width=10,bg='brown',font=(10),foreground='black',command=fun1)
txt1=Entry(frame1,bd=2,width=25)
txt2=Entry(frame1,show='*',bd=2,width=25)
label1.grid(row=1,column=2)
txt1.grid(row=1,column=4)
label2.grid(row=2,column=2)
txt2.grid(row=2,column=4)
b1.grid(row=4,column=4)
root.mainloop()
