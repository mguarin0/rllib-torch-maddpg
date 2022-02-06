from setuptools import setup, find_packages

setup(name="pytorchmaddpg",
      version="1.0",
      packages=find_packages(),
      install_requires=[
          "ray[rllib,tune,default]==1.5.0",
          "numpy==1.21.1",
          "pyglet==1.5.15",
          "tensorflow==2.8.0",
          "torch==1.10.2",
          "gym==0.21.0",
          "pettingzoo[mpe]==1.15.0",
          "supersuit==3.3.3",
          "aiohttp==3.7.4",
      ])

