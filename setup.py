from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open ("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name="pacote_de_processamento_de_imagens",
    version="0.0.1",
    author="Heitor Estrela de Andrade",
    author_email="heitorestrela13@gmail.com",
    description="",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hestrela/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)