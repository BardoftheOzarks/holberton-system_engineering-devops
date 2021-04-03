# Configures SSH to connect without a password
file_line { 'Turn off passwd auth' :
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => 'PasswordAuthentication no'
}

file_line { 'Declare identity file' :
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => 'IdentityFile ~/.ssh/holberton'
}
