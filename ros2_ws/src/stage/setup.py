# import os
# from glob import glob
# from setuptools import setup, find_packages

# package_name = 'stage'

# setup(
#     name=package_name,
#     version='0.0.1',
#     packages=find_packages(include=[package_name, f"{package_name}.*"]),
#     data_files=[
#         # Pour ament_index
#         ('share/ament_index/resource_index/packages',
#             ['resource/' + package_name]),
#         # Copie du package.xml
#         ('share/' + package_name, ['package.xml']),
#         # Copie du dossier launch
#         (os.path.join('share', package_name, 'launch'),
#             glob(os.path.join('launch', '*launch.[pxy][yma]*')))
#     ],
#     install_requires=[
#         'setuptools',
#         'ncnn',                 # wheel Python
#         'ultralytics==8.2.0',   # déjà pip-installé mais déclaré ici
#         'opencv-python'
#     ],
#     zip_safe=True,
#     maintainer='ros',
#     maintainer_email='stage@stage.stage',
#     description='stage',
#     license='Apache-2.0',
#     tests_require=['pytest'],
#     entry_points={
#         'console_scripts': [
#             'object_detection       = stage.object_detection:main',
#             'decision               = stage.decision:main',
#             'sort_action            = stage.actions.sort_action:main',
#             'object_3d_localisation = stage.object_3d_localisation:main',
#             'interact_action        = stage.actions.interact_action:main',
#         ],
#     },
# )


import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'stage'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(include=[package_name, f"{package_name}.*"]),
    data_files=[
        # ament index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # package.xml
        ('share/' + package_name, ['package.xml']),
        # launch folder
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        # votre modèle NCNN exporté
        (os.path.join('share', package_name, 'yolov8s_ncnn_model'),
            glob(os.path.join('yolov8s_ncnn_model', '*'))),
    ],
    install_requires=[
        'setuptools',
        'ncnn',
        'opencv-python',
        'ultralytics==8.2.0',  # pour l’export si nécessaire
    ],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='stage@stage.stage',
    description='stage',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_detection       = stage.object_detection:main',
            'decision               = stage.decision:main',
            'object_3d_localisation = stage.object_3d_localisation:main',
            'interact_action        = stage.actions.interact_action:main',
        ],
    },
)
