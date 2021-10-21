from config import *

class Pokemon(db.Model):
    #Atributos da classe Pokemon
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    tipo = db.Column(db.String(254))
    categoria = db.Column(db.String(254))
    altura = db.Column(db.String(254))
    peso = db.Column(db.String(254))
    
    #Método para imprimir em texto
    def __str__(self):
        return f'ID {self.id}) {self.nome}, ' +\
               f'Tipo {self.tipo}, Pokemon {self.categoria}, Altura: {self.altura}, Peso: {self.peso}.'
    
    #Método de expressão da classe em Json
    def json(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "categoria": "Pokemon " + self.categoria,
            "altura": self.altura,
            "peso": self.peso,
        }
    
if __name__ == "__main__":
    
    #Apagar arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
        
    #Criar tabela
    db.create_all()
    
    #Teste da classe Pokemon
    p1 = Pokemon(nome = "Pikachu", tipo = "Eletrico", categoria = "Rato Elétrico", altura = "0.4 m", peso = "6.0 kg")
    p2 = Pokemon(nome = "Charmander", tipo = "Fogo", categoria = "Lagarto", altura = "0.6 m", peso = "8.5 kg")
    p3 = Pokemon(nome = "Bulbasauro", tipo = "Planta", categoria = "Semente", altura = "0.7 m", peso = "6.7 kg")
    
    #Persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.commit()
    
    #Exibir
    print(p1)
    print(p2)
    print(p3.json())