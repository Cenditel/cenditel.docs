import os
from setuptools import setup, find_packages


version = '0.1'

setup(name='cenditel.docs',
      version=version,
      description="Cenditel Foundation Plone Products Documentation in Sphinx format",
      # long_description=open("README.rst").read() + "\n",
      # Get more strings from https://pypi.org/classifiers/
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='cenditel foundation, plone, products, documentation, ppm, audio, video, multimedia',
      author='Víctor Terán Herrera, Oswaldo Lopez, Leonardo J. Caballer G.',
      author_email='elalcon89@gmail.com, oswaldolo@hotmail.com, leonardocaballero@gmail.com',
      maintainer='Leonardo J. Caballero G.',
      maintainer_email='leonardocaballero@gmail.com',
      url='http://plataforma.cenditel.gob.ve/wiki/Plone',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
)
