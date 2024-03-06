#!/usr/bin/python3

"""
This script generates a .tgz archive from the contents
of the web_static directory of AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime


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
