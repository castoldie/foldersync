from setuptools import setup

setup(
    name='folder_sync',
    author='Edmondo Castoldi',
    author_email='edmondo.castoldi@protonmail.com',
    description='A simple folder synchronization tool',
    version='1.0',
    py_modules=['folder_sync'],
    install_requires=[
        'shutil',
    ],
    entry_points={
        'console_scripts': [
            'folder_sync = folder_sync:sync_folders'
        ]
    },
)