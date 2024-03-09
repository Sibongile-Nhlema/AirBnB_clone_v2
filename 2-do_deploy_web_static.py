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
    ''' Deploys the archive to the web servers '''
    if not exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ on the web server
        put(archive_path, '/tmp/')

        # Extract the contents of the archive to the web server
        archive_file = archive_path.split('/')[-1]
        base_name = archive_file.split('.')[0]
        deploy_path = '/data/web_static/releases/{}/'.format(base_name)

        run('sudo mkdir -p {}'.format(deploy_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_file, deploy_path))
        run('sudo rm /tmp/{}'.format(archive_file))

        # Move contents and delete web_static directory
        run('sudo mv {0}web_static/* {0}'.format(deploy_path))
        run('sudo rm -rf {0}web_static'.format(deploy_path))

        # Update symbolic link
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(deploy_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
