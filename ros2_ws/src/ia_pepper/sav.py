from setuptools import setup
from glob import glob
import os

package_name = 'ia_pepper'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	
            'whisper = ia_pepper.whisper_conversion_audio_texte:main',
            'mistral = ia_pepper.mistral_7b_llm:main',
            'demande_clavier = ia_pepper.demande_clavier:main',
            'reconnaissance_vocal = ia_pepper.reconnaissance_vocal:main',
            'retour_vocal = ia_pepper.retour_vocal:main',
            'test_bouge = ia_pepper.test_bouge:main',
            'envoie_commande = ia_pepper.envoie_commande:main',
            'mistral_morpion = ia_pepper.mistral_morpion:main',
            'test = ia_pepper.test:main',

        ],

    },
)

