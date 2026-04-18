class Item:
    def __init__(self, id, valor, peso):
        self.id = id
        self.valor = valor
        self.peso = peso
    
    def __repr__(self):
        return f"Item(ID:{self.id}, V:{self.valor}, P:{self.peso})"
    def __str__(self):
        return f"Item(ID:{self.id}, V:{self.valor}, P:{self.peso})"