# Configures a brand new Ubuntu machine setting the custom HTTP header
package { 'nginx':
  name     => 'nginx',
  ensure   => 'installed',
  provider => 'apt',
}
exec { 'start nginx service':
  path    => '/usr/sbin',
  command => 'service nginx restart',
}
file_line { 'append a line in nginx config file':
  path  => '/etc/nginx/nginx.conf',
  line  => 'add_header X-Served-By $HOSTNAME;',
  after => 'http {',
}
