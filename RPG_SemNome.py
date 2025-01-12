from random import randint as r
from time import sleep as s

contador = 0
# inimigos
inimigos = [{'nome': 'Zumbi', 'hp': 10, 'forca': 2, 'defesa': 1, 'mana': 0, 'mira': 100, 'energia': 10, 'velocidade': 5, 'evasiva': 10, 'critico': 10,'level': 1},
            {'nome': 'Esqueleto', 'hp': 8, 'forca': 2, 'defesa': 0,'mana': 0, 'mira': 80, 'energia': 10, 'velocidade': 7, 'evasiva': 20, 'critico': 20, 'level': 1},
            {'nome': 'Vampiro', 'hp': 14, 'forca': 4, 'defesa': 4,'mana': 0, 'mira': 90, 'energia': 15, 'velocidade': 8, 'evasiva': 20, 'critico': 30, 'level': 1}]

# equipando
print('antes de jogar...')
s(1)
print('vamos personalizar seus equipamentos')
s(2)
print('Na sua batalha,', end= ' ')
s(1)
print('você ira utilizar o quê? ')
while True:
    opc = int(input('''<<<->>>=<<<->>>=<<<->>>
[ 1 ] Espada
[ 2 ] Arco
[ 3 ] Soco

[ 4 ] Ver inimigos
=> '''))
    if opc > 4 and opc < 1:
        print('Valor invalido!')
        s(1)
    else:
        if opc == 1:
            equipamento_mao = {'nome': 'Espada', 'forca': 3, 'critico': 10, 'energia': 3, 'level': 1}
            break
        elif opc == 2:
            equipamento_mao = {'nome': 'Arco', 'forca': 2, 'critico': 30, 'energia': 2, 'level': 1}
            break
        elif opc == 3:
            equipamento_mao = {'nome': 'Soco', 'forca': forca, 'critico': critico, 'energia': 1, 'level': level}
            break
        else:
            for c in range(0, 3):
                print('\n')
                print('=-'*15)
                for k, v in inimigos[c].items():
                    print(f'{k} = {v}')
                s(3)
print('<<<->>>=<<<->>>=<<<->>>')
# configuração do personagem
p_hp = 10
p_mana = 10
p_energia = 10
p_velocidade = 5
p_forca = 2
p_defesa = 1
p_sorte = 10
p_mira = 100
p_evasiva = 10
p_critico = 5
p_level = 1
p_xp = 0

# configuraçao do jogo
fim = 0
mochila = list()

desbloquear_novo_inimigo = 1
ativar_defesa = 0
ativar_defesa_inimiga = 0
vez = 0
altura_torre = 1

equipamento_ataque = [{'nome': 'Espada', 'forca': 3, 'critico': 10, 'energia': 3, 'level': 1},
                        {'nome': 'Arco', 'forca': 2, 'critico': 30, 'energia': 2, 'level': 1},
                      {'nome': 'Soco', 'forca': p_forca, 'critico': p_critico, 'energia': 1, 'level': p_level}]
equipamento_defesa_cabeça = 0
equipamento_defesa_peitoral = 0
equipamento_defesa_pernas = 0
equipamento_defesa_pes = 0

amuleto_anel_direito = 0
amuleto_anel_esquerdo = 0

a_equipamento_mao = equipamento_mao

ataque_1 = 0
ataque_2 = 0
forca_especial = (a_equipamento_mao["forca"] +2) * 2
energia_especial = (a_equipamento_mao["energia"] +2) * 2

