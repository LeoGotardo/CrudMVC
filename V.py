import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
from C import Controller


class View:
    def __init__(self):
        self.root = Tk()
        self.c = Controller()

        self.mainScreen()
        self.root.mainloop()


    def mainScreen(self):

        self.root.geometry("600x700")
        self.root.title("MainD")
        self.root.configure(bg="black")
        self.root.bind('<Escape>', self.c.exit)
        self.mainFrame = tk.Frame(self.root, height=600, width=700, bg="black")
        self.mainFrame.grid(row=0, column=0, columnspan=2,padx=150)

        self.create_label(self.mainFrame,"MainD", ('Calibri', 40), 10, 10)

        self.create_label(self.mainFrame, "Product Name:", ('Calibri', 15), 10, 10)
        self.entryName = self.create_entry(self.mainFrame, 'center', 'grey', 1, 50)
        
               
        self.create_label(self.mainFrame, "Stock:", ('Calibri', 15), 10, 10)
        self.entryEstoque = self.create_entry(self.mainFrame, 'center', 'grey', 1, 50)
           
        self.create_button(self.mainFrame, "Cadastrar", ('Calibri', 10), '#121313', 'white', 10, 20, lambda:[self.cadastrar(self.entryName.get(),self.entryEstoque.get(), self.c.getFile()), self.clearFields("mainScreen")])
        
        self.create_button(self.mainFrame, "Limpar Campos", ('Calibri', 10), '#121313', 'white', 10, 10, self.clearFields("mainScreen"))     

        self.create_button(self.mainFrame, "Search Itens", ('Calibri', 10), '#121313', 'white', 10, 10, lambda:[self.searchScreen(), self.mainFrame.grid_forget()])


    def searchScreen(self):
        self.searchFrame = tk.Frame(self.root, height=700, width=800, bg="black")
        self.searchFrame.grid(row=0, column=0, columnspan=2,padx=150)

        self.create_label(self.searchFrame, "MainD", ('Calibri', 40), 10, 10)

        self.create_label(self.searchFrame,"Search:", ('Calibri', 15), 10, 10)
        self.entrySearch = self.create_entry(self.searchFrame, 'center', 'grey', 1, 50)

        self.create_button(self.searchFrame,"Search", ('Calibri', 10), '#121313', 'white', 10, 10, lambda:[self.create_table('white', 'black', self.entrySearch.get())])
        self.create_button(self.searchFrame, "Add a Product", ('Calibri', 10), '#121313', 'white', 10, 10, lambda:[self.mainScreen(), self.searchFrame.grid_forget()])

    def editScreen(self):
        self.editFrame = tk.Frame(self.root, height=600, width=700, bg="black")
        self.searchFrame.grid(row=0, column=0, columnspan=2, padx=150)

        self.create_label(self.editFrame, "MainD",('Calibri', 40), 10, 10)

        self.create_label(self.editFrame, "New Name:", ('Calibri', 15), 10, 10)
        self.entryNewName = self.create_entry(self.editFrame, 'center', 'grey', 1, 50)

        self.create_label(self.editFrame, "New Stock:", ('Calibri', 15), 10, 10)
        self.entryNewStock = self.create_entry(self.editFrame, 'center', 'grey', 1, 50)

        self.create_label(self.editFrame, "New Pic:", ('Calibri', 15), 10, 10)
        self.entryNewPic = self.create_entry(self.editFrame, 'center', 'grey', 1, 50)


    def create_table(self, fg, bg, func):
        Nomes = self.c.bd.find(func, "Nomes")
        Estoques = self.c.bd.find(func, "Estques")
        Ident = self.c.bd.find(func, "Ident")
        Fotos = self.c.bd.find(func, "Fotos")
        for i in self.c.bd.fotos:
            imagem = ImageTk.PhotoImage(i)
            Fotos.append(imagem)

        tableFrame = tk.Frame(self.root,height=100, width=150, bg='black')
        tableFrame.grid(row=1, column=0, columnspan=2)

        self.create_label(tableFrame, "ID", ('Calibri',15), 10, 10)
        self.entryID = self.create_entry(tableFrame, 'center', 'grey', 1, 50)

        self.create_button(tableFrame, "DELETE", ('Calibri', 10),'#121313', 'white', 10, 10, lambda:[self.c.delete(), self.mainScreen(), self.editFrame.grid_forget()])

        self.create_button(tableFrame,'Edit',('Calibri', 10), '#121313', 'white', 10, 10, lambda:[self.c.edit(self.entryID.get()), self.clearFields('editScreen')])

        legend1 = Entry(tableFrame, width=20, font=('Calibri1',10), bg=bg, fg=fg)
        
        legend1.grid(row=0,column=1)
        legend1.insert(END, "ID")

        legend2 = Entry(tableFrame, width=20, font=('Calibri1',10), bg=bg, fg=fg)
        
        legend2.grid(row=0,column=2)
        legend2.insert(END, "Nome")
        
        legend3 = Entry(tableFrame, width=20, font=('Calibri1',10), bg=bg, fg=fg)
        
        legend3.grid(row=0,column=3)
        legend3.insert(END, "Estoque")

        legend4 = Entry(tableFrame, width=20, font=('Calibri1',10), bg=bg, fg=fg)
        
        legend4.grid(row=0,column=4)
        legend4.insert(END, "Pic")
        ind=1


        while ind < (len(Nomes)+1):
                alfa = Entry(tableFrame, width=20, font=('Calibri',10), bg=bg, fg=fg, )

                alfa.grid(row=ind, column=1)
                alfa.insert(END, ind)

                a = Entry(tableFrame, width=20, font=('Calibri',10), bg=bg, fg=fg)
                
                a.grid(row=ind, column=2)
                a.insert(END, Nomes[ind-1])

                b = Entry(tableFrame, width=20, font=('Calibri',10), bg=bg, fg=fg)
                
                b.grid(row=ind, column=3)
                b.insert(END, Estoques[ind-1])

                c = Entry(tableFrame, width=20, fg=fg, font=('Calibri',10), bg=bg)
                
                c.grid(row=i, column=2)
                c.insert(END, Imagens[i])

                ind+=1
        print(f"Nomes:{Nomes}\nEstoque:{Estoques}\nIdent:{Ident}")
        return Ident

    def create_label(self, frame, text, font, pady, padx):
        label = Label(frame, text=text, font=font, justify='center', bg='black', fg='white', pady=pady, padx=padx)

        label.grid()

    def create_entry(self, frame, justify, bg, borderwidth, width):
        entry = Entry(frame, justify=justify, bg=bg, borderwidth=borderwidth, width=width)
        entry.grid()
        return entry


    def create_button(self, frame, text, font, bg, fg, pady, padx, command):
        button = Button(frame, borderwidth=0, text=text, font=font, justify='center', bg=bg, fg=fg, pady=pady, padx=padx, command=command)
        
        button.grid(pady=10)


    def alert(self, Name):
        alert = messagebox
        id = self.c.bd.find(Name, "Ident")
        alert.showwarning('Salvo', "ID: "+str(id))

    def clearFields(self, screen):
        if screen == "mainScreen":
            self.entryName.delete(0, tk.END)
            self.entryEstoque.delete(0, tk.END)

        elif screen == "editScreen":
            self.entryNewName.delete(0,tk.END)
            self.entryNewPic.delete(0,tk.END)            
            self.entryNewStock.delete(0,tk.END)
    
    def cadastrar(self, nome, estoque, getfile):
        if self.c.cadastrar(nome, estoque, getfile) == False:
              messagebox.showwarning('Falha','Preencha todos os campos')
              self.clearFields("mainScreen")
        else:
            self.alert(self.entryName.get())

if __name__ == "__main__":
        view = View()