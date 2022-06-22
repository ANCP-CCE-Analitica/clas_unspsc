from setuptools import setup, find_packages


setup(
    name='test_recomendación_unspsc',
    version='0.3',
    license='MIT',
    author="Isaac Zainea",
    author_email='cizaineam@gmail.com',
    packages=find_packages('clas_unspsc'),
    package_dir={'': 'clas_unspsc'},
    url='https://github.com/ANCP-CCE-Analitica/datos_abiertos',
    keywords='Compra pública, CCE, UNSPSC',
    install_requires=[
          'scikit-learn',
        'numpy',
        'pandas',
        'nltk',
        'spacy',
        'ipywidgets'
      ],

)