# jogo
while True:
    print('\n'*100)
    if altura_torre == 5:
        desbloquear_novo_inimigo += 1
    for c in range(1, altura_torre+1):
        if c % 5 == 0:
            hp = p_hp
            print('Você encontrou uma poção de cura!')
            contador += 1
            s(2)
    print(f'Você está no andar {altura_torre} da torre')
    s(1)
    inimigo = r(0, desbloquear_novo_inimigo)
    # configuração do inimigo atual
    i_hp = inimigos[inimigo]["hp"]
    i_mana = inimigos[inimigo]["mana"]
    i_energia = inimigos[inimigo]["energia"]
    i_velocidade = inimigos[inimigo]["velocidade"]
    i_forca = inimigos[inimigo]["forca"]
    i_defesa = inimigos[inimigo]["defesa"]
    i_mira = inimigos[inimigo]["mira"]
    i_evasiva = inimigos[inimigo]["evasiva"]
    i_level = inimigos[inimigo]["level"]
    
    # igualando
    forca_equipamento = equipamento_mao
    print(f'Um {inimigos[inimigo]["nome"]} Lv.{inimigos[inimigo]["level"]} apareceu!')
    s(2)
    # status inimigo atual
    i_hp = inimigos[inimigo]["hp"]
    i_mana = inimigos[inimigo]["mana"]
    i_energia = inimigos[inimigo]["energia"]
    i_forca = inimigos[inimigo]["forca"]
    i_defesa = inimigos[inimigo]["defesa"]
    i_velocidade = inimigos[inimigo]["velocidade"]
    i_mira = inimigos[inimigo]["mira"]
    i_evasiva = inimigos[inimigo]["evasiva"]
    i_level = inimigos[inimigo]["level"]

    # status jogador atual
    if altura_torre == 1:
        hp = p_hp
        mana = p_mana
        energia = p_energia
        velocidade = p_velocidade
        forca = p_forca
        defesa = p_defesa
        sorte = p_sorte
        mira = p_mira
        evasiva = p_evasiva
        critico = p_critico
        level = p_level
        xp = p_xp
    
    s(2)
    while True:
        if hp <= 0 or i_hp <= 0:
            break
        if velocidade > i_velocidade or vez == 1:
            if ativar_defesa == 1:
                ativar_defesa = 0
                defesa -= defesa / 2
            print('='*30)
            print('Jogador: ')
            print(f'VIDA = {hp}\nENERGIA = {energia}')
            print()
            print('Inimigo: ')
            print(f'VIDA = {i_hp}\nENERGIA = {i_energia}')
            print('='*30)
            s(3)
            escolha = int(input('''O que deseja fazer?
[ 1 ] ATACAR
[ 2 ] DEFENDER
[ 3 ] ESPERAR
[ 4 ] FUGIR

[ 0 ] SAIR
=> '''))
            if escolha == 0:
                fim = 1
                break
            elif escolha == 1:
                while True:
                    escolha = int(input(f'''Qual ataque usar?
[ 1 ] {a_equipamento_mao["nome"]} Fraco ( -{a_equipamento_mao["energia"]} Energia ) ( +{a_equipamento_mao["forca"]} Força )
[ 2 ] {a_equipamento_mao["nome"]} Forte ( -{a_equipamento_mao["energia"]*2} Energia ) ( +{a_equipamento_mao["forca"]*2} Força )
[ 3 ] ESPECIAL ( -{energia_especial} Energia ) ( +{forca_especial} Força )
[ 4 ] Sem energia
=> '''))
                    if escolha == 1 and equipamento_mao["energia"] <= energia:
                        if r(0, 100) <= i_evasiva:
                            energia -= a_equipamento_mao["energia"]
                            vez = 0
                            print('Errou!')
                            s(2)
                        else:
                            energia -= a_equipamento_mao["energia"]
                            i_hp -= a_equipamento_mao["forca"] - i_defesa
                            vez = 0
                            s(2)
                            if r(0, 100) <= a_equipamento_mao["critico"]:
                                i_hp -= a_equipamento_mao["forca"] - i_defesa
                                print('ACERTO CRITICO!')
                                s(2)
                        break
                    elif escolha == 2 and equipamento_mao["energia"]*2 <= energia:
                        if r(0, 100) <= i_evasiva:
                            print('Errou!')
                            s(2)
                            energia -= a_equipamento_mao["energia"]
                            vez = 0
                        else:
                            energia -= a_equipamento_mao["energia"]*2
                            i_hp -= a_equipamento_mao["forca"]*2 - i_defesa
                            vez = 0
                            s(2)
                            if r(0, 100) <= a_equipamento_mao["critico"]:
                                i_hp -= a_equipamento_mao["forca"]*2 - i_defesa
                                print('ACERTO CRITICO!')
                                s(2)
                        break
                    elif escolha == 3 and energia_especial <= energia:
                        energia -= energia_especial
                        i_hp -= forca_especial - i_defesa
                        vez = 0
                        s(2)
                        if r(0, 100) <= a_equipamento_mao["critico"]:
                            i_hp -= forca_especial - i_defesa
                            print('ACERTO CRITICO!')
                            s(2)
                        break
                    elif escolha > 4 or escolha < 1:
                        print('Valor invalido!')
                        s(2)
                    else:
                        print('Sem energia')
                        break
                        s(2)
            elif escolha == 2:
                vez = 0
                ativar_defesa = 1
                defesa += defesa * 2
                print('Modo defesa')
                s(2)
            elif escolha == 3:
                vez = 0
                if energia < p_energia:
                    energia += 1
                else:
                    print('Energia cheia')
                    s(2)
            elif escolha == 4:
                vez = 0
                if r(0, 100) <= sorte:
                    i_hp = 0
                    print('Você conseguiu fugir!')
                    s(2)
                else:
                    print('Você não conseguiu fugir...')
                    s(2)
        if i_hp <= 0:
            print('Inimigo derrotado!')
            s(2)
            break
        else:
            if i_hp > 0:
                if ativar_defesa_inimiga == 1:
                    ativar_defesa_inimiga = 0
                    i_defesa -= defesa / 2
                vez = 1
                escolha = r(1, 3)
                if escolha == 1:
                    escolha = r(1, 3)
                    if escolha == 1 and inimigos[inimigo]["energia"] >= i_energia:
                        if r(0, 100) <= evasiva:
                            i_energia -= inimigos[inimigo]["forca"]
                            print('Inimigo errou!')
                            s(2)
                        else:
                            hp -= inimigos[inimigo]["forca"] - defesa
                            i_energia -= inimigos[inimigo]["forca"]
                            print('O inimigo atacou')
                            if r(0, 100) <= inimigos[inimigo]["critico"]:
                                hp -= inimigos[inimigo]["forca"] - defesa
                                print('Você recebeu um ataque critico!')
                            s(2)
                    elif escolha == 2 and inimigos[inimigo]["energia"] >= i_energia:
                        if r(0, 100) <= evasiva:
                            i_energia -= inimigos[inimigo]["forca"]
                            print('Inimigo errou!')
                            s(2)
                        else:
                            hp -= inimigos[inimigo]["forca"] - defesa
                            i_energia -= inimigos[inimigo]["forca"]
                            print('O inimigo atacou')
                            if r(0, 100) <= inimigos[inimigo]["critico"]:
                                hp -= inimigos[inimigo]["forca"] - defesa
                                print('Você recebeu um ataque critico!')
                            s(2)
                    elif escolha == 3 and inimigos[inimigo]["energia"] >= i_energia:
                        if r(0, 100) <= evasiva:
                            i_energia -= inimigos[inimigo]["forca"]
                            print('Inimigo errou!')
                            s(2)
                        else:
                            hp -= inimigos[inimigo]["forca"]
                            i_energia -= inimigos[inimigo]["forca"] - defesa
                            print('O inimigo atacou')
                            if r(0, 100) <= inimigos[inimigo]["critico"]:
                                hp -= inimigos[inimigo]["forca"] - defesa
                                print('Você recebeu um ataque critico!')
                            s(2)
                    else:
                        print('Sem energia')
                elif escolha == 2:
                    ativar_defesa_inimiga = 1
                    i_defesa += i_defesa * 2
                    print('Inimigo está em modo defesa!')
                    s(2)
                elif escolha == 3:
                    print('Inimigo está esperando!')
                    if i_energia < inimigos[inimigo]["energia"]:
                        i_energia += 1
                    s(2)
                elif escolha == 4:
                    if r(0, 100) <= sorte:
                        i_hp = 0
                        print('O inimigo fugiu')
                        s(2)
            else:
                print('Inimigo derrotado!')
    while True:
        s(2)
        if hp <= 0:
            print('\n'*100)
            print(f'andar maximo da torre: {altura_torre}')
            s(1)
            print('Você foi derrotado...')
            s(2)
            altura_torre = 0
            
        opc = str(input('Continuar jogando? [S/N]')).upper().strip()
        if opc == 'N':
            break
        else:
            vez = 0
            altura_torre += 1
            break
    if opc == 'N':
        break
print('\n'*100)
print('''Obrigado por testar a versão pre_alpha do meu "RPG sem nome".
Agradecimento especial a VOCÊ JOGADOR!!''')
s(2)
print('''Desenvolvido por RX4N
Versão: 0.0.1''')
s(7)
