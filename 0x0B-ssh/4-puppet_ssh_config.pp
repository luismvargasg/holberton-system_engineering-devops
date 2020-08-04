# Puppet to make changes to our configuration file.
::ssh::client::config::user { 'ubuntu':
  ensure  => present,
  options => {
    'Host'                   => '104.196.209.226',
    'IdentityFile'           => '~/.ssh/holberton',
    'PasswordAuthentication' => 'no',
  }
}
