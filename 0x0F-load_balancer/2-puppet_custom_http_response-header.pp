# Configures a brand new Ubuntu machine setting the custom HTTP header
package { 'nginx':
  provider => 'apt-get',
  ensure => 'installed',
}
file_line { 'append a line in nginx config file':
  path  => '/etc/nginx/nginx.conf',
  line  => 'IdentityFile ~/.ssh/holberton',
  after => 'http {',
}
