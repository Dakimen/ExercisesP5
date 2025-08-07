"""Cette module contient l'exercice numéro 6."""


# Fonction calculate_average
def calculate_average(numbers_list):
    """Calcule la moyenne d'un liste de nombres passés comme argument."""
    average = sum(numbers_list) / len(numbers_list)
    return average


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
