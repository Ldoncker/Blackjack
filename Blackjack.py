from random import *
from tkinter import *

class Blackjack(object):
    def __init__(self):
        self.compteurbackground = 1
        self.compteurbackcard = 1
        self.color ="#36794e"
        self.cartes = ["Ressources/1t.gif",
            "Ressources/2t.gif",
            "Ressources/3t.gif",
            "Ressources/4t.gif",
            "Ressources/5t.gif",
            "Ressources/6t.gif",
            "Ressources/7t.gif",
            "Ressources/8t.gif",
            "Ressources/9t.gif",
            "Ressources/10t.gif",
            "Ressources/11t.gif",
            "Ressources/12t.gif",
            "Ressources/13t.gif",
            "Ressources/1p.gif",
            "Ressources/2p.gif",
            "Ressources/3p.gif",
            "Ressources/4p.gif",
            "Ressources/5p.gif",
            "Ressources/6p.gif",
            "Ressources/7p.gif",
            "Ressources/8p.gif",
            "Ressources/9p.gif",
            "Ressources/10p.gif",
            "Ressources/11p.gif",
            "Ressources/12p.gif",
            "Ressources/13p.gif",
            "Ressources/1ca.gif",
            "Ressources/2ca.gif",
            "Ressources/3ca.gif",
            "Ressources/4ca.gif",
            "Ressources/5ca.gif",
            "Ressources/6ca.gif",
            "Ressources/7ca.gif",
            "Ressources/8ca.gif",
            "Ressources/9ca.gif",
            "Ressources/10ca.gif",
            "Ressources/11ca.gif",
            "Ressources/12ca.gif",
            "Ressources/13ca.gif",
            "Ressources/1co.gif",
            "Ressources/2co.gif",
            "Ressources/3co.gif",
            "Ressources/4co.gif",
            "Ressources/5co.gif",
            "Ressources/6co.gif",
            "Ressources/7co.gif",
            "Ressources/8co.gif",
            "Ressources/9co.gif",
            "Ressources/10co.gif",
            "Ressources/11co.gif",
            "Ressources/12co.gif",
            "Ressources/13co.gif"]
        self.menu()
        
