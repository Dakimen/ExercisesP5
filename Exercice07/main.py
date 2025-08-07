"""Ce fichier contient l'exercice 7."""


def square(number):
    """Retourne le carré du nombre."""
    if isinstance(number, (int, float)):
        square = number * number
        return square
    else:
        print("Le paramètre doit être un nombre !")
        return None
    