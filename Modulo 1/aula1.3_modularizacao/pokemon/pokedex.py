NUMERO_MAXIMO = 150 
TIPOS = ('Normal', 'Fogo', 'Agua', 'Eletrico', 'Grama', 'Gelo', 'Lutador', 'Venenoso', 'Terra', 'Voador', 'Psiquico', 'Inseto', 'Pedra', 'Fantasma', 'Dragao', 'Noturno', 'Metalico', 'Fada')

# Funçoes
def verificar_tipo_pokemon(tipo):
    return tipo in TIPOS # Verifica se o tipo do pokemon é valido

def verificar_numero_pokemon(numero):
    return 1 <= numero <= NUMERO_MAXIMO # Verifica se o numero do pokemon é valido
