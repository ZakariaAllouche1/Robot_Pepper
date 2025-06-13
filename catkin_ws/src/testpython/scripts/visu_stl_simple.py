import os
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

while True:
    # Liste tous les fichiers STL dans le répertoire courant
    stl_files = [file for file in os.listdir() if file.endswith('.stl')]

    # Afficher les fichiers STL disponibles
    for i, stl_file in enumerate(stl_files):
        print(f"{i+1}. {stl_file}")

    # L'utilisateur sélectionne le fichier à visualiser
    file_number = input("Veuillez entrer le numéro du fichier que vous voulez visualiser (ou '0' pour quitter) : ")

    # Vérifie si l'utilisateur veut quitter le programme
    if file_number == '0':
        break

    file_number = int(file_number)

    # Charger le fichier STL
    your_mesh = mesh.Mesh.from_file(stl_files[file_number - 1])

    fig, axs = plt.subplots(1, 3, figsize=(24, 8))

    # Vue XY
    xy_vectors = your_mesh.vectors[:,:,:2]  # Prendre seulement X et Y
    collection = PolyCollection(xy_vectors, edgecolors='black', linewidths=1, alpha=0.1)
    axs[0].add_collection(collection)
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].set_title('Vue XY')
    axs[0].axis('equal')
    axs[0].grid(True)

    # Vue YZ
    yz_vectors = your_mesh.vectors[:,:,1:]  # Prendre seulement Y et Z
    collection = PolyCollection(yz_vectors, edgecolors='black', linewidths=1, alpha=0.1)
    axs[1].add_collection(collection)
    axs[1].set_xlabel('Y')
    axs[1].set_ylabel('Z')
    axs[1].set_title('Vue YZ')
    axs[1].axis('equal')
    axs[1].grid(True)

    # Vue ZX
    zx_vectors = your_mesh.vectors[:,:,::2]  # Prendre seulement Z et X
    collection = PolyCollection(zx_vectors, edgecolors='black', linewidths=1, alpha=0.1)
    axs[2].add_collection(collection)
    axs[2].set_xlabel('Z')
    axs[2].set_ylabel('X')
    axs[2].set_title('Vue ZX')
    axs[2].axis('equal')
    axs[2].grid(True)

    plt.show()
