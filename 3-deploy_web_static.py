#!/usr/bin/python3

"""
Creates and distributes an archive to web servers.
"""

from fabric.api import env, put, run, local
from datetime import datetime
import os


env.hosts = ['100.25.211.5', '54.90.20.242']


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static directory"""

    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")

        archive_path = f"versions/web_static_{time}.tgz"

        local(f"tar -czvf {archive_path} web_static")

        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Uploads the archive to the /tmp/ of web server,
    uncompresses the archive, deletes the archive,
    deletes the symbolic link /data/web_static/current
    and creates a new the symbolic link linked to the
    new version of code on the web server.
    """

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')

        archive_name = archive_path.split('/')[-1]
        arch_no_extension = archive_name.split('.')[0]
        deploy_directory = f'/data/web_static/releases/{arch_no_extension}/'

        run(f'mkdir -p {deploy_directory}')
        run(f'tar -xzf /tmp/{archive_name} -C {deploy_directory}')
        run(f'rm /tmp/{archive_name}')
        run(
            """
            mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/
            """.format(arch_no_extension, arch_no_extension)
        )
        run(
            'rm -rf /data/web_static/releases/{}/web_static'.format(
                arch_no_extension
            )
            )
        run('rm -rf /data/web_static/current')
        run(f'ln -s {deploy_directory} /data/web_static/current')
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to web servers."""

    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
