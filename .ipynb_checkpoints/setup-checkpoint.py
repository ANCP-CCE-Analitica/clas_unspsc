from setuptools import setup, find_packages


setup(
    name='clas_unspsc',
    version='0.3.2',
    license='MIT',
    author="Isaac Zainea",
    author_email='cizaineam@gmail.com',
    packages=find_packages('clas_unspsc'),
    package_dir={'': 'src'},
    url='https://github.com/ANCP-CCE-Analitica/clas_unspsc',
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
