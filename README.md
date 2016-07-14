# kodi-gpio-controller

Kodi remote controller by GPIO switch.

# Target

Raspberry PI and simulated system.

# Installation and setup

## Tested system

Raspberry PI2 and raspbian.

## Install scripts

~~~
$ sudo apt-get install python python-yaml
$ sudo python setup.py install
~~~

## Setup Kodi

### Enable JSON-RPC in Kodi

1. Launch Kodi
2. Open System
3. Open Services
4. Select "Web server"
5. Enable "Allow remote control via HTTP"
6. Input Port/Username/Password

### Add media path to Videos

1. Open Videos
2. Open Files
3. Open "Add videos..."
4. Browse media path and add to Videos

## Edit configuration file

Create yaml file based on [kodi-gpio.yml](sample/kodi-gpio.yml).

# Launch

~~~
$ sudo kodi-gpio -c sample/kodi-gpio.yml
~~~
