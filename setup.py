from setuptools import setup, find_packages

setup(name='kodi-gpio',
      version='0.0.2',
      description='Kodi remote controller by GPIO switch',
      author='Koji Hachiya',
      author_email='koji.hachiya@gmail.com',
      url='https://github.com/koji88/kodi-gpio-controller/',
      packages=find_packages(),
      entry_points="""
      [console_scripts]
      kodi-gpio = scripts.main:main
      """,
      install_requires=[
          'sysfs-gpio',
          'twisted'
      ],
)
