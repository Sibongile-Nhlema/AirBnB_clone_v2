#!/usr/bin/python3
'''
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
of the AirBnB clone using def do_pack
'''

from fabric.api import *
from datetime import datetime
import os


def do_pack():
    ''' Function generates a tgz archive file if it doesn't exist '''
    local('sudo mkdir -p versions')

    t = datetime.now()
    time_string = t.strftime('%y%m%d%H%M%S')
    local('sudo tar -cvzf versions/web_static_{}.tgz web_static'.format(time_string))
    file_path = 'versions/web_static_{}.tgz'.format(time_string)
    file_string = os.path.getsize('{}'.format(file_path))
    print('web_static packed: {} -> {}'.format(file_path, file_string))


do_pack()
