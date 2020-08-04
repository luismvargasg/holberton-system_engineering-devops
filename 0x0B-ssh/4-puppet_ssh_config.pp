# Puppet to make changes to our configuration file.
file_line { 'disable password login':
  path => '~/.ssh/config',
  line => 'PasswordAuthentication no',
}
file_line { 'add path to find the keys':
  path => '~/.ssh/config',
  line => 'IdentityFile ~/.ssh/holberton',
}
