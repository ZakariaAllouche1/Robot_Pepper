import os
import numpy as np
from stl import mesh

while True:
    # Liste tous les fichiers STL dans le répertoire courant
    stl_files = [file for file in os.listdir() if file.endswith('.stl')]

    # Afficher les fichiers STL disponibles
    for i, stl_file in enumerate(stl_files):
        print(f"{i+1}. {stl_file}")

    # L'utilisateur sélectionne les fichiers à fusionner
    file_number1 = input("Veuillez entrer le numéro du premier fichier que vous voulez fusionner (ou '0' pour quitter) : ")
    file_number2 = input("Veuillez entrer le numéro du deuxième fichier que vous voulez fusionner (ou '0' pour quitter) : ")

    # Vérifie si l'utilisateur veut quitter le programme
    if file_number1 == '0' or file_number2 == '0':
        break

    file_number1 = int(file_number1)
    file_number2 = int(file_number2)

    # Charger les fichiers STL
    mesh1 = mesh.Mesh.from_file(stl_files[file_number1 - 1])
    mesh2 = mesh.Mesh.from_file(stl_files[file_number2 - 1])

    # L'utilisateur spécifie le vecteur de déplacement
    displacement_vector = np.array([float(n) for n in input("Veuillez entrer le vecteur de déplacement (séparé par des espaces) : ").split()])

    # Déplacer le deuxième mesh
    mesh2.x += displacement_vector[0]
    mesh2.y += displacement_vector[1]
    mesh2.z += displacement_vector[2]

    # Fusionner les deux mesh
    combined_mesh = mesh.Mesh(np.concatenate([mesh1.data, mesh2.data]))

    # Sauvegarder le mesh fusionné dans un nouveau fichier STL
    combined_mesh.save('combined.stl')
