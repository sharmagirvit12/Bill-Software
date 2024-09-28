from setuptools import setup, find_packages

setup(
    name='bill_software',  # Name of your project
    version='1.0.0',  # Version number
    description='A billing software application using Tkinter GUI',
    author='Girvit Sharma',  # Your name
    author_email='your_email@example.com',  # Your email
    url='https://github.com/sharmagirvit12/Bill-Software',  # GitHub URL
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[  # List of dependencies
        'tkinter',  # Add other dependencies as required
    ],
    entry_points={
        'console_scripts': [
            'bill-software=bill_software.main:main',  # Entry point to run your application
        ]
    }
)
