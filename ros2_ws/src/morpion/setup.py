import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'morpion'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(include=[package_name, f"{package_name}.*"]),
    data_files=[
        
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=[
        'setuptools',
        'ncnn',               
        'ultralytics',   
        'opencv-python',
    ],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='morpion@morpion.morpion',
    description='morpion',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_detection       = morpion.object_detection:main',
            'object_3d_localisation = morpion.object_3d_localisation:main',
            'board_localization     = morpion.board_localization:main',
            'board_state            = morpion.board_state:main',
            'morpion_mistral        = morpion.morpion_mistral:main',
            'pos_morpion            = morpion.pos_morpion:main',
            'initialisation         = morpion.initialisation:main',
            
        ],
    },
)