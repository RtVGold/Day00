import random

def tri_croissant(tableau):
    n = len(tableau)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if tableau[j] < tableau[min_index]:
                min_index = j
        tableau[i], tableau[min_index] = tableau[min_index], tableau[i]
    return tableau

# Exemple de génération d'un tableau d'entiers aléatoires de plus de 15 indices
tableau_aleatoire = [random.randint(1, 100) for _ in range(20)]

print("Tableau avant le tri :", tableau_aleatoire)
tableau_trie = tri_croissant(tableau_aleatoire)
print("Tableau après le tri croissant :", tableau_trie)
