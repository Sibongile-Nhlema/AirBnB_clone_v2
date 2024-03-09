#!/usr/bin/python3
'''
a Fabric script that distributes an archive to
webservers.
'''

from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['100.25.222.45', '18.207.142.12']
env.user = 'ubuntu'


def do_pack():
    ''' Function generates a tgz archive file if it doesn't exist '''
    local('sudo mkdir -p versions')

    t = datetime.now()
    time_string = t.strftime('%y%m%d%H%M%S')
    local('sudo tar -cvzf \
            versions/web_static_{}.tgz web_static'.format(time_string))
    file_path = 'versions/web_static_{}.tgz'.format(time_string)
    file_string = os.path.getsize('{}'.format(file_path))
    print('web_static packed: {} -> {}'.format(file_path, file_string))


def do_deploy(archive_path):
    ''' delpoys the archive to the web servers '''
    if not exists(archive_path):
        return False

    try:
        # upload archive to /tmp/ in web server
        put(archive_path, '/tmp/')

        # Extract the contents of the archive to the web servers
        archive_filename = archive_path.split('/')[-1]
        folder_name = archive_filename.split('.')[0]
        run('sudo mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('sudo tar -xzf /tmp/{} -C \
                /data/web_static/releases/{}/'.format(archive_filename,
                                                      folder_name))

        # delete the uploae archive
        run('sudo rm /tmp/{}'.format(archive_filename))

        # delte the symbolic link and create a new one
        run('sudo rm -f /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False