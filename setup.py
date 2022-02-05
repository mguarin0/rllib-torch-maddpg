from setuptools import setup, find_packages

setup(name="pytorchmaddpg",
      version="1.0",
      packages=find_packages(),
      install_requires=[
          "ray[rllib,tune,default]==1.5.0",
          "tensorflow",
          "torch",
          "pettingzoo[mpe]",
          "supersuit",
          "aiohttp==3.7.4",
      ])
