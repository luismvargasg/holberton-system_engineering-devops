# Configures a brand new Ubuntu machine setting the custom HTTP header
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}
file_line { 'append a line in nginx config file':
  path  => '/etc/nginx/nginx.conf',
  line  => 'add_header X-Served-By 1610-web-02;',
  after => 'http {',
}
