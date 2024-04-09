from setuptools import setup, find_packages

setup(
    name='pdf_analyzer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pdfplumber',
    ],
    entry_points={
        'console_scripts': [
            'pdf-analyzer=pdf_analyzer.cli:main',
        ],
    },
)

