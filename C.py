from M import Model
from tkinter import *
from tkinter import filedialog
import os
import sys


class Controller:
    def __init__(self):
        self.bd = Model()

    def getFile(self):
        file = filedialog.askopenfile()
        pach = os.path.abspath(file.name)

        return pach

    def cadastrar(self, Nome, Stoque, Pic):
        if Nome == "" or Stoque == "" or Pic == "":
            return False
        else:
            self.bd.cad(Nome, Stoque, Pic)
    
    def search(self, par):
        self.bd.find(par)    
    
    def every(self):
        itens = self.bd.everyItem()

        return itens
    
    
    def edit(self,Id):
        self.bd.edit(Id)

        return True
    
    def moveFile(self, pach):
        self.bd.moveFile(pach)

    def exit(self):
        sys.exit()
    
if __name__ == "__main__":
    controller = Controller()