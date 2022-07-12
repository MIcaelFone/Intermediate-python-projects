from random import randint
vitoria_jogador_1_modo_de_jogo_1=0
vitoria_jogador_2_modo_de_jogo_1=0
derrota_jogador_1_modo_de_jogo_1=0
derrota_jogador_2_modo_de_jogo_1=0
total_de_jogos_jogador_1_modo_de_jogo_1=0
total_de_jogos_jogador_2_modo_de_jogo_1=0
empate_modo_3=0
empate_modo_1=0
empate_modo_2=0
vitoria_jogador_computador_modo_de_jogo_2=0
vitoria_jogador_humano_modo_de_jogo_2=0
derrota_jogador_computador_modo_de_jogo_2=0
derrota_jogador_humano_modo_de_jogo_2=0
vitoria_computador_2_modo_de_jogo_3=0
vitoria_computador_1_modo_de_jogo_3=0
derrota_computador_2_modo_de_jogo_3=0
derrota_computador_1_modo_de_jogo_3=0
total_de_jogos_computador_1_modo_de_jogo_3=0
total_de_jogos_computador_2_modo_de_jogo_3=0
derrota_computador_modo_de_jogo_2=0
derrota_computador_modo_de_jogo_2=0
total_de_jogos_computador_modo_de_jogo_2=0
total_de_jogos_jogador_humano_modo_de_jogo_2=0
total_de_jogos_jogador_computador_modo_de_jogo_2=0

def menu_de_retorno():
    print("[1] SIM")
    print("[2] NÃO")
    opcao_modo_de_jogo_3 = int(input("Você deseja retornar ao menu principal?"))
    if opcao_modo_de_jogo_3 == 1:
        print("Retornando ao menu principal")
        print("---------------------------")
        inicializando_o_jogo()
    while (opcao_modo_de_jogo_3 == 2):
        print("Volte sempre")
        break
    while opcao_modo_de_jogo_3 > 2:
        print("Opção errada")
        print("Digite novamente")
        print("---------------------------")
        print("[1] SIM")
        print("[2] NÃO")
        opcao_modo_de_jogo_3 = int(input("Você deseja retornar ao menu principal?"))
        if opcao_modo_de_jogo_3 ==1:
            print("Retornando ao menu principal")
            print("---------------------------")
            inicializando_o_jogo()
        while (opcao_modo_de_jogo_3 == 2):
            print("Volte sempre")
            break
    return opcao_modo_de_jogo_3



