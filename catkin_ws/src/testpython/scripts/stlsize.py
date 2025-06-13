import os
from stl import mesh

# Obtenir le répertoire courant
repertoire_courant = os.getcwd()

while True:
    # Rechercher les fichiers .stl dans le répertoire courant
    fichiers_stl = [fichier for fichier in os.listdir(repertoire_courant) if fichier.endswith(".stl")]

    # Afficher la liste des fichiers .stl
    print("Fichiers STL disponibles dans le répertoire courant:")
    for index, fichier in enumerate(fichiers_stl):
        print(f"{index+1}. {fichier}")
    print("0. Quitter")

    # Saisir le numéro du fichier choisi ou 0 pour sortir
    numero_fichier = int(input("Veuillez saisir le numéro du fichier STL pour connaître les dimensions (0 pour sortir) : "))

    # Vérifier si l'utilisateur souhaite quitter
    if numero_fichier == 0:
        break

    # Vérifier la validité du numéro de fichier saisi
    if numero_fichier < 1 or numero_fichier > len(fichiers_stl):
        print("Numéro de fichier invalide.")
    else:
        # Charger le fichier STL choisi
        fichier_stl = fichiers_stl[numero_fichier - 1]
        modele = mesh.Mesh.from_file(fichier_stl)

       
# Obtenir les valeurs minimales et maximales dans chaque direction
        min_x = modele.min_[0]
        max_x = modele.max_[0]
        min_y = modele.min_[1]
        max_y = modele.max_[1]
        min_z = modele.min_[2]
        max_z = modele.max_[2]

# Afficher les valeurs minimales et maximales
        print("Min et Max dans chaque direction :")
        print("X : Min =", min_x, ", Max =", max_x)
        print("Y : Min =", min_y, ", Max =", max_y)
        print("Z : Min =", min_z, ", Max =", max_z)
