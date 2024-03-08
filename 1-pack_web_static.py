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
    t_str = t.strftime('%y%m%d%H%M%S')
    local('sudo tar -cvzf versions/web_static_{}.tgz web_static'.format(t_str))
    f_path = 'versions/web_static_{}.tgz'.format(t_str)
    f_size = os.path.getsize('{}'.format(f_path))
    print('web_static packed: {} -> {}'.format(f_path, f_size))

do_pack()

