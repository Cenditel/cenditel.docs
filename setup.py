from setuptools import setup, find_packages
#
# Note: This file does not really serve any purpose
# it just keeps some tools happy
# 
import os

version = '0.1'

setup(name='cenditel.documentation',
      version=version,
      description="Cenditel Foundation Plone Products Documentation in Sphinx format",
      #long_description=open("README.txt").read() + "\n",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='cenditel foundation, plone, products, documentation, ppm, audio, video, multimedia',
      author='Oswaldo Lopez, Víctor Terán Herrera, Leonardo J. Caballer G.',
      author_email='elalcon89@gmail.com, oswaldolo@hotmail.com, leonardocaballero@gmail.com',
      maintainer='Leonardo J. Caballero G.',
      maintainer_email='leonardocaballero@gmail.com',
      url='http://plataforma.cenditel.gob.ve/wiki/Plone',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      #namespace_packages=['gomobiletheme'],
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
