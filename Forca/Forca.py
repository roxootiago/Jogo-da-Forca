from random import choice
import cassiopeia as cass


def Forca():
    def champsGenerator():
        champions = cass.get_champions(region="BR")
        random_champion = choice(champions)
        return random_champion.name, random_champion.title

    name = champsGenerator()
    nameChamp = name[0]
    title = name[1]
    champsRand = nameChamp.upper()
    emptyList = []

    def continuar():
        opcao = input("Deseja jogar novamente? ").upper()
        if opcao == "S" or opcao == "SIM":

            Forca()

        else:

            print("Encerrando o jogo...")

    def tentativa(count):
        champTentativa = input("Digite sua tentativa: ").upper()
        if champTentativa == champsRand:
            print(f" \U0001f3c6Parabéns! Você acertou!\U0001f3c6\nCampeão selecionado: {nameChamp.capitalize()}: {title.title()} ")
            continuar()

        else:
            print("Você errou! Tente novamente")
            jogar(count+1)

    print(" ---x--- JOGO DA FORCA ---x---")
    print("--- ADIVINHE O NOME DO CHAMP ---")

    while True:
        nivel = int(input(
            "Escolha uma opção de nível:\n(1)Fácil = 10 tentativas\n(2)Médio = 5 tentativas\n(3)Difícil = 3 "
            "tentativas\nDigite sua opção: "))
        if nivel == 1:
            tentativas = 10
            break
        elif nivel == 2:
            tentativas = 5
            break
        elif nivel == 3:
            tentativas = 3
            break
        else:
            print("Digite um nível válido!")

    print(f"Dica: {title.title()}\nO campeão tem {len(champsRand)} letras")

    for k in range(len(champsRand)):
        emptyList.append("_")

    listChamp = list(champsRand)

    for t in range(len(champsRand)):
        if "'" in champsRand[t]:
            emptyList[t] = "'"
        if " " in champsRand[t]:
            emptyList[t] = " "
        if "." in champsRand[t]:
            emptyList[t] = "."

    def jogar(count = 1):
        while count <= tentativas:

            print(f"Tentativas: {count} de {tentativas}")
            for y in range(len(champsRand)):
                print(emptyList[y], end=" ")
            print()

            kick = input("Digite uma letra ou 'tentar' para tentar a palavra: ").upper()

            if kick == "TENTAR":
                tentativa(count)
                return

            if kick in emptyList:
                print(f"'{kick}' ja se encontra na palavra!\nDigite uma letra diferente")
            elif len(kick) > 1:
                print("Digite apenas uma letra ou 'tentar'!")

            elif kick != "TENTAR":
                letra_encontrada = False
                for z in range(len(champsRand)):
                    if champsRand[z] == kick:
                        emptyList[z] = kick
                        letra_encontrada = True

                if emptyList == listChamp:
                    print(f"\U0001f3c6Você completou a palavra!\U0001f3c6\nCampeão selecionado: {nameChamp.capitalize()}: {title.title()} ")
                    continuar()
                    break

                if not letra_encontrada:
                    print(f"A palavra não possui a letra '{kick}'")
                    count += 1
                if count > tentativas:
                    print(f"\U0001f480Você perdeu!\U0001f480\nCampeão selecionado foi: {nameChamp.capitalize()}: {title.title()} ")
                    continuar()
                    break

    jogar()