import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import tkinter as tk
from tkinter import filedialog

while True:
    # Créer une fenêtre Tkinter et la cacher
    root = tk.Tk()
    root.withdraw()

    # Ouvrir une boîte de dialogue pour sélectionner le fichier STL
    file_path = filedialog.askopenfilename(filetypes =[('STL Files', '*.stl')])

    # L'utilisateur a annulé la sélection du fichier
    if not file_path:
        break

    # Charger le fichier STL
    your_mesh = mesh.Mesh.from_file(file_path)

    # Créer un nouvel axe 3D
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)

    # Ajouter le mesh à l'axe créé
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

    # Auto scale pour le mesh
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    # Afficher le plot
    plt.show()
