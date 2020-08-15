# Configures a brand new Ubuntu machine setting the custom HTTP header
package { 'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
}
file_line { 'append a line in nginx config file':
  path  => '/etc/nginx/nginx.conf',
  line  => "add_header X-Served-By ${hostname};",
  after => 'http {',
}
exec { 'sudo service nginx restart':
  path    => '/usr/sbin',
  command => 'service nginx restart',
}