def inicializando_o_jogo():
    print("MENU PRINCIPAL")
    print("[1]HUMANO X HUMANO")
    print("[2]HUMANO X COMPUTADOR")
    print("[3]COMPUTADOR X COMPUTADOR")
    print("[4]SAIR")
    modo_de_jogo = int(input("Escolha o modo de jogo:"))
    while modo_de_jogo <=0 or modo_de_jogo >5:
        modo_de_jogo = int(input("Escolha o modo de jogo válida:"))
    if modo_de_jogo == 1:
        print("Escolha sua jogada")
        print("[1]PEDRA")
        print("[2]PAPEL")
        print("[3]TESOURA")
        jogador_1_modo_de_jogo_1 = int(input("JOGADOR 1:"))
        while jogador_1_modo_de_jogo_1 > 3:
            print("OPÇÃO INVÁLIDA")
            print("-------------------------")
            jogador_1_modo_de_jogo_1 = int(input("JOGADOR 1 OPÇÃO INVÁLIDA:"))
        jogador_2_modo_de_jogo_1 = int(input("JOGADOR 2:"))
        while jogador_2_modo_de_jogo_1 > 3:
            print("OPÇÃO INVÁLIDA")
            print("-------------------------")
            jogador_2_modo_de_jogo_1 = int(input("JOGADOR 2 INSIRA UMA OPÇÃO VÁLIDA:"))
        print("-------------------------")
        print("JO")
        print("KEN")
        print("PÔ")
        print("-------------------------")
        if (jogador_1_modo_de_jogo_1 == 2 and jogador_2_modo_de_jogo_1 == 1) or (jogador_1_modo_de_jogo_1 == 3 and jogador_2_modo_de_jogo_1 == 2) or (jogador_1_modo_de_jogo_1 == 1 and jogador_2_modo_de_jogo_1 == 3):
            global vitoria_jogador_1_modo_de_jogo_1,derrota_jogador_2_modo_de_jogo_1,vitoria_jogador_2_modo_de_jogo_1,total_de_jogos_jogador_1_modo_de_jogo_1,total_de_jogos_jogador_2_modo_de_jogo_1
            vitoria_jogador_1_modo_de_jogo_1+=1
            derrota_jogador_2_modo_de_jogo_1 += 1
            total_de_jogos_jogador_1_modo_de_jogo_1 +=1
            total_de_jogos_jogador_2_modo_de_jogo_1 += 1
            print("O jogador 1 venceu a disputa ")

        elif ((jogador_2_modo_de_jogo_1 == 2 and jogador_1_modo_de_jogo_1 == 1) or (jogador_2_modo_de_jogo_1 == 3 and jogador_1_modo_de_jogo_1 == 2) or (jogador_2_modo_de_jogo_1 == 1 and jogador_1_modo_de_jogo_1 == 3)):
            global vitoria_jogador_2_modo_de_jogo_1,derrota_jogador_1_modo_de_jogo_1
            vitoria_jogador_2_modo_de_jogo_1 += 1
            derrota_jogador_1_modo_de_jogo_1 += 1
            total_de_jogos_jogador_1_modo_de_jogo_1 += 1
            total_de_jogos_jogador_2_modo_de_jogo_1 += 1
            print("O jogador 2 venceu a disputa")
            print("-------------------------")

        elif (jogador_2_modo_de_jogo_1 == 1 and jogador_1_modo_de_jogo_1 == 1) or (jogador_2_modo_de_jogo_1 == 2 and jogador_1_modo_de_jogo_1 == 2) or (jogador_2_modo_de_jogo_1 == 3 and jogador_1_modo_de_jogo_1 == 3):
            global empate_modo_1
            empate_modo_1+=1
            total_de_jogos_jogador_1_modo_de_jogo_1+=1
            total_de_jogos_jogador_2_modo_de_jogo_1+=1
            print("Empate")
        print("-------------------------")
        print("Jogador 1:")
        print("NÚMEROS DE PARTIDAS =",total_de_jogos_jogador_1_modo_de_jogo_1)
        print("VITÓRIAS:", vitoria_jogador_1_modo_de_jogo_1)
        print("DERROTAS:",derrota_jogador_1_modo_de_jogo_1)
        print("EMPATES:", empate_modo_1)
        porcentual_de_vitorias_jogador_1_modo_de_jogo_1 = ((vitoria_jogador_1_modo_de_jogo_1 / total_de_jogos_jogador_1_modo_de_jogo_1)) * 100
        print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_jogador_1_modo_de_jogo_1)
        print("---------------------------")
        print("Jogador 2: ")
        print("NÚMEROS DE PARTIDAS =", total_de_jogos_jogador_2_modo_de_jogo_1)
        print("VITÓRIAS:", vitoria_jogador_2_modo_de_jogo_1)
        print("DERROTAS:", derrota_jogador_2_modo_de_jogo_1)
        print("EMPATES:", empate_modo_1)
        porcentual_de_vitorias_jogador_2_modo_de_jogo_1 = ((vitoria_jogador_2_modo_de_jogo_1 / total_de_jogos_jogador_2_modo_de_jogo_1)) * 100
        print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_jogador_2_modo_de_jogo_1)
        print("---------------------------")
        menu_de_retorno()
    if modo_de_jogo == 2:
        print("-------------------------")
        print("Escolha sua jogada")
        print("[1]PEDRA")
        print("[2]PAPEL")
        print("[3]TESOURA")
        jogador_1_modo_de_jogo_2 = int(input("JOGADOR 1:"))
        while jogador_1_modo_de_jogo_2 >3:
            print("Combinação inválida")
            print("-------------------------")
            jogador_1_modo_de_jogo_2 = int(input("JOGADOR 1:"))
        computador_modo_de_jogo_2 = randint(1, 3)
        print("COMPUTADOR:",computador_modo_de_jogo_2)
        print("-------------------------")
        print("JO")
        print("KEN")
        print("PÔ")
        print("-------------------------")

        if (jogador_1_modo_de_jogo_2 == 2 and computador_modo_de_jogo_2 == 1) or (jogador_1_modo_de_jogo_2 == 3 and computador_modo_de_jogo_2 == 2) or (jogador_1_modo_de_jogo_2 == 1 and computador_modo_de_jogo_2 == 3):
            global vitoria_jogador_humano_modo_de_jogo_2,derrota_jogador_computador_modo_de_jogo_2,total_de_jogos_jogador_humano_modo_de_jogo_2,total_de_jogos_jogador_computador_modo_de_jogo_2
            vitoria_jogador_humano_modo_de_jogo_2 = vitoria_jogador_humano_modo_de_jogo_2 + 1
            derrota_jogador_computador_modo_de_jogo_2=derrota_jogador_computador_modo_de_jogo_2 + 1
            total_de_jogos_jogador_computador_modo_de_jogo_2 += total_de_jogos_jogador_computador_modo_de_jogo_2 + 1
            total_de_jogos_jogador_humano_modo_de_jogo_2 += total_de_jogos_jogador_humano_modo_de_jogo_2 + 1
            print("O jogador humano venceu a disputa ")
            print("-------------------------")
        elif ((computador_modo_de_jogo_2 == 1 and jogador_1_modo_de_jogo_2 == 2) or (computador_modo_de_jogo_2 == 3 and jogador_1_modo_de_jogo_2 == 2) or (computador_modo_de_jogo_2 == 1 and jogador_1_modo_de_jogo_2 == 3)):
            global vitoria_jogador_computador_modo_de_jogo_2,derrota_jogador_humano_modo_de_jogo_2
            vitoria_jogador_computador_modo_de_jogo_2 = vitoria_jogador_computador_modo_de_jogo_2 + 1
            derrota_jogador_humano_modo_de_jogo_2 = derrota_jogador_humano_modo_de_jogo_2 + 1
            total_de_jogos_jogador_computador_modo_de_jogo_2 +=1
            total_de_jogos_jogador_humano_modo_de_jogo_2 +=1
            print("O Computador venceu a disputa")
            print("------------------------")
        elif (jogador_1_modo_de_jogo_2 == computador_modo_de_jogo_2):
            global empate_modo_2
            empate_modo_2+=1
            total_de_jogos_jogador_computador_modo_de_jogo_2 +=  1
            total_de_jogos_jogador_humano_modo_de_jogo_2 += 1
            print("Empate")
            print("-------------------------")

        elif ((jogador_1_modo_de_jogo_2 == 2 and computador_modo_de_jogo_2 == 1) or (jogador_1_modo_de_jogo_2 == 3 and computador_modo_de_jogo_2 == 2) or (jogador_1_modo_de_jogo_2 == 1 and computador_modo_de_jogo_2 == 3)):
            vitoria_jogador_humano_modo_de_jogo_2 = vitoria_jogador_humano_modo_de_jogo_2 + 1
            derrota_jogador_computador_modo_de_jogo_2=derrota_jogador_computador_modo_de_jogo_2 + 1
            total_de_jogos_jogador_computador_modo_de_jogo_2 +=1
            total_de_jogos_jogador_humano_modo_de_jogo_2 +=1
            print("O jogador humano venceu a disputa ")
            print("-------------------------")
        elif ((computador_modo_de_jogo_2 == 1 and jogador_1_modo_de_jogo_2 == 2) or (computador_modo_de_jogo_2 == 3 and jogador_1_modo_de_jogo_2 == 2) or (computador_modo_de_jogo_2 == 1 and jogador_1_modo_de_jogo_2 == 3)):
            vitoria_jogador_computador_modo_de_jogo_2 = vitoria_jogador_computador_modo_de_jogo_2 + 1
            derrota_jogador_humano_modo_de_jogo_2 = derrota_jogador_humano_modo_de_jogo_2 + 1
            total_de_jogos_jogador_computador_modo_de_jogo_2 += 1
            total_de_jogos_jogador_humano_modo_de_jogo_2 += 1
            print("O Computador venceu a disputa")
            print("------------------------")

        elif (jogador_1_modo_de_jogo_2 == computador_modo_de_jogo_2):
            empate_modo_2+=1
            total_de_jogos_jogador_computador_modo_de_jogo_2 +=1
            total_de_jogos_jogador_humano_modo_de_jogo_2 +=1
            print("Empate")
            print("-------------------------")
        print("Jogador 1: ")
        print("NÚMEROS DE PARTIDAS =", total_de_jogos_jogador_humano_modo_de_jogo_2)
        print("DERROTAS:", derrota_jogador_humano_modo_de_jogo_2)
        print("VITÓRIAS:", vitoria_jogador_humano_modo_de_jogo_2)
        print("EMPATES:", empate_modo_2)
        porcentual_de_vitorias_jogador_humano_modo_de_jogo_2 = ((vitoria_jogador_humano_modo_de_jogo_2 / total_de_jogos_jogador_humano_modo_de_jogo_2)) * 100
        print("PORCENTUAL DE VITÓRIAS :", porcentual_de_vitorias_jogador_humano_modo_de_jogo_2)
        print("---------------------------")
        print("Computador: ")
        print("NÚMEROS DE PARTIDAS =", total_de_jogos_jogador_computador_modo_de_jogo_2)
        print("VITÓRIAS:",vitoria_jogador_computador_modo_de_jogo_2 )
        print("DERROTAS:",derrota_jogador_computador_modo_de_jogo_2)
        print("EMPATES:",empate_modo_2)
        porcentual_de_vitorias_computador_modo_de_jogo_2 = ((vitoria_jogador_computador_modo_de_jogo_2/total_de_jogos_jogador_computador_modo_de_jogo_2) * 100)
        print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_computador_modo_de_jogo_2)
        print("---------------------------")
        menu_de_retorno()
    if modo_de_jogo == 3:
        print("Escolha sua jogada")
        print("[1]PEDRA")
        print("[2]PAPEL")
        print("[3]TESOURA")
        computador_1_modo_de_jogo_3 = randint(1, 3)
        computador_2_modo_de_jogo_3 = randint(1, 3)
        print("-------------------------")
        print("COMPUTADOR_1:",computador_1_modo_de_jogo_3)
        print("COMPUTADOR_2:",computador_2_modo_de_jogo_3)
        print("-------------------------")
        print("JO")
        print("KEN")
        print("PÔ")
        print("-------------------------")
        if (computador_1_modo_de_jogo_3 == 1 and computador_2_modo_de_jogo_3 == 2) or (computador_1_modo_de_jogo_3 == 3 and computador_2_modo_de_jogo_3 == 2) or (computador_1_modo_de_jogo_3 == 1 and computador_2_modo_de_jogo_3 == 3):
            global vitoria_computador_1_modo_de_jogo_3,derrota_computador_2_modo_de_jogo_3,total_de_jogos_computador_1_modo_de_jogo_3,total_de_jogos_computador_2_modo_de_jogo_3
            vitoria_computador_1_modo_de_jogo_3 = vitoria_computador_1_modo_de_jogo_3 + 1
            derrota_computador_2_modo_de_jogo_3 = derrota_computador_2_modo_de_jogo_3 + 1
            total_de_jogos_computador_1_modo_de_jogo_3 = total_de_jogos_computador_1_modo_de_jogo_3 + 1
            total_de_jogos_computador_2_modo_de_jogo_3 = total_de_jogos_computador_2_modo_de_jogo_3 + 1
            print("O computador 1 venceu a disputa ")
            print("-------------------------")
        elif ((computador_2_modo_de_jogo_3 == 2 and computador_1_modo_de_jogo_3 == 1) or (computador_2_modo_de_jogo_3 == 1 and computador_1_modo_de_jogo_3 == 3) or (computador_2_modo_de_jogo_3 == 3 and computador_1_modo_de_jogo_3 == 2)):
            global vitoria_computador_2_modo_de_jogo_3,derrota_computador_1_modo_de_jogo_3
            vitoria_computador_2_modo_de_jogo_3 = vitoria_computador_2_modo_de_jogo_3 + 1
            derrota_computador_1_modo_de_jogo_3 = derrota_computador_1_modo_de_jogo_3 + 1
            total_de_jogos_computador_2_modo_de_jogo_3= total_de_jogos_computador_2_modo_de_jogo_3 + 1
            total_de_jogos_computador_1_modo_de_jogo_3 = total_de_jogos_computador_1_modo_de_jogo_3 + 1
            print("O Computador 2 venceu a disputa")
            print("-------------------------")
        elif (computador_1_modo_de_jogo_3 == computador_2_modo_de_jogo_3):
            global empate_modo_3
            empate_modo_3+=1
            total_de_jogos_computador_1_modo_de_jogo_3 = total_de_jogos_computador_1_modo_de_jogo_3 + 1
            total_de_jogos_computador_2_modo_de_jogo_3 = total_de_jogos_computador_2_modo_de_jogo_3 + 1
            print("Empate")
        print("Computador 1: ")
        print("NÚMEROS DE PARTIDAS =", total_de_jogos_computador_1_modo_de_jogo_3)
        print("VITÓRIAS:", vitoria_computador_1_modo_de_jogo_3)
        print("DERROTAS:", derrota_computador_1_modo_de_jogo_3)
        print("EMPATES:", empate_modo_3)
        porcentual_de_vitorias_computador_1_modo_de_jogo_3 = ((vitoria_computador_1_modo_de_jogo_3/total_de_jogos_computador_1_modo_de_jogo_3)) * 100
        print("PORCENTUAL DE VITÓRIAS :",porcentual_de_vitorias_computador_1_modo_de_jogo_3)
        print("---------------------------")
        print("Computador 2: ")
        print("NÚMEROS DE PARTIDAS =", total_de_jogos_computador_2_modo_de_jogo_3)
        print("VITÓRIAS:", vitoria_computador_2_modo_de_jogo_3)
        print("DERROTAS:", derrota_computador_2_modo_de_jogo_3)
        print("EMPATES:", empate_modo_3)
        porcentual_de_vitorias_computador_2_modo_de_jogo_3 = ((vitoria_computador_2_modo_de_jogo_3 / total_de_jogos_computador_2_modo_de_jogo_3)) * 100
        print("PORCENTUAL DE VITÓRIAS:",porcentual_de_vitorias_computador_2_modo_de_jogo_3)
        print("-------------------------")
        menu_de_retorno()
    while modo_de_jogo == 4:
        print("DESLIGANDO O JOGO.")
        break
inicializando_o_jogo()

