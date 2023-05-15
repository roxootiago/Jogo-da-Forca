from random import choice
import cassiopeia as cass


def champs():
    champions = cass.get_champions(region="BR")
    random_champion = choice(champions)
    return random_champion.name


"""champ = champs()


def titleChamps():
    title = champ.title
    return title


def nameChampion():
    namChamp = champ.name
    return namChamp"""




