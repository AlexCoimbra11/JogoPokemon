import pickle
from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print('Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!'.format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas:')
    print('1-', pikachu)
    print('2-', charmander)
    print('3-', squirtle)

    while True:
        escolha = input('Escolha o seu Pokemon')
        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha invalida!')

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('jogo salvo com sucesso')

    except Exception as error:
        print("Erro ao salvar o jogo")
        print(error)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            pickle.load(arquivo)
            print('Loading feito com sucesso')
            return player
    except:
        print("Save não encontrado")


if __name__=='__main__':
    print('__________________________________________')
    print('Bem vindo ao game Pokemon RPG de terminal')
    print('__________________________________________')

    player = carregar_jogo()

    if not player:

        nome = input('Ola, qual é o seu nome:')
        player = Player(nome)
        print('Ola {}, esse é um mundo habitado por pokemons, '
              'a partir de agora sua missão é se tornar um mestre dos pokemons!'.format(player))
        print('Capture o maximo de pokemons que conseguir e ute com seus inimigos')
        player.mostrar_dinheiro()
        if player.pokemons:
            print('Ja vi que vc tem alguns pokemons')
            player.mostrar_pokemons()
        else:
            print('Você não tem nenhum pokemon, portanto precisa escolher um')
            escolher_pokemon_inicial(player)

        print('Pronto, agora que vc ja possui um pokemon, '
             'enfrente seu arqui-rival desde o jardim da infancia Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        gary.batalhar(gary)
        salvar_jogo(player)
    while True:
        print('___________________________________')
        print('O que deseja fazer?:')
        print('1- Caçar pockemons pelo mundão a fora:')
        print('2- Lutar com um inimigo :')
        print('3- Pokeagenda')
        print('0 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo...')
            break
        elif escolha =='1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print('Escolha inválida')
