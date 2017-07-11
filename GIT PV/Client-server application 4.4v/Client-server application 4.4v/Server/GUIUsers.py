import sqlite3 as lite
from Tkinter import *
import config

class But_print:
    def __init__(self, root):
       scrollbar=Scrollbar(orient=VERTICAL)
       self.root = root
       self.lbox1 = Listbox(root, yscrollcommand=scrollbar.set)
       scrollbar.config( command= self.lbox1.yview)
       scrollbar.pack(side=RIGHT,fill=Y)
       self.lbox1.config(height='25')
       self.lbox1.pack(side=TOP,fill=X)
       self.lbox1.pack()
       self.lbox1.delete(0, END)
       # кнопка выхода из формы
       self.butExit = Button(root, text="Выход",  # надпись на кнопке
                        bg="white", fg="black",
                        )
       self.butExit.place(x=570, y=405, width=100, height=40)
       self.butExit.bind("<Button-1>", self.ExitFun)
       # кнопка блокирования пользователя
       self.butLock = Button(root, text="Блокировать",  # надпись на кнопке
                             bg="white", fg="black",
                             )
       self.butLock.place(x=460, y=405, width=100, height=40)
       self.butLock.bind("<Button-1>", self.ClockFun)
       # кнопка разблокирования пользователя
       self.butUnLock = Button(root, text="Разблокировать",  # надпись на кнопке
                             bg="white", fg="black",
                             )
       self.butUnLock.place(x=350, y=405, width=100, height=40)
       self.butUnLock.bind("<Button-1>", self.UnClockFun)
       con = lite.connect('C:\Users\user04.K714\Desktop\GIT PV\Client-server application 4.4v\Client-server application 4.4v\Server\Bin\DB\USERS.db')
       with con:
           cur = con.cursor()
           cur.execute("SELECT Login, Name, Surname,ConConection, Password FROM Users")
           rows = cur.fetchall()
           for row in rows:
               self.lbox1.insert(END, row)

    def ClockFun(self , event):
        selectIndex = self.lbox1.curselection()
        value=self.lbox1.get(selectIndex[0],selectIndex[0])
        SplitString=str((value[0])).split(" ")
        manival=SplitString[0].replace("(u'","")
        manival2=manival.replace("',","")
        con = lite.connect('USERS.db')
        cur = con.cursor()
        cur.execute("UPDATE  Users SET ConConection = '" + str(FALSE) + "'"+"WHERE Login ='" + manival2+ "'")
        #-----------------------------------------------------------------------------
        cur.execute("SELECT Login, Name, Surname,ConConection, Password FROM Users")
        config.ClientCommand = (manival2, 1)
        rows = cur.fetchall()
        self.lbox1.delete(0, END)
        for row in rows:
            self.lbox1.insert(END, row)
        #----------------------------------------------------------------------
        con.commit()
        con.close()

    def UnClockFun(self, event):
        selectIndex = self.lbox1.curselection()
        value = self.lbox1.get(selectIndex[0], selectIndex[0])
        SplitString = str((value[0])).split(" ")
        manival = SplitString[0].replace("(u'", "")
        manival2 = manival.replace("',", "")
        con = lite.connect('USERS.db')
        cur = con.cursor()
        cur.execute("UPDATE  Users SET ConConection = '" + str(TRUE) + "'" + "WHERE Login ='" + manival2 + "'")

        #-----------------------------------------------------------------------------
        cur.execute("SELECT Login, Name, Surname,ConConection, Password FROM Users")
        rows = cur.fetchall()
        self.lbox1.delete(0,END)
        for row in rows:
            self.lbox1.insert(END, row)
        #----------------------------------------------------------------------
        con.commit()
        con.close()
    def ExitFun(self, event):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk() # Окно
    root.geometry('700x450') # Размер окнаа
    root.title('Списки пользователей') # Заголовок окна
    root.resizable(width = False, height = False) # Запрет на изменение размеров окна
    obj=But_print()
    root.mainloop()