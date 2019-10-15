from tkinter import *

CROIX = 1
ROND = 2



NOMS = ["", "Croix", "Rond"]


class Fenetre(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.LARGEUR_FENETRE = self.winfo_screenwidth() * 7 // 10
        self.title("Morpion")
        self.resizable(False, False)

        self.canv = Canvas(self, width=self.LARGEUR_FENETRE * 3 // 4, height=self.LARGEUR_FENETRE * 3 // 4, bg="gray")
        self.canv.grid(row=0, column=0)

        self.frame_droite = Frame(self)
        self.frame_droite.grid(row=0, column=1, sticky=N + S + E + W)
        Grid.rowconfigure(self, 0, weight=1)

        self.bouton = Button(self.frame_droite, bg="yellow", text="Recommencer")
        self.bouton.grid(row=0, column=0, sticky=N + S + E + W)
        Grid.rowconfigure(self.frame_droite, 0, weight=1)

        self.midframe = Frame(self.frame_droite, bg="black", width=self.LARGEUR_FENETRE // 4)
        self.midframe.grid(row=1, column=0, sticky=N + S + E + W)
        Grid.rowconfigure(self.frame_droite, 1, weight=1)

        self.label = Label(self.frame_droite, bg="white", anchor=N + W)
        self.label.grid(row=2, column=0, sticky=N + S + E + W)
        Grid.rowconfigure(self.frame_droite, 2, weight=1)

        self.bouton.bind("<Button-1>", self.reset)
        self.canv.bind("<Button-1>", self.clic_canvas)

        self.reset()

    def dessiner(self):
        self.canv.delete("all")
        self.canv.create_line(self.LARGEUR_FENETRE // 4, 0, self.LARGEUR_FENETRE // 4, self.LARGEUR_FENETRE * 3 // 4, width=5)
        self.canv.create_line(self.LARGEUR_FENETRE // 2, 0, self.LARGEUR_FENETRE // 2, self.LARGEUR_FENETRE * 3 // 4, width=5)
        self.canv.create_line(0, self.LARGEUR_FENETRE // 4, self.LARGEUR_FENETRE * 3 // 4, self.LARGEUR_FENETRE // 4, width=5)
        self.canv.create_line(0, self.LARGEUR_FENETRE // 2, self.LARGEUR_FENETRE * 3 // 4, self.LARGEUR_FENETRE // 2, width=5)

        for i in range(0, 9):

            if self.etatTableau[i // 3][i % 3] == CROIX:
                self.canv.create_line((i // 3) * self.LARGEUR_FENETRE // 4 + 10, (i % 3) * self.LARGEUR_FENETRE // 4 + 10, (i // 3) * self.LARGEUR_FENETRE // 4 + (self.LARGEUR_FENETRE // 4 - 10),
                                      (i % 3) * self.LARGEUR_FENETRE // 4 + (self.LARGEUR_FENETRE // 4 - 10), width=5)
                self.canv.create_line((i // 3) * self.LARGEUR_FENETRE // 4 + 10, (i % 3) * self.LARGEUR_FENETRE // 4 + (self.LARGEUR_FENETRE // 4 - 10), (i // 3) * self.LARGEUR_FENETRE // 4 + (self.LARGEUR_FENETRE // 4 - 10),
                                      (i % 3) * self.LARGEUR_FENETRE // 4 + 10, width=5)

            if self.etatTableau[i // 3][i % 3] == ROND:
                self.canv.create_oval((i // 3) * self.LARGEUR_FENETRE // 4 + 10, (i % 3) * self.LARGEUR_FENETRE // 4 + 10, (i // 3) * self.LARGEUR_FENETRE // 4 + (self.LARGEUR_FENETRE // 4 - 10),
                                      (i % 3) * self.LARGEUR_FENETRE // 4 + (self.LARGEUR_FENETRE // 4 - 10), width=5)

    def reset(self, event=None):
        self.etatTableau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.joueur = CROIX

        self.victoire = False

        self.canv.delete("all")
        self.canv.create_line(self.LARGEUR_FENETRE // 4, 0, self.LARGEUR_FENETRE // 4, self.LARGEUR_FENETRE * 3 // 4, width=5)
        self.canv.create_line(self.LARGEUR_FENETRE // 2, 0, self.LARGEUR_FENETRE // 2, self.LARGEUR_FENETRE * 3 // 4, width=5)
        self.canv.create_line(0, self.LARGEUR_FENETRE // 4, self.LARGEUR_FENETRE * 3 // 4, self.LARGEUR_FENETRE // 4, width=5)
        self.canv.create_line(0, self.LARGEUR_FENETRE // 2, self.LARGEUR_FENETRE * 3 // 4, self.LARGEUR_FENETRE // 2, width=5)

        self.label.config(text=NOMS[self.joueur] + " commence")

    def clic_canvas(self, event):
        if (self.victoire):
            return

        x = event.x // (self.LARGEUR_FENETRE // 4)
        y = event.y // (self.LARGEUR_FENETRE // 4)

        if self.etatTableau[x][y] == 0:
            self.etatTableau[x][y] = self.joueur

            if self.test_victoire():
                self.label.config(text=NOMS[self.joueur] + " a gagné!")
                self.victoire = True
            elif self.test_egalite():
                self.label.config(text="Égalité")
                self.victoire = True
            else:
                self.joueur = 3 - self.joueur
                self.label.config(text=NOMS[self.joueur] + " joue")

        else:
            self.label.config(text="Cette case est occupée")

        self.dessiner()

    def test_victoire(self):
        for i in range(0, 3):
            if self.etatTableau[i][0] == self.etatTableau[i][1] and self.etatTableau[i][1] == self.etatTableau[i][2] and self.etatTableau[i][0] != 0:
                return True

            if self.etatTableau[0][i] == self.etatTableau[1][i] and self.etatTableau[1][i] == self.etatTableau[2][i] and self.etatTableau[0][i] != 0:
                return True

        if (self.etatTableau[0][0] == self.etatTableau[1][1] and self.etatTableau[1][1] == self.etatTableau[2][2] and self.etatTableau[0][0] != 0):
            return True

        if (self.etatTableau[2][0] == self.etatTableau[1][1] and self.etatTableau[1][1] == self.etatTableau[0][2] and self.etatTableau[1][1] != 0):
            return True
        return False

    def test_egalite(self):
        for i in range(0, 9):
            if self.etatTableau[i // 3][i % 3] == 0:
                return False
        return True


Fenetre().mainloop()