##-----------------------------------------------------------------------------------------------------------
##
##-------------------------------------------- Menu ---------------------------------------------------------
##
##-----------------------------------------------------------------------------------------------------------

    def menu(self):
        self.menu = Tk()
        self.menu.title("Blackjack")
        self.menu.resizable(width = False, height = False)
        self.menu.wm_iconbitmap("Ressources/icon.ico")
        self.loadimages()
        self.windowWidth, self.windowHeight = self.menubackground.width(), self.menubackground.height()
        self.positionRight = int(self.menu.winfo_screenwidth() // 2 - self.windowWidth // 2)
        self.positionDown = int(self.menu.winfo_screenheight() // 2 - self.windowHeight // 2 - 60)
        self.menu.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.labelmenubg = Label(self.menu, image = self.menubackground)
        self.labelmenubg.pack()
        self.b1a = Button(self.menu, text = "1 adversaire", font="Algerian", fg =  self.color, bg = "#000000", width = 13, command = self.wgame1)
        self.b1a.place(x=175, y=220)
        self.b2a = Button(self.menu, text = "2 adversaires", font="Algerian", fg =  self.color, bg = "#000000", width = 13, command = self.wgame2)
        self.b2a.place(x=175, y=270)
        self.b3a = Button(self.menu, text = "Options", font="Algerian", fg =  self.color, bg = "#000000", width = 13, command = self.woptions)
        self.b3a.place(x=175, y=350)
        self.menu.mainloop()

##-----------------------------------------------------------------------------------------------------------
##
##-------------------------------------------- 1 Adversaire -------------------------------------------------
##
##-----------------------------------------------------------------------------------------------------------

    def wgame1(self):
        self.game = Toplevel()
        self.game.title("Blackjack")
        self.game.resizable(width = False, height = False)
        self.game.wm_iconbitmap("Ressources/icon.ico")
        self.labelgamebg = Label(self.game, image=self.gamebackground)
        self.labelgamebg.pack()
        self.windowWidth, self.windowHeight = self.gamebackground.width(), self.gamebackground.height()
        self.positionRight = int(self.game.winfo_screenwidth() / 2 - self.windowWidth / 2)
        self.positionDown = int(self.game.winfo_screenheight() / 2 - self.windowHeight / 2 - 50)
        self.game.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.bs1 = Button(self.game, text = "Débuter la partie", font="Algerian", fg = self.color, bg = "#000000", command = self.sgame1)
        self.bs1.place(x=275, y=335)
        self.gamebackcard1 = Label(self.game, image=self.backcard)
        self.gamebackcard1.place(x=295, y=550)
        self.gamebackcard2 = Label(self.game, image=self.backcard)
        self.gamebackcard2.place(x=295, y=10)
        self.score = Label(self.game, text = "Score : 0", bg =  self.color, font = ("Helvetica", 13))
        self.score.place(x=315, y=523)
        self.popupOn = False
        self.game.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.b1a.config(command="")
        self.b2a.config(command="")
        self.b3a.config(command="")
        self.game.mainloop()

    def sgame1(self):
        self.labelgamebg.config(image=self.tokengame1)
        self.cartesp1 = 0
        self.cartesp2 = 0
        self.totalp1 = 0
        self.totalp2 = 0
        self.acep1 = 0
        self.acep2 = 0
        self.p1ok = True
        self.p2ok = True
        self.cartesp = []
        self.gamebackcard1.destroy()
        self.gamebackcard2.destroy()
        self.bs1.destroy()
        self.bs1 = Button(self.game, text = "Prendre une carte", font="Algerian", fg =  self.color, bg = "#000000")
        self.bs1.place(x=265,y=300)
        self.bs2 = Button(self.game, text = "Passer", font="Algerian", fg =  self.color, bg = "#000000")
        self.bs2.place(x=315,y=350)
        self.p1game1()

#------------------------------------------------------------------------------------------------------------

    def p1game1(self):
        if self.p1ok == True:
            if self.cartesp1 == 5 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c6p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c6 = Label(self.game, image=self.c6p1)
                self.p1c6.place(x=370, y=550)
            if self.cartesp1 == 4 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c5p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c5=Label(self.game, image=self.c5p1)
                self.p1c5.place(x=350,y=550)
            if self.cartesp1 == 3 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c4p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c4=Label(self.game, image=self.c4p1)
                self.p1c4.place(x=330, y=550)
            if self.cartesp1 == 2 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c3p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c3=Label(self.game, image=self.c3p1)
                self.p1c3.place(x=310,y=550)
            if self.cartesp1 == 0 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c1p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c1=Label(self.game, image=self.c1p1)
                self.p1c1.place(x=270, y=550)
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c2p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c2 = Label(self.game, image=self.c2p1)
                self.p1c2.place(x=290, y=550)
            self.acecheckp1()
            if self.totalp1 >= 21 :
                self.bs1.config(command="")
                self.bs2.config(command="")
                self.p1ok = False
        self.score.config(text = "Score : " + str(self.totalp1))
        self.p2game1()

    def p2game1(self):
        self.p2AI()
        if self.p2ok == True :
            if self.cartesp2 == 5 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c6p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c6 = Label(self.game, image=self.backcard)
                self.p2c6.place(x=370, y=10)
            if self.cartesp2 == 4 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c5p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c5 = Label(self.game, image=self.backcard)
                self.p2c5.place(x=350, y=10)
            if self.cartesp2 == 3 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c4p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c4 = Label(self.game, image=self.backcard)
                self.p2c4.place(x=330, y=10)
            if self.cartesp2 == 2 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c3p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c3 = Label(self.game, image=self.backcard)
                self.p2c3.place(x=310, y=10)
            if self.cartesp2 == 0 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c1p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c1=Label(self.game, image=self.c1p2)
                self.p2c1.place(x=270, y=10)
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c2p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c2=Label(self.game, image=self.backcard)
                self.p2c2.place(x=290, y=10)
        self.G1checkok()

#------------------------------------------------------------------------------------------------------------

    def G1checkok(self):
        if self.p1ok == True :
            self.bs1.config(command=self.p1game1)
            self.bs2.config(command=self.G1passer)
        elif self.p2ok == False :
            self.G1whowins()
        else :
            self.p2game1()

    def G1passer(self):
        self.p1ok = False
        self.bs1.config(command="")
        self.bs2.config(command="")
        self.p2game1()

    def G1whowins(self):
        if self.totalp1 > 21 :
            self.G1ending()
            self.G1loose()
        elif self.totalp1 == 21 :
            if self.totalp2 == 21 :
                self.G1ending()
                self.G1drawgame()
            else :
                self.G1ending()
                self.G1win()
        else :
            if self.totalp2 == self.totalp1 :
                self.G1ending()
                self.G1drawgame()
            elif self.totalp2 > self.totalp1 and self.totalp2 < 22 :
                self.G1ending()
                self.G1loose()
            else:
                self.G1ending()
                self.G1win()

#------------------------------------------------------------------------------------------------------------

    def G1ending(self):
        self.p2c2 = Label(self.game, image=self.c2p2)
        self.p2c2.place(x=290, y=10)
        if self.cartesp2 > 2:
            self.p2c3 = Label(self.game, image=self.c3p2)
            self.p2c3.place(x=310, y=10)
        if self.cartesp2 > 3:
            self.p2c4 = Label(self.game, image=self.c4p2)
            self.p2c4.place(x=330, y=10)
        if self.cartesp2 > 4:
            self.p2c5 = Label(self.game, image=self.c5p2)
            self.p2c5.place(x=350, y=10)
        if self.cartesp2 > 5:
            self.p2c6 = Label(self.game, image=self.c6p2)
            self.p2c6.place(x=370, y=10)
        self.score2 = Label(self.game, text="Score : " + str(self.totalp2), bg= self.color, font=("Helvetica", 13))
        self.score2.place(x=315, y=157)

    def G1win(self):
        self.popupOn = True
        self.popup = Toplevel()
        self.popup.title("Victoire !")
        self.popup.resizable(width=False, height=False)
        self.popup.wm_iconbitmap("Ressources/icon.ico")
        self.popup.geometry("300x80")
        self.windowWidth, self.windowHeight = self.popup.winfo_reqwidth(), self.popup.winfo_reqheight()
        self.positionRight = int(self.popup.winfo_screenwidth() / 2 - self.windowWidth / 2 - 50)
        self.positionDown = int(self.popup.winfo_screenheight() / 2 - self.windowHeight / 2 + 20)
        self.popup.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.popup.configure(background= self.color)
        self.labelwin = Label(self.popup, text="Bravo, vous avez gagné !", bg =  self.color, font = ("Helvetica", 13))
        self.labelwin.place(x=53, y=5)
        self.bw1 = Button(self.popup, text = "Rejouer", font="Algerian", fg =  self.color, bg = "#000000", command=self.G1restart)
        self.bw1.place(x=60,y=35)
        self.bw2 = Button(self.popup, text = "Quitter", font="Algerian", fg =  self.color, bg = "#000000", command=self.quitgame)
        self.bw2.place(x=150,y=35)
        self.popup.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.popup.mainloop()

    def G1loose(self):
        self.popupOn = True
        self.popup = Toplevel()
        self.popup.title("Défaite")
        self.popup.resizable(width=False, height=False)
        self.popup.wm_iconbitmap("Ressources/icon.ico")
        self.popup.geometry("300x80")
        self.windowWidth, self.windowHeight = self.popup.winfo_reqwidth(), self.popup.winfo_reqheight()
        self.positionRight = int(self.popup.winfo_screenwidth() / 2 - self.windowWidth / 2 - 50)
        self.positionDown = int(self.popup.winfo_screenheight() / 2 - self.windowHeight / 2 + 20)
        self.popup.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.popup.configure(background= self.color)
        self.labelwin = Label(self.popup, text="Vous avez perdu.", bg =  self.color, font = ("Helvetica", 13))
        self.labelwin.place(x=80, y=5)
        self.bw1 = Button(self.popup, text = "Rejouer", font="Algerian", fg =  self.color, bg = "#000000", command=self.G1restart)
        self.bw1.place(x=60,y=35)
        self.bw2 = Button(self.popup, text = "Quitter", font="Algerian", fg =  self.color, bg = "#000000", command=self.quitgame)
        self.bw2.place(x=150,y=35)
        self.popup.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.popup.mainloop()

    def G1drawgame(self):
        self.popupOn = True
        self.popup = Toplevel()
        self.popup.geometry("300x80")
        self.popup.title("Égalité !")
        self.popup.resizable(width=False, height=False)
        self.popup.wm_iconbitmap("Ressources/icon.ico")
        self.windowWidth, self.windowHeight = self.popup.winfo_reqwidth(), self.popup.winfo_reqheight()
        self.positionRight = int(self.popup.winfo_screenwidth() / 2 - self.windowWidth / 2 - 50)
        self.positionDown = int(self.popup.winfo_screenheight() / 2 - self.windowHeight / 2 + 20)
        self.popup.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.popup.configure(background= self.color)
        self.labelwin = Label(self.popup, text="Égalité !", bg =  self.color, font = ("Helvetica", 13))
        self.labelwin.place(x=120, y=5)
        self.bw1 = Button(self.popup, text="Rejouer", font="Algerian", fg =  self.color, bg = "#000000", command=self.G1restart)
        self.bw1.place(x=60, y=35)
        self.bw2 = Button(self.popup, text="Quitter", font="Algerian", fg =  self.color, bg = "#000000", command=self.quitgame)
        self.bw2.place(x=150, y=35)
        self.popup.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.popup.mainloop()

    def G1restart(self):
        self.popup.destroy()
        self.game.destroy()
        self.wgame1()

##-----------------------------------------------------------------------------------------------------------
##
##-------------------------------------------- 2 Adversaires ------------------------------------------------
##
##-----------------------------------------------------------------------------------------------------------

    def wgame2(self):
        self.game = Toplevel()
        self.game.title("Blackjack")
        self.game.resizable(width = False, height = False)
        self.game.wm_iconbitmap("Ressources/icon.ico")
        self.labelgamebg = Label(self.game, image=self.gamebackground)
        self.labelgamebg.pack()
        self.windowWidth, self.windowHeight = self.gamebackground.width(), self.gamebackground.height()
        self.positionRight = int(self.game.winfo_screenwidth() / 2 - self.windowWidth / 2)
        self.positionDown = int(self.game.winfo_screenheight() / 2 - self.windowHeight / 2 - 60)
        self.game.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.bs1 = Button(self.game, text="Débuter la partie", font="Algerian", fg= self.color, bg="#000000", command=self.sgame2)
        self.bs1.place(x=275, y=335)
        self.gamebackcard1 = Label(self.game, image=self.backcard)
        self.gamebackcard1.place(x=295, y=550)
        self.gamebackcard2 = Label(self.game, image=self.backcard)
        self.gamebackcard2.place(x=20, y=10)
        self.gamebackcard3 = Label(self.game, image=self.backcard)
        self.gamebackcard3.place(x=450, y=10)
        self.score = Label(self.game, text="Score : 0", bg= self.color, font=("Helvetica", 13))
        self.score.place(x=315, y=523)
        self.popupOn = False
        self.game.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.b1a.config(command="")
        self.b2a.config(command="")
        self.b3a.config(command="")
        self.game.mainloop()

    def sgame2(self):
        self.dealerchoice()
        if self.dealer == 1 :
            if self.compteurbackground == 1 :
                self.game2 = PhotoImage(file="Ressources/game2-1green.gif")
            elif self.compteurbackground == 2 :
                self.game2 = PhotoImage(file="Ressources/game2-1blue.gif")
            elif self.compteurbackground == 3 :
                self.game2 = PhotoImage(file="Ressources/game2-1red.gif")
        else :
            if self.compteurbackground == 1 :
                self.game2 = PhotoImage(file="Ressources/game2-2green.gif")
            elif self.compteurbackground == 2 :
                self.game2 = PhotoImage(file="Ressources/game2-2blue.gif")
            elif self.compteurbackground == 3 :
                self.game2 = PhotoImage(file="Ressources/game2-2red.gif")
        self.labelgamebg.config(image=self.game2)
        self.cartesp1 = 0
        self.cartesp2 = 0
        self.cartesp3 = 0
        self.totalp1 = 0
        self.totalp2 = 0
        self.totalp3 = 0
        self.acep1 = 0
        self.acep2 = 0
        self.acep3 = 0
        self.p1ok = True
        self.p2ok = True
        self.p3ok = True
        self.cartesp = []
        self.gamebackcard1.destroy()
        self.gamebackcard2.destroy()
        self.gamebackcard3.destroy()
        self.bs1.destroy()
        self.bs1 = Button(self.game, text="Prendre une carte", font="Algerian", fg= self.color, bg="#000000")
        self.bs1.place(x=265, y=300)
        self.bs2 = Button(self.game, text="Passer", font="Algerian", fg= self.color, bg="#000000")
        self.bs2.place(x=315, y=350)
        self.p1game2()

#------------------------------------------------------------------------------------------------------------

    def dealerchoice(self):
        self.dealer = randrange(1,3)

#------------------------------------------------------------------------------------------------------------

    def p1game2(self):
        if self.p1ok == True:
            if self.cartesp1 == 5 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c6p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c6 = Label(self.game, image=self.c6p1)
                self.p1c6.place(x=370, y=550)
            if self.cartesp1 == 4 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c5p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c5=Label(self.game, image=self.c5p1)
                self.p1c5.place(x=350,y=550)
            if self.cartesp1 == 3 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c4p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c4=Label(self.game, image=self.c4p1)
                self.p1c4.place(x=330, y=550)
            if self.cartesp1 == 2 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c3p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c3=Label(self.game, image=self.c3p1)
                self.p1c3.place(x=310,y=550)
            if self.cartesp1 == 0 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c1p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c1=Label(self.game, image=self.c1p1)
                self.p1c1.place(x=270, y=550)
                self.gpick()
                if self.valeur == 1 :
                    self.acep1 += 1
                self.totalp1 += self.valeur
                self.c2p1 = PhotoImage(file = self.fcarte)
                self.cartesp1 += 1
                self.p1c2 = Label(self.game, image=self.c2p1)
                self.p1c2.place(x=290, y=550)
            self.acecheckp1()
            if self.totalp1 >= 21 :
                self.bs1.config(command="")
                self.bs2.config(command="")
                self.p1ok = False
        self.score.config(text="Score : " + str(self.totalp1))
        self.p2game2()

    def p2game2(self):
        self.p2AI()
        if self.p2ok == True :
            if self.cartesp2 == 5 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c6p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c6 = Label(self.game, image=self.backcard)
                self.p2c6.place(x=120, y=10)
            if self.cartesp2 == 4 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c5p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c5 = Label(self.game, image=self.backcard)
                self.p2c5.place(x=100, y=10)
            if self.cartesp2 == 3 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c4p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c4 = Label(self.game, image=self.backcard)
                self.p2c4.place(x=80, y=10)
            if self.cartesp2 == 2 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c3p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c3 = Label(self.game, image=self.backcard)
                self.p2c3.place(x=60, y=10)
            if self.cartesp2 == 0 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c1p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                if self.dealer == 1 :
                    self.p2c1=Label(self.game, image=self.c1p2)
                else:
                    self.p2c1=Label(self.game, image=self.backcard)
                self.p2c1.place(x=20, y=10)
                self.gpick()
                if self.valeur == 1 :
                    self.acep2 += 1
                self.totalp2 += self.valeur
                self.c2p2 = PhotoImage(file = self.fcarte)
                self.cartesp2 += 1
                self.p2c2=Label(self.game, image=self.backcard)
                self.p2c2.place(x=40, y=10)
        self.p3game2()

    def p3game2(self):
        self.p3AI()
        if self.p3ok == True :
            if self.cartesp3 == 5 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep3 += 1
                self.totalp3 += self.valeur
                self.c6p3 = PhotoImage(file = self.fcarte)
                self.cartesp3 += 1
                self.p3c6=Label(self.game, image=self.backcard)
                self.p3c6.place(x=550,y=10)
            if self.cartesp3 == 4 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep3 += 1
                self.totalp3 += self.valeur
                self.c5p3 = PhotoImage(file = self.fcarte)
                self.cartesp3 += 1
                self.p3c5=Label(self.game, image=self.backcard)
                self.p3c5.place(x=530,y=10)
            if self.cartesp3 == 3 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep3 += 1
                self.totalp3 += self.valeur
                self.c4p3 = PhotoImage(file = self.fcarte)
                self.cartesp3 += 1
                self.p3c4=Label(self.game, image=self.backcard)
                self.p3c4.place(x=510,y=10)
            if self.cartesp3 == 2 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep3 += 1
                self.totalp3 += self.valeur
                self.c3p3 = PhotoImage(file = self.fcarte)
                self.cartesp3 += 1
                self.p3c3=Label(self.game, image=self.backcard)
                self.p3c3.place(x=490,y=10)
            if self.cartesp3 == 0 :
                self.gpick()
                if self.valeur == 1 :
                    self.acep3 += 1
                self.totalp3 += self.valeur
                self.c1p3 = PhotoImage(file = self.fcarte)
                self.cartesp3 += 1
                if self.dealer == 2:
                    self.p3c1=Label(self.game, image=self.c1p3)
                else:
                    self.p3c1=Label(self.game, image=self.backcard)
                self.p3c1.place(x=450,y=10)
                self.gpick()
                if self.valeur == 1 :
                    self.acep3 += 1
                self.totalp3 += self.valeur
                self.c2p3 = PhotoImage(file = self.fcarte)
                self.cartesp3 += 1
                self.p3c2=Label(self.game, image=self.backcard)
                self.p3c2.place(x=470,y=10)
        self.G2checkok()

#------------------------------------------------------------------------------------------------------------

    def G2checkok(self):
        if self.p1ok == True:
            self.bs1.config(command=self.p1game2)
            self.bs2.config(command=self.G2passer)
        elif self.p2ok == False and self.p3ok == False:
            self.G2whowins()
        else:
            self.p2game2()

    def G2passer(self):
        self.p1ok = False
        self.bs1.config(command="")
        self.bs2.config(command="")
        self.p2game2()

    def G2whowins(self):
        if self.totalp1 > 21:
            self.G2ending()
            self.G2loose()
        elif self.totalp1 == self.totalp2 and self.totalp1 == self.totalp3:
            self.G2ending()
            self.G2drawgame()
        elif self.totalp1 == 21:
            self.G2ending()
            self.G2win()
        elif self.totalp1 < 21:
            if self.totalp2 < 22 and self.totalp2 > self.totalp1:
                self.G2ending()
                self.G2loose()
            elif self.totalp3 < 22 and self.totalp3 > self.totalp1:
                self.G2ending()
                self.G2loose()
            elif self.totalp1 > self.totalp2 and self.totalp1 > self.totalp3:
                self.G2ending()
                self.G2win()
            else :
                self.G2ending()
                self.G2win()

#------------------------------------------------------------------------------------------------------------

    def G2ending(self):
        self.p2c1 = Label(self.game, image=self.c1p2)
        self.p2c1.place(x=20, y=10)
        self.p2c2 = Label(self.game, image=self.c2p2)
        self.p2c2.place(x=40, y=10)
        if self.cartesp2 > 2:
            self.p2c3 = Label(self.game, image=self.c3p2)
            self.p2c3.place(x=60, y=10)
        if self.cartesp2 > 3:
            self.p2c4 = Label(self.game, image=self.c4p2)
            self.p2c4.place(x=80, y=10)
        if self.cartesp2 > 4:
            self.p2c5 = Label(self.game, image=self.c5p2)
            self.p2c5.place(x=100, y=10)
        if self.cartesp2 > 5:
            self.p2c6 = Label(self.game, image=self.c6p2)
            self.p2c6.place(x=120, y=10)
        self.p3c2=Label(self.game, image=self.c2p3)
        self.p3c2.place(x=470,y=10)
        if self.cartesp3 > 2:
            self.p3c3=Label(self.game, image=self.c3p3)
            self.p3c3.place(x=490,y=10)
        if self.cartesp3 > 3:
            self.p3c4=Label(self.game, image=self.c4p3)
            self.p3c4.place(x=510,y=10)
        if self.cartesp3 > 4:
            self.p3c5=Label(self.game, image=self.c5p3)
            self.p3c5.place(x=530,y=10)
        if self.cartesp3 > 5:
            self.p3c6=Label(self.game, image=self.c6p3)
            self.p3c6.place(x=550,y=10)
        self.score2 = Label(self.game, text="Score : " + str(self.totalp2), bg= self.color, font=("Helvetica", 13))
        self.score2.place(x=50, y=157)
        self.score3 = Label(self.game, text="Score : " + str(self.totalp3), bg= self.color, font=("Helvetica", 13))
        self.score3.place(x=500, y=157)

    def G2win(self):
        self.popupOn = True
        self.popup = Toplevel()
        self.popup.title("Victoire !")
        self.popup.resizable(width=False, height=False)
        self.popup.wm_iconbitmap("Ressources/icon.ico")
        self.popup.geometry("300x80")
        self.windowWidth, self.windowHeight = self.popup.winfo_reqwidth(), self.popup.winfo_reqheight()
        self.positionRight = int(self.popup.winfo_screenwidth() / 2 - self.windowWidth / 2 - 50)
        self.positionDown = int(self.popup.winfo_screenheight() / 2 - self.windowHeight / 2 + 20)
        self.popup.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.popup.configure(background= self.color)
        self.labelwin = Label(self.popup, text="Bravo, vous avez gagné !", bg =  self.color, font = ("Helvetica", 13))
        self.labelwin.place(x=53, y=5)
        self.bw1 = Button(self.popup, text = "Rejouer", font="Algerian", fg =  self.color, bg = "#000000", command=self.G2restart)
        self.bw1.place(x=60,y=35)
        self.bw2 = Button(self.popup, text = "Quitter", font="Algerian", fg =  self.color, bg = "#000000", command=self.quitgame)
        self.bw2.place(x=150,y=35)
        self.popup.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.popup.mainloop()

    def G2loose(self):
        self.popupOn = True
        self.popup = Toplevel()
        self.popup.title("Défaite")
        self.popup.resizable(width=False, height=False)
        self.popup.wm_iconbitmap("Ressources/icon.ico")
        self.popup.geometry("300x80")
        self.windowWidth, self.windowHeight = self.popup.winfo_reqwidth(), self.popup.winfo_reqheight()
        self.positionRight = int(self.popup.winfo_screenwidth() / 2 - self.windowWidth / 2 - 50)
        self.positionDown = int(self.popup.winfo_screenheight() / 2 - self.windowHeight / 2 + 20)
        self.popup.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.popup.configure(background= self.color)
        self.labelwin = Label(self.popup, text="Vous avez perdu.", bg =  self.color, font = ("Helvetica", 13))
        self.labelwin.place(x=80, y=5)
        self.bw1 = Button(self.popup, text = "Rejouer", font="Algerian", fg =  self.color, bg = "#000000", command=self.G2restart)
        self.bw1.place(x=60,y=35)
        self.bw2 = Button(self.popup, text = "Quitter", font="Algerian", fg =  self.color, bg = "#000000", command=self.quitgame)
        self.bw2.place(x=150,y=35)
        self.popup.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.popup.mainloop()

    def G2drawgame(self):
        self.popupOn = True
        self.popup = Toplevel()
        self.popup.geometry("300x80")
        self.popup.title("Égalité !")
        self.popup.resizable(width=False, height=False)
        self.popup.wm_iconbitmap("Ressources/icon.ico")
        self.windowWidth, self.windowHeight = self.popup.winfo_reqwidth(), self.popup.winfo_reqheight()
        self.positionRight = int(self.popup.winfo_screenwidth() / 2 - self.windowWidth / 2 - 50)
        self.positionDown = int(self.popup.winfo_screenheight() / 2 - self.windowHeight / 2 + 20)
        self.popup.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.popup.configure(background= self.color)
        self.labelwin = Label(self.popup, text="Égalité !", bg =  self.color, font = ("Helvetica", 13))
        self.labelwin.place(x=120, y=5)
        self.bw1 = Button(self.popup, text="Rejouer", font="Algerian", fg =  self.color, bg = "#000000", command=self.G2restart)
        self.bw1.place(x=60, y=35)
        self.bw2 = Button(self.popup, text="Quitter", font="Algerian", fg =  self.color, bg = "#000000", command=self.quitgame)
        self.bw2.place(x=150, y=35)
        self.popup.protocol('WM_DELETE_WINDOW', self.quitgame)
        self.popup.mainloop()

    def G2restart(self):
        self.popup.destroy()
        self.game.destroy()
        self.wgame2()

##-----------------------------------------------------------------------------------------------------------
##
##-----------------------------------------------------------------------------------------------------------

    def gpick(self):
        while True :
            self.randomp()
            if self.fcarte not in self.cartesp :
                self.cartesp.append(self.fcarte)
                break
        self.quickmath()

    def randomp(self):
        self.valeur = randrange(52)
        self.fcarte = self.cartes[self.valeur]

    def quickmath(self):
        self.valeur += 1
        if self.valeur > 39 :
            self.valeur -= 13
        if self.valeur > 26 :
            self.valeur -= 13
        if self.valeur > 13 :
            self.valeur -= 13
        if self.valeur > 10 :
            self.valeur = 10

#------------------------------------------------------------------------------------------------------------

    def p2AI(self):
        self.acecheckp2()
        if self.totalp2 < 12 :
            self.p2ok = True
        elif self.totalp2 == 12 or self.totalp2 == 13 :
            self.a = randrange(100)
            if self.a == 1 :
                self.p2ok = False
        elif self.totalp2 == 14 :
            self.a = randrange(10)
            if self.a == 1:
                self.p2ok = False
        elif self.totalp2 == 15 :
            self.a = randrange(2)
            if self.a == 1:
                self.p2ok = True
        elif self.totalp2 == 16 :
            self.a = randrange(5)
            if self.a == 1:
                self.p2ok = True
        elif self.totalp2 == 17 :
            self.a = randrange(20)
            if self.a == 1:
                self.p2ok = True
        elif self.totalp2 > 17 :
            self.p2ok = False

    def p3AI(self):
        self.acecheckp3()
        if self.totalp3 < 12 :
            self.p3ok = True
        elif self.totalp3 == 12 or self.totalp3 == 13 :
            self.a = randrange(100)
            if self.a == 1 :
                self.p3ok = True
        elif self.totalp3 == 14 :
            self.a = randrange(10)
            if self.a == 1:
                self.p3ok = True
        elif self.totalp3 == 15 :
            self.a = randrange(2)
            if self.a == 1:
                self.p3ok = True
        elif self.totalp3 == 16 :
            self.a = randrange(5)
            if self.a == 1:
                self.p3ok = True
        elif self.totalp3 == 17 :
            self.a = randrange(20)
            if self.a == 1:
                self.p3ok = True
        elif self.totalp3 > 17 :
            self.p3ok = False

#------------------------------------------------------------------------------------------------------------

    def acecheckp1(self):
        if self.acep1 > 0:
            if self.totalp1 + 10 == 21 :
                self.totalp1 = 21

    def acecheckp2(self):
        if self.acep2 > 0:
            if self.totalp2 + 10 == 21 :
                self.totalp2 = 21

    def acecheckp3(self):
        if self.acep3 > 0:
            if self.totalp3 + 10 == 21 :
                self.totalp3 = 21

#------------------------------------------------------------------------------------------------------------

    def woptions(self):
        self.options = Toplevel()
        self.options.title("Options")
        self.options.resizable(width=False, height=False)
        self.options.wm_iconbitmap("Ressources/icon.ico")
        self.windowWidth, self.windowHeight = self.optionbg.width(), self.optionbg.height()
        self.positionRight = int(self.options.winfo_screenwidth() // 2 - self.windowWidth // 2)
        self.positionDown = int(self.options.winfo_screenheight() // 2 - self.windowHeight // 2 - 60)
        self.options.geometry("+{}+{}".format(self.positionRight, self.positionDown))
        self.labeloptionsbg = Label(self.options, image=self.optionbg)
        self.labeloptionsbg.pack()
        self.labelbg = Label(self.options, text="Fond d'écran", bg= self.color, font=("Helvetica", 13))
        self.labelbg.place(x=101, y=25)
        self.labelbackcard = Label(self.options, text="Dos de carte", bg=self.color, font=("Helvetica", 13))
        self.labelbackcard.place(x=400, y=25)
        self.green = PhotoImage(file="Ressources/optiongreen.gif")
        self.blue = PhotoImage(file="Ressources/optionblue.gif")
        self.red = PhotoImage(file="Ressources/optionred.gif")
        self.options.protocol('WM_DELETE_WINDOW', self.saveoptions)
        self.b1a.config(command="")
        self.b2a.config(command="")
        self.b3a.config(command="")

        self.previewbg = Canvas(self.options, width= 100, height=150)
        self.previewbg.place(x=100, y=50)
        self.previewcard = Canvas(self.options, width=110, height=135)
        self.previewcard.place(x=393, y=50)

        self.leftbg = Button(self.options, width = 2, text="<", bg=self.color, height=2, relief=GROOVE, command=self.pleftbg)
        self.leftbg.place(x=74  , y=100)
        self.rightbg = Button(self.options, text=">",bg=self.color, width=2, height=2, relief=GROOVE, command=self.pleftbg)
        self.rightbg.place(x=205, y=100)

        self.leftbc = Button(self.options, width=2, text="<", bg=self.color, height=2, relief=GROOVE, command=self.pleftbc)
        self.leftbc.place(x=367, y=100)
        self.rightbc = Button(self.options, text=">", bg=self.color, width=2, height=2, relief=GROOVE, command=self.prightbc)
        self.rightbc.place(x=508, y=100)

        self.backmenu = Button(self.options, text="Retourner au menu", fg=self.color, bg="#000000", width=18, font="Algerian", command=self.saveoptions)
        self.backmenu.place(x=203, y=270)

        self.previewcard.create_image(0,0, image=self.backcard, anchor=NW)
        if self.compteurbackground == 1:
            self.previewbg.create_image(0, 0, image=self.green, anchor=NW)
        elif self.compteurbackground == 2:
            self.previewbg.create_image(0, 0, image=self.blue, anchor=NW)
        else:
            self.previewbg.create_image(0, 0, image=self.red, anchor=NW)

        self.bcompteurbackground = self.compteurbackground
        self.bcompteurbackcard = self.compteurbackcard

        self.options.mainloop()

    def pleftbg(self):
        self.optionchange("background", "left")

    def prightbg(self):
        self.optionchange("background", "right")

    def pleftbc(self):
        self.optionchange("backcard", "left")

    def prightbc(self):
        self.optionchange("backcard", "right")

    def optionchange(self,subject,direction):
        if subject == "background":
            if direction == "right":
                self.compteurbackground += 1
                if self.compteurbackground == 4:
                    self.compteurbackground = 1
            else:
                self.compteurbackground -= 1
                if self.compteurbackground == 0:
                    self.compteurbackground = 3
            self.previewbg.delete("all")
            if self.compteurbackground == 1 :
                self.previewbg.create_image(0,0, image=self.green, anchor=NW)
                self.color = "#36794e"
            elif self.compteurbackground == 2:
                self.previewbg.create_image(0,0, image=self.blue, anchor=NW)
                self.color = "#264666"
            elif self.compteurbackground == 3:
                self.previewbg.create_image(0,0, image=self.red, anchor=NW)
                self.color = "#74252b"
            self.previewbg.update()
        else:
            if direction == "right":
                self.compteurbackcard += 1
                if self.compteurbackcard == 6:
                    self.compteurbackcard = 1
            else :
                self.compteurbackcard -= 1
                if self.compteurbackcard == 0:
                    self.compteurbackcard = 5
            self.previewcard.delete("all")
            if self.compteurbackcard == 1:
                self.backcard = PhotoImage(file="Ressources/bcsimple.gif")
            elif self.compteurbackcard == 2:
                self.backcard = PhotoImage(file="Ressources/bchs.gif")
            elif self.compteurbackcard == 3:
                self.backcard = PhotoImage(file="Ressources/bcpokemon.gif")
            elif self.compteurbackcard == 4:
                self.backcard = PhotoImage(file="Ressources/bcuno.gif")
            elif self.compteurbackcard == 5:
                self.backcard = PhotoImage(file="Ressources/bcyugi.gif")
            self.previewcard.create_image(0,0, image=self.backcard, anchor=NW)
            self.previewcard.update()

    def saveoptions(self):
        self.options.destroy()
        self.b1a.config(command=self.wgame1)
        self.b2a.config(command=self.wgame2)
        self.b3a.config(command=self.woptions)
        if self.compteurbackground != self.bcompteurbackground:
            if self.compteurbackground == 1:
                self.menubackground = PhotoImage(file="Ressources/menugreen.gif")
                self.gamebackground = PhotoImage(file="Ressources/gamegreen.gif")
                self.tokengame1 = PhotoImage(file="Ressources/game1green.gif")
                self.optionbg = PhotoImage(file="Ressources/optiongreen.gif")
            elif self.compteurbackground == 2:
                self.menubackground = PhotoImage(file="Ressources/menublue.gif")
                self.gamebackground = PhotoImage(file="Ressources/gameblue.gif")
                self.tokengame1 = PhotoImage(file="Ressources/game1blue.gif")
                self.optionbg = PhotoImage(file="Ressources/optionblue.gif")
            else:
                self.menubackground = PhotoImage(file="Ressources/menured.gif")
                self.gamebackground = PhotoImage(file="Ressources/gamered.gif")
                self.tokengame1 = PhotoImage(file="Ressources/game1red.gif")
                self.optionbg = PhotoImage(file="Ressources/optionred.gif")
            self.labelmenubg.config(image=self.menubackground)
            self.b1a.config(fg=self.color)
            self.b2a.config(fg=self.color)
            self.b3a.config(fg=self.color)

    def loadimages(self):
        self.menubackground = PhotoImage(file="Ressources/menugreen.gif")
        self.gamebackground = PhotoImage(file="Ressources/gamegreen.gif")
        self.backcard = PhotoImage(file="Ressources/bcsimple.gif")
        self.tokengame1 = PhotoImage(file="Ressources/game1green.gif")
        self.optionbg = PhotoImage(file="Ressources/optiongreen.gif")

    def quitgame(self):
        if self.popupOn == True :
            self.popup.destroy()
            self.popupOn = False
        self.game.destroy()
        self.b1a.config(command=self.wgame1)
        self.b2a.config(command=self.wgame2)
        self.b3a.config(command=self.woptions)

##-----------------------------------------------------------------------------------------------------------
##
##-----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    Blackjack()
