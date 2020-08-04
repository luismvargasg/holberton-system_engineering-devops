# Puppet to make changes to our configuration file.
file_line { 'disable password login':
  path => '~/.ssh/holberton',
  line => 'PasswordAuthentication no',
}
file_line { 'add path to find the keys':
  path => '~/.ssh/holberton',
  line => 'IdentityFile ~/.ssh/holberton',
}
