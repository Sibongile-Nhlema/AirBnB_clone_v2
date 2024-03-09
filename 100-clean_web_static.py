#!/usr/bin/python3
'''
A Fabric script that deletes out-of-date archives
'''

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


def do_clean(number=0):
    ''' Deletes unnecessary archives '''

    number = int(number)
    if number == 0 or number == 1:
        number = 1

    with lcd('versions'):
        local('ls -1t | tail -n +{} | xargs rm -f'.format(number + 1))

    with cd('/data/web_static/releases'):
        run('ls -1t | tail -n +{} | xargs rm -rf'.format(number + 1))

    with cd('/data/web_static'):
        run('ls -1t | grep -v releases | xargs rm -rf')
