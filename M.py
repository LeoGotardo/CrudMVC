from pymongo import MongoClient
from PIL import Image
from bson import Binary
import io
import os


class Model:
    def __init__(self):
        self.root = "LeoGotardo"
        self.password = "GUDP6TDvj9vdzGEH"
        self.CONNECTION_STRING = f"mongodb+srv://{self.root}:{self.password}@cluster0.8isoiw5.mongodb.net/"

        self.client = MongoClient(self.CONNECTION_STRING)
        self.bd = self.client["Dug"]
        self.Products = self.bd["Products"]

        print(self.client['user_shopping_list'])


    def cad(self, Nome, Estoque, Pic):
        products = self.bd["Products"]

        data = self.moveFile(Pic)

        product = {
            "Nome": Nome,
            "Estoque": Estoque,
            "Picture_path": Pic,
            "Picture_data": data
        }

        products.insert_one(product)


    def moveFile(self, pach):
        im = Image.open(pach)
        image_bytes = io.BytesIO()
        formate = pach.split(".")
  
        im.save(image_bytes, format = formate[-1])
        
        bytes = image_bytes.getvalue()

        return bytes


    def everything(self):
        every = self.Products.find({"Nome":{"$exists": True}})
        coll = []
        for result in every: 
            coll.append(result)
            
        return coll


    def everyItem(self, Item):
        every = self.Products.find({"_id":{"$exists": True}})
        coll = []
        for result in every:      
            coll.append(result[str(Item)])

        return coll
    
    def find(self, Name, indice):
        every = self.Products.find({"Nome":Name})
        self.Nomes = []
        self.Estoques = []
        self.Fotos = []
        self.Ident = []
        for result in every:
            self.Nomes.append(result["Nome"])
            self.Estoques.append(result["Estoque"])
            self.Ident.append(result["_id"])
            self.fotos.append(Image.open(io.BytesIO(result["Picture_data"])))

        if indice == "Nomes":
            self.coll = self.Nomes
        elif indice == "Estoques":
            self.coll = self.Estoques
        elif indice == "Fotos":
            self.coll = self.Fotos
        elif indice == "Ident":
            self.coll = self.Ident

        return self.coll


    def edit(self, id):
        self.Products.update_one({})


if __name__ == "__main__":
    model = Model()
