# Puppet manifest to setup web_static
# Place this file in /etc/puppet/modules/web_static/manifests

class web_static {
  file { '/data':
    ensure => 'directory',
  }

  file { '/data/web_static':
    ensure => 'directory',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
  }

  file { '/data/web_static/releases':
    ensure => 'directory',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
  }

  file { '/data/web_static/releases/test/index.html':
    content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  }
}

include web_static

