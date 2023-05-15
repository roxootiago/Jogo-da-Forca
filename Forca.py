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

    def tentativa():
        champTentativa = input("Digite sua tentativa: ").upper()
        if champTentativa == champsRand:
            print(f"Parabéns! Você acertou!\nCampeão selecionado: {champsRand}")
            continuar()

        else:
            print(champTentativa)
            print("Você errou! Tente novamente")
            jogar()

    print(" ---x--- JOGO DA FORCA ---x---")
    print("--- ADIVINHE O NOME DO CHAMP ---")


    print(f"{title}\nO campeão tem {len(champsRand)} letras")

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

    print(champsRand)

    def jogar():
        for y in range(len(champsRand)):
            print(emptyList[y], end=" ")
        print()

        kick = input("Digite uma letra ou 'tentar' para tentar a palavra: ").upper()

        if kick == "TENTAR":
            tentativa()

        elif kick != "TENTAR":
            for z in range(len(champsRand)):
                if champsRand[z] == kick:
                    emptyList[z] = kick
                    if listChamp == emptyList:
                        print(f"Parabéns! Você completou a palavra\nCampeão selecionado: {champsRand}")
                        continuar()
                elif kick not in champsRand:
                    print("esta letra não está presente")
                    break
            jogar()

    jogar()

Forca()
