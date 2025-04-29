from datetime import datetime
class Evento:
    # Atributos de classe
    total_eventos = 0

    def __init__(self,titulo="",data_hora = datetime,descricao = ""):
        # Inicializaçao Atributos de instância
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        #Adicionando classe_total
        Evento.total_eventos += 1

    def __str__(self,):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descrição: {self.descricao}, Concluido: {self.is_concluido}."
    
    def __eq__(self, other):
        return self.data_hora == other.data_hora
    
    def __ne__(self,other):
        return self.data_hora != other.data_hora
    
    def __gt__(self,other):
        return self.data_hora > other.data_hora
    
    def __lt__(self,other):
        return self.data_hora < other.data_hora
    
    def __ge__(self,other):
        return self.data_hora >= other.data_hora
    
    def __le__(self,other):
        return self.data_hora <= other.data_hora
    
    

    
    
    @classmethod
    def num_eventos(cls):
        print(cls.total_eventos)

    @staticmethod
    def valida_evento(titulo,data_hora,descricao):
        return print (isinstance(titulo,str) and isinstance(data_hora,datetime) and isinstance(descricao,str))
        
        
    def isconcluido_confere(self):
        agora = datetime.now()
        if self.data_hora < agora:
            self.is_concluido = True



evento1 = Evento("Reunião de equipe", datetime(2025,4,1,8,30),"Discutir o progresso do projeto")
evento2 = Evento("Apresentação de resultados", datetime(2025, 4, 2, 10, 0), "Mostrar os resultados trimestrais.")

print("\n\nTeste print instancia: \n")
print("Evento 1:",evento1.__dict__)
print("Evento 2:",evento2.__dict__)

print("Numero de eventos: ",Evento.total_eventos)

print("\n\nTeste isconcluido: \n")
evento1.isconcluido_confere()
evento2.isconcluido_confere()
print("Evento1:", evento1.__dict__)
print("Evento 2:",evento2.__dict__)

print("\n\nTeste num_eventos : \n")
Evento.num_eventos()

print("\n\nTeste valida_evento : \n")
Evento.valida_evento("Reunião de equipe", datetime(2025,4,1,8,30),"Discutir o progresso do projeto")
Evento.valida_evento("Reunião de equipe", datetime(2025,4,1,8,30),2)
Evento.valida_evento("Reunião de equipe", 3,"Discutir o progresso do projeto")

print("\n Teste __str__")
print(evento1)

print("\n Teste operadores matematicos")
print(evento1.data_hora ,"          ",evento2.data_hora )

print("Igual",evento1 == evento2)
print("Não Igual",evento1 != evento2)

print("Maior", evento1 > evento2)
print("Menor", evento1 < evento2)

print("Maior Igual", evento1 >= evento2)
print("Menor Igual", evento1 <= evento2)