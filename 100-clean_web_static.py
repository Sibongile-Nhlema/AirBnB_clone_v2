#!/usr/bin/python3

"""Deletes out-of-date archives"""

from fabric.api import *
from os import listdir

env.hosts = ['100.25.211.5', '54.90.20.242']


def do_clean(number=0):
    """
    Deletes out-of-date archives

    Args:
    - number: number of archives to keep
    """

    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    versions = sorted(listdir('versions'))
    for i in range(number):
        versions.pop()

    with lcd('versions'):
        for version in versions:
            local(f"rm ./{version}")

    with cd('/data/web_static/releases'):
        releases = run('ls -tr').split()
        releases = [
            release for release in releases
            if 'web_static_' in release
            ]

        for i in range(number):
            releases.pop()

        for release in releases:
            run(f"rm -rf ./{release}")
